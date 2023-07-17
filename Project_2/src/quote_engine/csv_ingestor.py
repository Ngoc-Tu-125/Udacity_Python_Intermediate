"""Csv ingestor."""

import csv
from typing import List
from quote_engine.ingestor_interface import IngestorInterface
from quote_engine.quote_model import QuoteModel


class CsvIngestor(IngestorInterface):
    """Parse docx defination."""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Csv parse."""
        with open(path, 'r') as file:
            # Create a csv object
            reader = csv.reader(file)

            quotes = []
            for row in reader:
                quotes.append(QuoteModel(row[0], row[1]))

        return quotes
