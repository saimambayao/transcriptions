"""
Verify Workflow - Compare OCR output against markdown transcription.

This workflow compares extracted PDF text against existing markdown
to identify discrepancies for correction.
"""

import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum

from .extract_workflow import ExtractWorkflow, ExtractConfig, ExtractInput


class DiscrepancyType(Enum):
    """Types of discrepancies found during verification."""
    NUMERIC = 'numeric'
    TEXT = 'text'
    MISSING_CONTENT = 'missing'
    TABLE = 'table'
    CITATION = 'citation'
    FORMATTING = 'formatting'


@dataclass
class Discrepancy:
    """A single discrepancy between OCR and markdown."""
    line_number: int
    discrepancy_type: DiscrepancyType
    markdown_text: str
    ocr_text: str
    action: str  # 'fix', 'verify', 'keep'
    confidence: float = 0.0  # 0.0 to 1.0


@dataclass
class VerifyInput:
    """Input for verify workflow."""
    pdf_path: str
    markdown_path: str
    start_page: int
    end_page: int


@dataclass
class VerifyOutput:
    """Output from verify workflow."""
    success: bool
    discrepancies: list[Discrepancy] = field(default_factory=list)
    total_discrepancies: int = 0
    by_type: dict = field(default_factory=dict)
    ocr_file: str = ''
    error: Optional[str] = None


class VerifyWorkflow:
    """
    Workflow for verifying markdown transcriptions against PDF source.

    Steps:
    1. Extract OCR text from PDF
    2. Read existing markdown
    3. Compare section by section
    4. Document discrepancies
    5. Return verification report
    """

    def __init__(self, extract_config: Optional[ExtractConfig] = None):
        self.extract_workflow = ExtractWorkflow(extract_config)

    def read_file(self, path: str) -> str:
        """Read file contents."""
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    def normalize_text(self, text: str) -> str:
        """Normalize text for comparison."""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Normalize quotes
        text = text.replace('"', '"').replace('"', '"')
        text = text.replace(''', "'").replace(''', "'")
        # Normalize dashes
        text = text.replace('—', '-').replace('–', '-')
        return text.strip().lower()

    def find_numeric_discrepancies(
        self,
        ocr_text: str,
        markdown_text: str
    ) -> list[Discrepancy]:
        """Find numeric discrepancies between texts."""
        discrepancies = []

        # Extract numbers from both texts
        ocr_numbers = re.findall(r'\b\d+(?:,\d{3})*(?:\.\d+)?\b', ocr_text)
        md_numbers = re.findall(r'\b\d+(?:,\d{3})*(?:\.\d+)?\b', markdown_text)

        # Simple comparison - find numbers in markdown not in OCR
        ocr_set = set(ocr_numbers)
        md_set = set(md_numbers)

        # Numbers only in markdown (potential errors)
        for num in md_set - ocr_set:
            # Find line number
            for i, line in enumerate(markdown_text.split('\n'), 1):
                if num in line:
                    discrepancies.append(Discrepancy(
                        line_number=i,
                        discrepancy_type=DiscrepancyType.NUMERIC,
                        markdown_text=num,
                        ocr_text='[not found in OCR]',
                        action='verify',
                        confidence=0.5
                    ))
                    break

        return discrepancies

    def compare_texts(
        self,
        ocr_text: str,
        markdown_text: str
    ) -> list[Discrepancy]:
        """
        Compare OCR and markdown texts to find discrepancies.

        This is a simplified comparison. A full implementation would use
        more sophisticated text alignment algorithms.
        """
        discrepancies = []

        # Find numeric discrepancies (highest priority)
        discrepancies.extend(
            self.find_numeric_discrepancies(ocr_text, markdown_text)
        )

        # Normalize both texts
        ocr_normalized = self.normalize_text(ocr_text)
        md_normalized = self.normalize_text(markdown_text)

        # Find words in markdown but not in OCR (potential additions)
        ocr_words = set(ocr_normalized.split())
        md_words = set(md_normalized.split())

        # Words only in markdown (might be errors or additions)
        suspicious_words = md_words - ocr_words

        # Filter to significant words (length > 5, not common)
        common_words = {'the', 'and', 'for', 'with', 'that', 'this', 'from', 'have', 'which'}
        suspicious_words = {w for w in suspicious_words if len(w) > 5 and w not in common_words}

        # Limit to top 10 most suspicious
        for word in list(suspicious_words)[:10]:
            for i, line in enumerate(markdown_text.split('\n'), 1):
                if word in line.lower():
                    discrepancies.append(Discrepancy(
                        line_number=i,
                        discrepancy_type=DiscrepancyType.TEXT,
                        markdown_text=word,
                        ocr_text='[not found in OCR]',
                        action='verify',
                        confidence=0.3
                    ))
                    break

        return discrepancies

    def run(self, input_data: VerifyInput) -> VerifyOutput:
        """
        Execute the verify workflow.

        Args:
            input_data: VerifyInput with paths and page range

        Returns:
            VerifyOutput with discrepancy report
        """
        try:
            # Step 1: Extract OCR text
            extract_result = self.extract_workflow.run(ExtractInput(
                pdf_path=input_data.pdf_path,
                start_page=input_data.start_page,
                end_page=input_data.end_page,
                output_file='/tmp/verify_ocr.txt'
            ))

            if not extract_result.success:
                return VerifyOutput(
                    success=False,
                    error=f'OCR extraction failed: {extract_result.error}'
                )

            # Step 2: Read both files
            ocr_text = self.read_file(extract_result.output_file)
            markdown_text = self.read_file(input_data.markdown_path)

            # Step 3: Compare texts
            discrepancies = self.compare_texts(ocr_text, markdown_text)

            # Step 4: Categorize discrepancies
            by_type = {}
            for d in discrepancies:
                type_name = d.discrepancy_type.value
                by_type[type_name] = by_type.get(type_name, 0) + 1

            # Step 5: Return results
            return VerifyOutput(
                success=True,
                discrepancies=discrepancies,
                total_discrepancies=len(discrepancies),
                by_type=by_type,
                ocr_file=extract_result.output_file
            )

        except Exception as e:
            return VerifyOutput(
                success=False,
                error=str(e)
            )


# Convenience function
def verify_transcription(
    pdf_path: str,
    markdown_path: str,
    start_page: int,
    end_page: int
) -> VerifyOutput:
    """
    Convenience function to verify a transcription.

    Example:
        result = verify_transcription(
            'document.pdf',
            'transcription.md',
            1, 20
        )
        for d in result.discrepancies:
            print(f'Line {d.line_number}: {d.markdown_text} vs {d.ocr_text}')
    """
    workflow = VerifyWorkflow()
    return workflow.run(VerifyInput(
        pdf_path=pdf_path,
        markdown_path=markdown_path,
        start_page=start_page,
        end_page=end_page
    ))
