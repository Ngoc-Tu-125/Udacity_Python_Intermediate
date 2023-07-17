"""Qoute: quote - author."""


class QuoteModel:
    """Quote Model defination."""

    def __init__(self, body, author) -> None:
        """Init."""
        self.body = body
        self.author = author

    def __str__(self):
        """str."""
        return f"{self.body} - {self.author}"
