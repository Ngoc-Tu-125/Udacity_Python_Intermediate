"""Ingestor Interface."""

from abc import ABC
from tkinter import BooleanVar
from typing import List
from quote_engine.quote_model import QuoteModel


class IngestorInterface(ABC):
    """Ingestor Interface Abstract class."""

    @classmethod
    def can_ingest(cls, path: str) -> BooleanVar:
        """Can ingest defination."""
        supported_extensions = ['.csv', '.docx', '.pdf', '.txt']
        if any(path.endswith(ext) for ext in supported_extensions):
            return True
        else:
            return False

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse defination."""
