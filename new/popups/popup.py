from abc import ABC, abstractmethod


class Popup(ABC):

    @abstractmethod
    def show(self) -> None:
        ...
