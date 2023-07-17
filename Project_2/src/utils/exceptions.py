"""Exceptions."""


class ImagePathError(Exception):
    """Command Error Defination."""

    def __init__(self, msg) -> None:
        """Init exception."""
        super().__init__(msg)


class SizeImageError(Exception):
    """Command Error Defination."""

    def __init__(self, msg) -> None:
        """Init exception."""
        super().__init__(msg)
