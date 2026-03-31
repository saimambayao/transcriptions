"""
Transcribe Workflow - Full PDF to markdown transcription.

This workflow extracts text from PDF and converts it to formatted markdown.
"""

import re
from pathlib import Path
from dataclasses import dataclass
from typing import Optional
from datetime import datetime

from .extract_workflow import ExtractWorkflow, ExtractConfig, ExtractInput


@dataclass
class TranscribeInput:
    """Input for transcribe workflow."""
    pdf_path: str
    start_page: int
    end_page: int
    output_path: str
    title: Optional[str] = None
    source_name: Optional[str] = None


@dataclass
class TranscribeOutput:
    """Output from transcribe workflow."""
    success: bool
    output_path: str
    word_count: int = 0
    page_count: int = 0
    error: Optional[str] = None


class TranscribeWorkflow:
    """
    Workflow for transcribing PDF pages to markdown.

    Steps:
    1. Extract OCR text from PDF
    2. Clean and format the text
    3. Convert to markdown structure
    4. Write output file with source citation
    """

    def __init__(self, extract_config: Optional[ExtractConfig] = None):
        self.extract_workflow = ExtractWorkflow(extract_config)

    def read_file(self, path: str) -> str:
        """Read file contents."""
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    def write_file(self, path: str, content: str) -> None:
        """Write content to file."""
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

    def clean_ocr_text(self, text: str) -> str:
        """Clean common OCR artifacts."""
        # Remove page markers
        text = re.sub(r'={60}\nPAGE \d+\n={60}', '\n', text)

        # Fix common OCR errors
        text = text.replace('|', 'I')  # Pipe to I
        text = re.sub(r'(\d),(\d{3})', r'\1,\2', text)  # Fix number formatting

        # Normalize whitespace
        text = re.sub(r'\n{3,}', '\n\n', text)  # Max 2 newlines
        text = re.sub(r' {2,}', ' ', text)  # Max 1 space

        # Fix hyphenation at line breaks
        text = re.sub(r'(\w)-\n(\w)', r'\1\2', text)

        return text.strip()

    def detect_headers(self, text: str) -> str:
        """Detect and format headers in the text."""
        lines = text.split('\n')
        result = []

        for line in lines:
            stripped = line.strip()

            # Chapter headers (all caps, short)
            if re.match(r'^CHAPTER\s+\d+', stripped, re.IGNORECASE):
                result.append(f'\n# {stripped.title()}\n')

            # Section headers (numbered sections)
            elif re.match(r'^\d+\.\d+\s+[A-Z]', stripped):
                result.append(f'\n## {stripped}\n')

            # Subsection headers
            elif re.match(r'^\d+\.\d+\.\d+\s+', stripped):
                result.append(f'\n### {stripped}\n')

            # All caps lines (potential headers)
            elif stripped.isupper() and len(stripped) < 100 and len(stripped) > 3:
                result.append(f'\n## {stripped.title()}\n')

            else:
                result.append(line)

        return '\n'.join(result)

    def format_tables(self, text: str) -> str:
        """Attempt to format tabular data as markdown tables."""
        # This is a simplified implementation
        # Full table detection would require more sophisticated analysis
        return text

    def format_lists(self, text: str) -> str:
        """Format bulleted and numbered lists."""
        lines = text.split('\n')
        result = []

        for line in lines:
            stripped = line.strip()

            # Bullet points
            if stripped.startswith(('•', '●', '○', '-', '*')):
                result.append(f'- {stripped[1:].strip()}')

            # Numbered lists (1., 2., etc.)
            elif re.match(r'^\d+\.\s', stripped):
                result.append(stripped)

            # Lettered lists (a., b., etc.)
            elif re.match(r'^[a-z]\.\s', stripped, re.IGNORECASE):
                result.append(stripped)

            else:
                result.append(line)

        return '\n'.join(result)

    def add_source_citation(
        self,
        content: str,
        source_name: str,
        start_page: int,
        end_page: int
    ) -> str:
        """Add source citation footer."""
        date = datetime.now().strftime('%Y-%m-%d')
        citation = f"""

---

**Source:** {source_name}, Pages {start_page}-{end_page}.

**Transcribed:** {date}
"""
        return content + citation

    def run(self, input_data: TranscribeInput) -> TranscribeOutput:
        """
        Execute the transcribe workflow.

        Args:
            input_data: TranscribeInput with paths and options

        Returns:
            TranscribeOutput with results
        """
        try:
            # Step 1: Extract OCR text
            extract_result = self.extract_workflow.run(ExtractInput(
                pdf_path=input_data.pdf_path,
                start_page=input_data.start_page,
                end_page=input_data.end_page,
                output_file='/tmp/transcribe_ocr.txt'
            ))

            if not extract_result.success:
                return TranscribeOutput(
                    success=False,
                    output_path=input_data.output_path,
                    error=f'OCR extraction failed: {extract_result.error}'
                )

            # Step 2: Read and clean OCR text
            raw_text = self.read_file(extract_result.output_file)
            cleaned_text = self.clean_ocr_text(raw_text)

            # Step 3: Format as markdown
            markdown = cleaned_text
            markdown = self.detect_headers(markdown)
            markdown = self.format_lists(markdown)
            markdown = self.format_tables(markdown)

            # Add title if provided
            if input_data.title:
                markdown = f'# {input_data.title}\n\n{markdown}'

            # Step 4: Add source citation
            source_name = input_data.source_name or Path(input_data.pdf_path).name
            markdown = self.add_source_citation(
                markdown,
                source_name,
                input_data.start_page,
                input_data.end_page
            )

            # Step 5: Write output
            self.write_file(input_data.output_path, markdown)

            # Calculate stats
            word_count = len(markdown.split())
            page_count = input_data.end_page - input_data.start_page + 1

            return TranscribeOutput(
                success=True,
                output_path=input_data.output_path,
                word_count=word_count,
                page_count=page_count
            )

        except Exception as e:
            return TranscribeOutput(
                success=False,
                output_path=input_data.output_path,
                error=str(e)
            )


# Convenience function
def transcribe_pdf(
    pdf_path: str,
    start_page: int,
    end_page: int,
    output_path: str,
    title: Optional[str] = None,
    source_name: Optional[str] = None
) -> TranscribeOutput:
    """
    Convenience function to transcribe PDF to markdown.

    Example:
        result = transcribe_pdf(
            'document.pdf',
            1, 20,
            'output/chapter1.md',
            title='Chapter 1: Introduction'
        )
        if result.success:
            print(f'Transcribed {result.word_count} words')
    """
    workflow = TranscribeWorkflow()
    return workflow.run(TranscribeInput(
        pdf_path=pdf_path,
        start_page=start_page,
        end_page=end_page,
        output_path=output_path,
        title=title,
        source_name=source_name
    ))
