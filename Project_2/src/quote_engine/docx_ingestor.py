"""Docx ingestor."""

from docx import Document
from typing import List
from quote_engine.ingestor_interface import IngestorInterface
from quote_engine.quote_model import QuoteModel


class DocxIngestor(IngestorInterface):
    """Parse docx defination."""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Docx parse."""
        reader = Document(path)

        quotes = []
        for row in reader.paragraphs:
            # Check quotes or not
            if ' - ' in row.text:
                quotes.append(QuoteModel(*row.text.split(' - ')))

        return quotes
