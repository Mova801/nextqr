from dataclasses import dataclass

from new.conf.layout_config import Layout
from new.conf.image_config import Image


@dataclass
class App:
    build: str
    name: str
    version: str
    auto_build: bool
    update_time_ms: int


@dataclass
class Screen:
    size: str
    resizable_width: bool
    resizable_height: bool
    appearance_mode: str
    color_theme: str


@dataclass
class Font:
    size_S: int
    size_M: int
    title_size_M: int
    title_size_L: int
    roboto: str


@dataclass
class Path:
    icons: str


@dataclass
class Link:
    github: str


@dataclass
class NextQrConfig:
    app: App
    screen: Screen
    font: Font
    path: Path
    link: Link
    layout: Layout
    image: Image
