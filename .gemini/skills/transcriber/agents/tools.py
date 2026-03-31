"""
Transcriber Agent Tools - ADK tool definitions.

These tools are used by the LLM agent for intelligent transcription tasks.
"""

import subprocess
from pathlib import Path
from typing import Optional

try:
    from google.adk import Tool, tool
    ADK_AVAILABLE = True
except ImportError:
    ADK_AVAILABLE = False
    # Mock decorator for when ADK is not available
    def tool(func):
        return func


SCRIPTS_DIR = Path(__file__).parent.parent / 'scripts'


@tool
def assess_pdf_tool(pdf_path: str) -> dict:
    """
    Assess a PDF to determine the best extraction method.

    Args:
        pdf_path: Path to the PDF file to assess

    Returns:
        Assessment with recommendation for extraction method
    """
    script = SCRIPTS_DIR / 'assess_pdf.py'

    result = subprocess.run(
        ['python', str(script), pdf_path],
        capture_output=True,
        text=True
    )

    output = result.stdout.lower()
    requires_ocr = 'pymupdf + pytesseract' in output or 'requires ocr: true' in output

    return {
        'requires_ocr': requires_ocr,
        'recommendation': 'ocr' if requires_ocr else 'text_extraction',
        'details': result.stdout
    }


@tool
def find_chapters_tool(pdf_path: str, chapter_num: Optional[int] = None) -> dict:
    """
    Find chapter boundaries in a PDF document.

    Args:
        pdf_path: Path to the PDF file
        chapter_num: Optional specific chapter number to find

    Returns:
        Chapter boundaries with page numbers
    """
    script = SCRIPTS_DIR / 'find_chapter.py'

    if chapter_num:
        result = subprocess.run(
            ['python', str(script), pdf_path, str(chapter_num)],
            capture_output=True,
            text=True
        )
    else:
        result = subprocess.run(
            ['python', str(script), pdf_path],
            capture_output=True,
            text=True
        )

    return {
        'success': result.returncode == 0,
        'chapters': result.stdout,
        'error': result.stderr if result.returncode != 0 else None
    }


@tool
def extract_pages_tool(
    pdf_path: str,
    start_page: int,
    end_page: int,
    use_ocr: bool = True,
    output_file: str = '/tmp/extracted.txt'
) -> dict:
    """
    Extract text from PDF pages.

    Args:
        pdf_path: Path to the PDF file
        start_page: First page to extract (1-indexed)
        end_page: Last page to extract (1-indexed)
        use_ocr: Whether to use OCR (for scanned PDFs) or text extraction
        output_file: Path for output file

    Returns:
        Extraction result with output file path
    """
    if use_ocr:
        script = SCRIPTS_DIR / 'extract_chapter.py'
    else:
        script = SCRIPTS_DIR / 'extract_text_only.py'

    result = subprocess.run(
        ['python', str(script), pdf_path, str(start_page), str(end_page), output_file],
        capture_output=True,
        text=True
    )

    return {
        'success': result.returncode == 0,
        'output_file': output_file,
        'method': 'ocr' if use_ocr else 'text',
        'pages_extracted': end_page - start_page + 1,
        'error': result.stderr if result.returncode != 0 else None
    }


@tool
def compare_texts_tool(ocr_text: str, markdown_text: str) -> dict:
    """
    Compare OCR extracted text with markdown transcription.

    Args:
        ocr_text: Text extracted via OCR from PDF
        markdown_text: Existing markdown transcription

    Returns:
        Comparison results with discrepancies found
    """
    import re

    discrepancies = []

    # Extract and compare numbers
    ocr_numbers = set(re.findall(r'\b\d+(?:,\d{3})*(?:\.\d+)?\b', ocr_text))
    md_numbers = set(re.findall(r'\b\d+(?:,\d{3})*(?:\.\d+)?\b', markdown_text))

    # Numbers only in markdown (potential transcription errors)
    only_in_md = md_numbers - ocr_numbers
    for num in only_in_md:
        discrepancies.append({
            'type': 'numeric',
            'markdown': num,
            'ocr': '[not found]',
            'action': 'verify'
        })

    # Numbers only in OCR (potential missing content)
    only_in_ocr = ocr_numbers - md_numbers
    for num in list(only_in_ocr)[:5]:  # Limit to 5
        discrepancies.append({
            'type': 'numeric',
            'markdown': '[not found]',
            'ocr': num,
            'action': 'verify'
        })

    return {
        'total_discrepancies': len(discrepancies),
        'numeric_discrepancies': len([d for d in discrepancies if d['type'] == 'numeric']),
        'discrepancies': discrepancies[:20],  # Limit to 20
        'ocr_word_count': len(ocr_text.split()),
        'markdown_word_count': len(markdown_text.split())
    }
