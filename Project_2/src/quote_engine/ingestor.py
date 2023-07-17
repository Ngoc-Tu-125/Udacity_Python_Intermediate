"""Ingestor."""

from typing import List
import os

from quote_engine.quote_model import QuoteModel
from quote_engine.ingestor_interface import IngestorInterface
from quote_engine.txt_ingestor import TxtIngestor
from quote_engine.docx_ingestor import DocxIngestor
from quote_engine.csv_ingestor import CsvIngestor
from quote_engine.pdf_ingestor import PdfIngestor


class Ingestor(IngestorInterface):
    """Ingestor defination."""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse."""
        ingestor_mapping = {
            '.txt': TxtIngestor,
            '.csv': CsvIngestor,
            '.docx': DocxIngestor,
            '.pdf': PdfIngestor
        }

        file_extension = os.path.splitext(path)[1].lower()

        if cls.can_ingest(path):
            ingestor_class = ingestor_mapping[file_extension]
            return ingestor_class.parse(path)
