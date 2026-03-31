#!/usr/bin/env python3
"""
Video Transcriber — fetches transcripts from YouTube, Facebook, and other platforms.

Tier 1: youtube-transcript-api (YouTube only, ~2 seconds, no download)
Tier 2: yt-dlp subtitle extraction (any platform with captions, ~3-5 seconds, no download)
Tier 3: yt-dlp audio + Whisper (any platform, minutes, downloads audio)
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path


# --- Platform Detection ---

def detect_platform(url):
    """Detect which platform a URL belongs to."""
    url_lower = url.lower()
    if any(d in url_lower for d in ["youtube.com", "youtu.be"]):
        return "youtube"
    if any(d in url_lower for d in ["facebook.com", "fb.watch", "fb.com"]):
        return "facebook"
    if any(d in url_lower for d in ["instagram.com"]):
        return "instagram"
    if any(d in url_lower for d in ["tiktok.com"]):
        return "tiktok"
    if any(d in url_lower for d in ["x.com", "twitter.com"]):
        return "twitter"
    # Check if it looks like a bare YouTube video ID (11 chars, alphanumeric + _-)
    if re.match(r'^[a-zA-Z0-9_-]{11}$', url):
        return "youtube"
    return "other"


def extract_video_id(url):
    """Extract YouTube video ID from various URL formats."""
    patterns = [
        r'(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/|youtube\.com/v/)([a-zA-Z0-9_-]{11})',
        r'^([a-zA-Z0-9_-]{11})$',  # bare video ID
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def normalize_url(url, platform):
    """Ensure a URL is fully qualified for yt-dlp."""
    if platform == "youtube":
        video_id = extract_video_id(url)
        if video_id:
            return f"https://youtube.com/watch?v={video_id}"
    return url


# --- Dependency Checks ---

def check_primary_deps():
    """Check if youtube-transcript-api is installed."""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        return True
    except ImportError:
        return False


def check_fallback_deps():
    """Check if yt-dlp and whisper are available."""
    yt_dlp = subprocess.run(["which", "yt-dlp"], capture_output=True).returncode == 0
    whisper = subprocess.run(["which", "whisper"], capture_output=True).returncode == 0
    return yt_dlp, whisper


def check_ytdlp():
    """Check if yt-dlp is available."""
    return subprocess.run(["which", "yt-dlp"], capture_output=True).returncode == 0


# --- Metadata ---

def get_video_metadata(url, platform):
    """Fetch video metadata using yt-dlp. Works for any supported platform."""
    resolved_url = normalize_url(url, platform)
    try:
        result = subprocess.run(
            ["yt-dlp", "--dump-json", "--no-download", resolved_url],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            data = json.loads(result.stdout)
            duration_secs = data.get("duration", 0) or 0
            minutes = int(duration_secs // 60)
            seconds = int(duration_secs % 60)

            # Extract chapter markers if available
            chapters = []
            for ch in data.get("chapters", []) or []:
                chapters.append({
                    "title": ch.get("title", ""),
                    "start_time": ch.get("start_time", 0),
                })

            return {
                "title": data.get("title", "Unknown Title"),
                "channel": data.get("channel", data.get("uploader", "Unknown Channel")),
                "duration": f"{minutes}:{seconds:02d}",
                "duration_seconds": duration_secs,
                "chapters": chapters,
                "platform": platform,
            }
    except (subprocess.TimeoutExpired, json.JSONDecodeError, FileNotFoundError):
        pass
    return {
        "title": "Unknown Title",
        "channel": "Unknown Channel",
        "duration": "Unknown",
        "duration_seconds": 0,
        "chapters": [],
        "platform": platform,
    }


# --- Tier 1: youtube-transcript-api (YouTube only) ---

def transcribe_youtube_api(video_id, lang="en"):
    """Fetch transcript using youtube-transcript-api v1.x. YouTube only."""
    from youtube_transcript_api import YouTubeTranscriptApi

    api = YouTubeTranscriptApi()
    transcript_list = api.list(video_id)

    transcript_meta = None

    # First try: exact match (manual)
    try:
        transcript_meta = transcript_list.find_manually_created_transcript([lang])
    except Exception:
        pass

    # Second try: exact match (auto-generated)
    if transcript_meta is None:
        try:
            transcript_meta = transcript_list.find_generated_transcript([lang])
        except Exception:
            pass

    # Third try: any available transcript
    if transcript_meta is None:
        try:
            for t in transcript_list:
                transcript_meta = t
                break
        except Exception:
            pass

    if transcript_meta is None:
        return None, None, None

    fetched = api.fetch(video_id, languages=[transcript_meta.language_code])
    entries = [
        {"start": snippet.start, "duration": snippet.duration, "text": snippet.text}
        for snippet in fetched
    ]

    is_generated = transcript_meta.is_generated
    lang_name = re.sub(r'\s*\(auto-generated\)\s*$', '', transcript_meta.language)
    lang_label = f"{lang_name} ({'auto-generated' if is_generated else 'manual'})"
    return entries, lang_label, None


# --- Tier 2: yt-dlp subtitle extraction (any platform with captions) ---

def transcribe_subtitles(url, platform, lang="en"):
    """Extract subtitles using yt-dlp without downloading the video.

    Works for any platform where captions exist (YouTube, Facebook, etc.).
    Returns transcript entries or None if no subtitles available.
    """
    resolved_url = normalize_url(url, platform)

    with tempfile.TemporaryDirectory() as tmpdir:
        output_template = os.path.join(tmpdir, "subs")

        # Try to get both manual and auto-generated subtitles
        cmd = [
            "yt-dlp",
            "--write-sub",
            "--write-auto-sub",
            "--sub-lang", lang,
            "--sub-format", "json3/vtt/srt/best",
            "--skip-download",
            "-o", output_template,
            resolved_url,
        ]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

        # Look for subtitle files in the temp directory
        sub_files = list(Path(tmpdir).glob("subs*.vtt")) + \
                    list(Path(tmpdir).glob("subs*.srt")) + \
                    list(Path(tmpdir).glob("subs*.json3"))

        if not sub_files:
            return None, None, "No subtitles available on this platform"

        sub_file = sub_files[0]
        suffix = sub_file.suffix.lower()

        # Parse subtitle file into entries
        entries = []
        if suffix == ".json3":
            entries = parse_json3_subtitles(sub_file)
        elif suffix == ".vtt":
            entries = parse_vtt_subtitles(sub_file)
        elif suffix == ".srt":
            entries = parse_srt_subtitles(sub_file)

        if not entries:
            return None, None, "Subtitle file found but could not parse"

        # Determine if auto-generated
        filename = sub_file.name
        is_auto = "auto" in result.stderr.lower() or ".auto." in filename
        lang_label = f"{lang} ({'auto-generated' if is_auto else 'manual'}) [yt-dlp subtitles]"

        return entries, lang_label, None


def parse_json3_subtitles(filepath):
    """Parse JSON3 subtitle format from yt-dlp."""
    entries = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        for event in data.get("events", []):
            start_ms = event.get("tStartMs", 0)
            duration_ms = event.get("dDurationMs", 0)
            segs = event.get("segs", [])
            text = "".join(s.get("utf8", "") for s in segs).strip()
            if text and text != "\n":
                entries.append({
                    "start": start_ms / 1000.0,
                    "duration": duration_ms / 1000.0,
                    "text": text,
                })
    except (json.JSONDecodeError, KeyError):
        pass
    return entries


def parse_vtt_subtitles(filepath):
    """Parse WebVTT subtitle format."""
    entries = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Match VTT timestamp lines: 00:00:01.234 --> 00:00:05.678
        blocks = re.split(r'\n\n+', content)
        for block in blocks:
            time_match = re.search(
                r'(\d{1,2}:?\d{2}:\d{2}[.,]\d{3})\s*-->\s*(\d{1,2}:?\d{2}:\d{2}[.,]\d{3})',
                block
            )
            if time_match:
                start = parse_vtt_timestamp(time_match.group(1))
                end = parse_vtt_timestamp(time_match.group(2))
                # Text is everything after the timestamp line
                text_lines = block.split('\n')
                text_start = None
                for i, line in enumerate(text_lines):
                    if '-->' in line:
                        text_start = i + 1
                        break
                if text_start is not None:
                    text = ' '.join(text_lines[text_start:]).strip()
                    # Remove VTT styling tags
                    text = re.sub(r'<[^>]+>', '', text)
                    if text:
                        entries.append({
                            "start": start,
                            "duration": end - start,
                            "text": text,
                        })
    except Exception:
        pass
    return entries


def parse_vtt_timestamp(ts):
    """Convert VTT timestamp (HH:MM:SS.mmm or MM:SS.mmm) to seconds."""
    ts = ts.replace(',', '.')
    parts = ts.split(':')
    if len(parts) == 3:
        h, m, s = parts
        return int(h) * 3600 + int(m) * 60 + float(s)
    elif len(parts) == 2:
        m, s = parts
        return int(m) * 60 + float(s)
    return 0


def parse_srt_subtitles(filepath):
    """Parse SRT subtitle format."""
    entries = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        blocks = re.split(r'\n\n+', content.strip())
        for block in blocks:
            lines = block.strip().split('\n')
            if len(lines) >= 3:
                time_match = re.search(
                    r'(\d{2}:\d{2}:\d{2}[.,]\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}[.,]\d{3})',
                    lines[1]
                )
                if time_match:
                    start = parse_vtt_timestamp(time_match.group(1))
                    end = parse_vtt_timestamp(time_match.group(2))
                    text = ' '.join(lines[2:]).strip()
                    if text:
                        entries.append({
                            "start": start,
                            "duration": end - start,
                            "text": text,
                        })
    except Exception:
        pass
    return entries


# --- Tier 3: yt-dlp audio + Whisper (universal fallback) ---

def transcribe_whisper(url, platform, whisper_model="base", start_time=None, end_time=None):
    """Download audio with yt-dlp and transcribe with Whisper.

    Works for any platform supported by yt-dlp.
    """
    resolved_url = normalize_url(url, platform)

    with tempfile.TemporaryDirectory() as tmpdir:
        audio_path = os.path.join(tmpdir, "audio.mp3")

        ytdlp_cmd = [
            "yt-dlp",
            "--extract-audio",
            "--audio-format", "mp3",
            "--audio-quality", "5",
        ]

        if start_time or end_time:
            section = f"*{start_time or '0'}-{end_time or 'inf'}"
            ytdlp_cmd.extend(["--download-sections", section])
            time_range = f"{start_time or '0:00'} to {end_time or 'end'}"
            print(f"  Downloading audio ({time_range})...", file=sys.stderr)
        else:
            print("  Downloading audio...", file=sys.stderr)

        ytdlp_cmd.extend(["-o", audio_path, resolved_url])

        result = subprocess.run(
            ytdlp_cmd,
            capture_output=True, text=True, timeout=600
        )
        if result.returncode != 0:
            return None, None, f"yt-dlp failed: {result.stderr.strip()}"

        audio_files = list(Path(tmpdir).glob("audio.*"))
        if not audio_files:
            return None, None, "No audio file produced by yt-dlp"
        actual_audio = str(audio_files[0])

        print(f"  Transcribing with Whisper ({whisper_model} model)...", file=sys.stderr)
        result = subprocess.run(
            [
                "whisper", actual_audio,
                "--model", whisper_model,
                "--output_format", "json",
                "--output_dir", tmpdir,
            ],
            capture_output=True, text=True, timeout=600
        )
        if result.returncode != 0:
            return None, None, f"Whisper failed: {result.stderr.strip()}"

        json_files = list(Path(tmpdir).glob("*.json"))
        if not json_files:
            return None, None, "No Whisper output produced"

        with open(json_files[0]) as f:
            whisper_data = json.load(f)

        entries = []
        for segment in whisper_data.get("segments", []):
            entries.append({
                "start": segment["start"],
                "duration": segment["end"] - segment["start"],
                "text": segment["text"].strip(),
            })

        return entries, "Whisper transcription", None


# --- Formatting ---

def format_timestamp(seconds):
    """Convert seconds to MM:SS or HH:MM:SS format."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def format_verbatim_transcript(entries):
    """Format transcript entries as [MM:SS] timestamped idea-sized paragraphs."""
    if not entries:
        return ""

    paragraphs = []
    current_texts = []
    current_start = None
    sentence_count = 0

    for entry in entries:
        text = entry.get("text", "").strip()
        if not text:
            continue

        if current_start is None:
            current_start = entry.get("start", 0)

        current_texts.append(text)
        sentence_count += text.count('.') + text.count('!') + text.count('?')

        if sentence_count >= 3:
            ts = format_timestamp(current_start)
            paragraphs.append(f"[{ts}] {' '.join(current_texts)}")
            current_texts = []
            current_start = None
            sentence_count = 0

    if current_texts:
        ts = format_timestamp(current_start)
        paragraphs.append(f"[{ts}] {' '.join(current_texts)}")

    return "\n\n".join(paragraphs)


def build_markdown(metadata, entries, lang_label, url):
    """Build the final markdown output."""
    verbatim = format_verbatim_transcript(entries)

    lines = [
        f"# {metadata['title']}",
        "",
        f"**Channel**: {metadata['channel']}",
        f"**Duration**: {metadata['duration']}",
        f"**Language**: {lang_label}",
        f"**URL**: {url}",
        f"**Transcribed**: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "---",
        "",
        "## Organized Notes",
        "",
        "<!-- PLACEHOLDER: Gemini will replace this with a detailed summary -->",
        "",
        "---",
        "",
        "## Transcript",
        "",
        verbatim,
        "",
    ]
    return "\n".join(lines)


def slugify(text, max_length=80):
    """Convert text to a filesystem-safe slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text).strip('-')
    return text[:max_length]


# --- Main Processing ---

def process_video(url, args):
    """Process a single video URL with 3-tier transcript strategy."""
    platform = detect_platform(url)

    # Validate we have the tools we need
    if platform != "youtube" and not check_ytdlp():
        return None, None, f"yt-dlp is required for {platform} videos. Install: brew install yt-dlp"

    # Fetch metadata
    print(f"Fetching metadata for {platform} video...", file=sys.stderr)
    if platform == "youtube":
        video_id = extract_video_id(url)
        if not video_id:
            return None, None, f"Could not extract video ID from: {url}"
        metadata = get_video_metadata(url, platform)
    else:
        metadata = get_video_metadata(url, platform)

    print(f"Title: \"{metadata['title']}\"", file=sys.stderr)

    entries = None
    lang_label = None
    error = None

    # --- Tier 1: youtube-transcript-api (YouTube only) ---
    if platform == "youtube" and not args.force_whisper and check_primary_deps():
        print(f"  [Tier 1] Trying youtube-transcript-api...", file=sys.stderr)
        try:
            video_id = extract_video_id(url)
            entries, lang_label, error = transcribe_youtube_api(video_id, args.lang)
            if entries:
                print(f"  [Tier 1] Success: {len(entries)} segments", file=sys.stderr)
        except Exception as e:
            error = str(e)
            print(f"  [Tier 1] Failed: {error}", file=sys.stderr)

    # --- Tier 2: yt-dlp subtitle extraction (any platform) ---
    if entries is None and not args.force_whisper and check_ytdlp():
        print(f"  [Tier 2] Trying yt-dlp subtitle extraction...", file=sys.stderr)
        try:
            entries, lang_label, error = transcribe_subtitles(url, platform, args.lang)
            if entries:
                print(f"  [Tier 2] Success: {len(entries)} segments", file=sys.stderr)
            else:
                print(f"  [Tier 2] No subtitles found", file=sys.stderr)
        except Exception as e:
            error = str(e)
            print(f"  [Tier 2] Failed: {error}", file=sys.stderr)

    # --- Tier 3: yt-dlp audio + Whisper (universal fallback) ---
    if entries is None and (args.fallback or args.force_whisper):
        has_ytdlp, has_whisper = check_fallback_deps()
        if not has_ytdlp:
            return None, metadata["title"], "Tier 3 requires yt-dlp. Install: brew install yt-dlp"
        if not has_whisper:
            return None, metadata["title"], "Tier 3 requires whisper. Install: pip3 install openai-whisper"

        tier_label = "Force-Whisper" if args.force_whisper else "Tier 3"
        print(f"  [{tier_label}] Downloading audio + Whisper transcription...", file=sys.stderr)
        entries, lang_label, error = transcribe_whisper(
            url, platform, args.whisper_model,
            start_time=args.start, end_time=args.end
        )
        if entries:
            print(f"  [{tier_label}] Success: {len(entries)} segments", file=sys.stderr)

    if entries is None:
        suggestion = " Try re-running with --fallback to use Whisper." if not args.fallback else ""
        err_detail = f" ({error})" if error else ""
        return None, metadata["title"], f"No transcript available for \"{metadata['title']}\"{err_detail}.{suggestion}"

    # Build canonical URL
    if platform == "youtube":
        video_id = extract_video_id(url)
        canonical_url = f"https://youtube.com/watch?v={video_id}"
    else:
        canonical_url = url

    markdown = build_markdown(metadata, entries, lang_label, canonical_url)
    return markdown, metadata["title"], None


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe videos from YouTube, Facebook, and other platforms to markdown."
    )
    parser.add_argument("urls", nargs="+", help="Video URL(s) — YouTube, Facebook, Instagram, TikTok, etc.")
    parser.add_argument("--lang", default="en",
                        help="Preferred transcript language (ISO code, default: en)")
    parser.add_argument("--output", "-o", default=None,
                        help="Output file path, or directory for batch mode")
    parser.add_argument("--fallback", action="store_true",
                        help="Enable Whisper fallback for videos without captions")
    parser.add_argument("--force-whisper", action="store_true",
                        help="Skip caption extraction entirely and use Whisper")
    parser.add_argument("--whisper-model", default="base",
                        choices=["tiny", "base", "small", "medium", "large"],
                        help="Whisper model size (default: base)")
    parser.add_argument("--start", default=None,
                        help="Start time for partial transcription (requires --force-whisper)")
    parser.add_argument("--end", default=None,
                        help="End time for partial transcription (requires --force-whisper)")

    args = parser.parse_args()

    # Check minimum dependencies
    has_primary = check_primary_deps()
    has_ytdlp = check_ytdlp()

    if not has_primary and not has_ytdlp:
        print("ERROR: No transcription tools available.", file=sys.stderr)
        print("Install at least one:", file=sys.stderr)
        print("  pip3 install youtube-transcript-api  (YouTube captions)", file=sys.stderr)
        print("  brew install yt-dlp                  (multi-platform subtitles + audio)", file=sys.stderr)
        sys.exit(1)

    is_batch = len(args.urls) > 1
    output_is_dir = args.output and (args.output.endswith("/") or os.path.isdir(args.output))

    if is_batch and args.output:
        os.makedirs(args.output, exist_ok=True)
        output_is_dir = True

    results = []
    errors = []

    for url in args.urls:
        markdown, title, error = process_video(url, args)

        if error:
            errors.append(error)
            print(f"ERROR: {error}", file=sys.stderr)
            continue

        results.append((markdown, title))

        if args.output:
            if output_is_dir or is_batch:
                out_dir = args.output if output_is_dir else os.path.dirname(args.output)
                os.makedirs(out_dir, exist_ok=True)
                timestamp = datetime.now().strftime("%y%m%d-%H%M")
                filename = f"{timestamp}-{slugify(title)}.md"
                filepath = os.path.join(out_dir, filename)
            else:
                filepath = args.output

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(markdown)
            print(f"Saved: {filepath}", file=sys.stderr)
        else:
            print(markdown)
            if is_batch and url != args.urls[-1]:
                print("\n---\n")

    if is_batch:
        print(f"\nProcessed: {len(results)} succeeded, {len(errors)} failed", file=sys.stderr)

    if errors and not results:
        sys.exit(1)


if __name__ == "__main__":
    main()
