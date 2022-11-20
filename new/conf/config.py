from dataclasses import dataclass


@dataclass
class App:
    build: str
    name: str
    version: str
    auto_build: bool


@dataclass
class Screen:
    size: str
    resizable_width: bool
    resizable_height: bool
    appearance_mode: str
    color_theme: str


@dataclass
class Font:
    size: int
    roboto: str


@dataclass
class Path:
    icons: str


@dataclass
class Image:
    logo: str


@dataclass
class Link:
    github: str


@dataclass
class Button:
    width: int
    height: int
    img_position: str


@dataclass
class Layout:
    button: Button


@dataclass
class NextQrConfig:
    app: App
    screen: Screen
    font: Font
    path: Path
    image: Image
    link: Link
    layout: Layout
