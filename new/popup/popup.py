from abc import ABC, abstractmethod
from typing import Any

WIN_WIDTH: int = 450
WIN_HEIGHT: int = 200
TITLE_SIZE: str = 20
FONT: str = "Roboto Medium"
FONT_SIZE: str = 12


class Popup(ABC):
    """Generic Popup abstract class."""

    @abstractmethod
    def build(self) -> None:
        """Builds the popup layout."""

    @abstractmethod
    def show(self, msg: Any) -> None:
        """Shows the popup on screen."""

    @abstractmethod
    def close(self) -> None:
        """Closes the popup."""
