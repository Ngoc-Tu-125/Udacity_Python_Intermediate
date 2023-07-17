"""Txt ingestor."""

from typing import List
from quote_engine.ingestor_interface import IngestorInterface
from quote_engine.quote_model import QuoteModel


class TxtIngestor(IngestorInterface):
    """Parse docx defination."""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Txt parse."""
        quotes = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                if ' - ' in line:
                    quotes.append(QuoteModel(*line.split(' - ')))

        return quotes
