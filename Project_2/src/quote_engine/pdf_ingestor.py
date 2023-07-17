"""Pdf ingestor."""

from subprocess import Popen, PIPE
from typing import List
from quote_engine.ingestor_interface import IngestorInterface
from quote_engine.quote_model import QuoteModel


class PdfIngestor(IngestorInterface):
    """Parse docx defination."""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Pdf parse."""
        quotes = []

        # Read pdf from process command:
        with Popen(['pdftotext', path], stdout=PIPE, shell=True) as proc:
            proc_out = proc.communicate()[0]

            for line in proc_out:
                if ' - ' in line:
                    quotes.append(QuoteModel(*line.split(' - ')))

        return quotes
