"""
Transcriber Agent - Main agent definition.

This agent handles PDF transcription and verification using OCR,
with Gemini for intelligent text processing.
"""

import logging
from pathlib import Path
from dataclasses import dataclass
from typing import Optional

try:
    from google.adk import Agent, LlmAgent
    from google.adk.models import GeminiModel
    ADK_AVAILABLE = True
except ImportError:
    ADK_AVAILABLE = False
    Agent = None
    LlmAgent = None
    GeminiModel = None

from .tools import (
    assess_pdf_tool,
    find_chapters_tool,
    extract_pages_tool,
    compare_texts_tool,
)
from .workflows import ExtractWorkflow, VerifyWorkflow, TranscribeWorkflow

logger = logging.getLogger(__name__)


TRANSCRIBER_SYSTEM_PROMPT = """You are the Transcriber Agent, specialized in PDF transcription and verification.

## Your Capabilities

1. **Assess PDFs** - Determine if a PDF requires OCR or has embedded text
2. **Find Chapters** - Scan PDFs for chapter/section boundaries
3. **Extract Text** - Extract text from PDF pages using OCR or text extraction
4. **Verify Transcriptions** - Compare markdown transcriptions against PDF sources
5. **Identify Errors** - Find discrepancies between transcriptions and sources

## Common OCR Errors to Watch For

### Numeric Errors (Highest Priority)
- 5 misread as 9 (e.g., 542 → 942)
- 1 misread as 7 (e.g., 1.9 → 7.9)
- Missing decimal points
- Comma/period confusion

### Character Errors
- l/1/I confusion
- 0/O confusion
- rn read as m
- Hyphenation artifacts

### Table Issues
- Column misalignment
- Missing cell values
- Merged cells not recognized

## Response Guidelines

- Always verify numeric data first - it has the highest error rate
- Provide confidence levels for discrepancy findings
- Suggest specific corrections with line numbers
- Note when visual inspection of the original PDF is needed

## Output Format

When reporting discrepancies:
1. Line number in markdown
2. Current text in markdown
3. Text found in OCR/PDF
4. Recommended action (fix, verify, keep)
5. Confidence level (HIGH, MEDIUM, LOW)
"""


@dataclass
class TranscriberConfig:
    """Configuration for the Transcriber Agent."""
    model_name: str = 'gemini-3-flash-preview'
    temperature: float = 0.2
    max_tokens: int = 4096
    scripts_dir: str = str(Path(__file__).parent.parent / 'scripts')


class TranscriberAgent:
    """
    Transcriber Agent for PDF transcription and verification.

    This agent combines OCR capabilities with LLM intelligence
    for accurate transcription verification.
    """

    def __init__(self, config: Optional[TranscriberConfig] = None):
        """Initialize the Transcriber Agent."""
        self.config = config or TranscriberConfig()
        self._agent = None
        self._initialized = False

        # Initialize workflows
        self.extract_workflow = ExtractWorkflow()
        self.verify_workflow = VerifyWorkflow()
        self.transcribe_workflow = TranscribeWorkflow()

    def _initialize(self):
        """Lazy initialization of the ADK agent."""
        if self._initialized:
            return

        if not ADK_AVAILABLE:
            logger.warning('Google ADK not available, agent will use direct workflow execution')
            self._initialized = True
            return

        try:
            model = GeminiModel(
                model_name=self.config.model_name,
                temperature=self.config.temperature,
                max_output_tokens=self.config.max_tokens,
            )

            self._agent = LlmAgent(
                name='transcriber',
                model=model,
                system_prompt=TRANSCRIBER_SYSTEM_PROMPT,
                tools=[
                    assess_pdf_tool,
                    find_chapters_tool,
                    extract_pages_tool,
                    compare_texts_tool,
                ],
            )

            self._initialized = True
            logger.info('Transcriber Agent initialized successfully')

        except Exception as e:
            logger.error(f'Failed to initialize Transcriber Agent: {e}')
            self._initialized = True

    async def assess_pdf(self, pdf_path: str) -> dict:
        """
        Assess a PDF to determine extraction method.

        Args:
            pdf_path: Path to PDF file

        Returns:
            Assessment with recommendation
        """
        self._initialize()
        return self.extract_workflow.assess_pdf(pdf_path)

    async def find_chapters(self, pdf_path: str, chapter_num: Optional[int] = None) -> dict:
        """
        Find chapter boundaries in a PDF.

        Args:
            pdf_path: Path to PDF file
            chapter_num: Optional specific chapter to find

        Returns:
            Chapter boundaries
        """
        self._initialize()

        import subprocess
        script = Path(self.config.scripts_dir) / 'find_chapter.py'

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
            'output': result.stdout,
            'error': result.stderr if result.returncode != 0 else None
        }

    async def extract(
        self,
        pdf_path: str,
        start_page: int,
        end_page: int,
        output_file: Optional[str] = None
    ) -> dict:
        """
        Extract text from PDF pages.

        Args:
            pdf_path: Path to PDF file
            start_page: First page (1-indexed)
            end_page: Last page (1-indexed)
            output_file: Optional output path

        Returns:
            Extraction result
        """
        self._initialize()

        from .workflows.extract_workflow import ExtractInput
        result = self.extract_workflow.run(ExtractInput(
            pdf_path=pdf_path,
            start_page=start_page,
            end_page=end_page,
            output_file=output_file
        ))

        return {
            'success': result.success,
            'output_file': result.output_file,
            'method': result.extraction_method,
            'pages': result.pages_extracted,
            'error': result.error
        }

    async def verify(
        self,
        pdf_path: str,
        markdown_path: str,
        start_page: int,
        end_page: int
    ) -> dict:
        """
        Verify a markdown transcription against PDF source.

        Args:
            pdf_path: Path to source PDF
            markdown_path: Path to markdown transcription
            start_page: First page in PDF
            end_page: Last page in PDF

        Returns:
            Verification report with discrepancies
        """
        self._initialize()

        from .workflows.verify_workflow import VerifyInput
        result = self.verify_workflow.run(VerifyInput(
            pdf_path=pdf_path,
            markdown_path=markdown_path,
            start_page=start_page,
            end_page=end_page
        ))

        return {
            'success': result.success,
            'total_discrepancies': result.total_discrepancies,
            'by_type': result.by_type,
            'discrepancies': [
                {
                    'line': d.line_number,
                    'type': d.discrepancy_type.value,
                    'markdown': d.markdown_text,
                    'ocr': d.ocr_text,
                    'action': d.action,
                    'confidence': d.confidence
                }
                for d in result.discrepancies
            ],
            'ocr_file': result.ocr_file,
            'error': result.error
        }

    async def transcribe(
        self,
        pdf_path: str,
        start_page: int,
        end_page: int,
        output_path: str,
        title: Optional[str] = None
    ) -> dict:
        """
        Transcribe PDF pages to markdown.

        Args:
            pdf_path: Path to PDF file
            start_page: First page (1-indexed)
            end_page: Last page (1-indexed)
            output_path: Path for output markdown
            title: Optional document title

        Returns:
            Transcription result
        """
        self._initialize()

        from .workflows.transcribe_workflow import TranscribeInput
        result = self.transcribe_workflow.run(TranscribeInput(
            pdf_path=pdf_path,
            start_page=start_page,
            end_page=end_page,
            output_path=output_path,
            title=title
        ))

        return {
            'success': result.success,
            'output_path': result.output_path,
            'word_count': result.word_count,
            'page_count': result.page_count,
            'error': result.error
        }


# Singleton instance
_agent_instance: Optional[TranscriberAgent] = None


def get_transcriber_agent() -> TranscriberAgent:
    """Get the singleton Transcriber Agent instance."""
    global _agent_instance
    if _agent_instance is None:
        _agent_instance = TranscriberAgent()
    return _agent_instance
