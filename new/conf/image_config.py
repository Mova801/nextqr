from dataclasses import dataclass
import inspect
from enum import Enum


class AvailableImages(Enum):
    GITHUB = "github"
    BUG = "bug"


@dataclass
class Logo:
    path: str


@dataclass
class Github:
    size: int
    path: str


@dataclass
class Bug:
    size: int
    path: str


@dataclass
class Image:
    logo: Logo
    github: Github
    bug: Bug


def image_list_from_config(image: Image) -> list[dict[[str, int], [str, str]]]:
    image_members: list = inspect.getmembers(image)
    return [elem[1] for elem in image_members if elem[0] != "logo"]
