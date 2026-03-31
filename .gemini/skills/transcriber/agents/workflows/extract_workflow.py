"""
Extract Workflow - OCR extraction from PDF pages.

This workflow handles PDF text extraction using either:
- pdfplumber for PDFs with embedded text
- PyMuPDF + pytesseract for scanned/image-based PDFs
"""

import subprocess
import tempfile
from pathlib import Path
from dataclasses import dataclass
from typing import Optional

try:
    from google.adk import Workflow, Step
    from google.adk.workflows import SequentialWorkflow
    ADK_AVAILABLE = True
except ImportError:
    ADK_AVAILABLE = False
    Workflow = object
    Step = object
    SequentialWorkflow = object


@dataclass
class ExtractConfig:
    """Configuration for PDF extraction."""
    dpi: int = 400  # 300=fast, 400=balanced, 600=high-quality
    output_dir: str = '/tmp'
    scripts_dir: str = str(Path(__file__).parent.parent.parent / 'scripts')


@dataclass
class ExtractInput:
    """Input for extract workflow."""
    pdf_path: str
    start_page: int
    end_page: int
    output_file: Optional[str] = None


@dataclass
class ExtractOutput:
    """Output from extract workflow."""
    success: bool
    output_file: str
    extraction_method: str  # 'ocr' or 'text'
    pages_extracted: int
    error: Optional[str] = None


class ExtractWorkflow:
    """
    Workflow for extracting text from PDF pages.

    Steps:
    1. Assess PDF quality to determine extraction method
    2. Extract text using appropriate method
    3. Return extracted text file path
    """

    def __init__(self, config: Optional[ExtractConfig] = None):
        self.config = config or ExtractConfig()

    def assess_pdf(self, pdf_path: str) -> dict:
        """
        Assess PDF to determine extraction method.

        Returns:
            dict with 'requires_ocr' boolean and 'recommendation' string
        """
        script = Path(self.config.scripts_dir) / 'assess_pdf.py'

        result = subprocess.run(
            ['python', str(script), pdf_path],
            capture_output=True,
            text=True
        )

        output = result.stdout.lower()
        requires_ocr = 'pymupdf + pytesseract' in output or 'requires ocr: true' in output

        return {
            'requires_ocr': requires_ocr,
            'recommendation': 'ocr' if requires_ocr else 'text',
            'raw_output': result.stdout
        }

    def extract_with_ocr(
        self,
        pdf_path: str,
        start_page: int,
        end_page: int,
        output_file: str
    ) -> dict:
        """Extract text using OCR (for scanned PDFs)."""
        script = Path(self.config.scripts_dir) / 'extract_chapter.py'

        result = subprocess.run(
            ['python', str(script), pdf_path, str(start_page), str(end_page), output_file],
            capture_output=True,
            text=True
        )

        return {
            'success': result.returncode == 0,
            'output': result.stdout,
            'error': result.stderr if result.returncode != 0 else None
        }

    def extract_text_only(
        self,
        pdf_path: str,
        start_page: int,
        end_page: int,
        output_file: str
    ) -> dict:
        """Extract embedded text (for text-based PDFs)."""
        script = Path(self.config.scripts_dir) / 'extract_text_only.py'

        result = subprocess.run(
            ['python', str(script), pdf_path, str(start_page), str(end_page), output_file],
            capture_output=True,
            text=True
        )

        return {
            'success': result.returncode == 0,
            'output': result.stdout,
            'error': result.stderr if result.returncode != 0 else None
        }

    def run(self, input_data: ExtractInput) -> ExtractOutput:
        """
        Execute the extract workflow.

        Args:
            input_data: ExtractInput with pdf_path, start_page, end_page

        Returns:
            ExtractOutput with results
        """
        # Determine output file
        output_file = input_data.output_file or f'{self.config.output_dir}/ocr_output.txt'

        # Step 1: Assess PDF
        assessment = self.assess_pdf(input_data.pdf_path)

        # Step 2: Extract using appropriate method
        if assessment['requires_ocr']:
            result = self.extract_with_ocr(
                input_data.pdf_path,
                input_data.start_page,
                input_data.end_page,
                output_file
            )
            method = 'ocr'
        else:
            result = self.extract_text_only(
                input_data.pdf_path,
                input_data.start_page,
                input_data.end_page,
                output_file
            )
            method = 'text'

        # Step 3: Return results
        return ExtractOutput(
            success=result['success'],
            output_file=output_file,
            extraction_method=method,
            pages_extracted=input_data.end_page - input_data.start_page + 1,
            error=result.get('error')
        )


# Convenience function
def extract_pdf(
    pdf_path: str,
    start_page: int,
    end_page: int,
    output_file: Optional[str] = None,
    config: Optional[ExtractConfig] = None
) -> ExtractOutput:
    """
    Convenience function to extract text from PDF.

    Example:
        result = extract_pdf('document.pdf', 1, 20, '/tmp/output.txt')
        if result.success:
            print(f'Extracted to {result.output_file}')
    """
    workflow = ExtractWorkflow(config)
    return workflow.run(ExtractInput(
        pdf_path=pdf_path,
        start_page=start_page,
        end_page=end_page,
        output_file=output_file
    ))
