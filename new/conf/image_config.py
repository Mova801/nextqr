from dataclasses import dataclass
import inspect
from enum import Enum
from typing import Any


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
    image_members: dict[str, Any] = image.__dict__
    return [{"size": img.size, "path": img.path} for img in image_members.values() if not isinstance(img, Logo)]
