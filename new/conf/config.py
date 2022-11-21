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
    size: int
    logo: str
    github: str


@dataclass
class Link:
    github: str


@dataclass
class Button:
    width: int
    height: int
    img_position: str


@dataclass
class Entry:
    width: int
    height: int


@dataclass
class Layout:
    button: Button
    entry: Entry


@dataclass
class NextQrConfig:
    app: App
    screen: Screen
    font: Font
    path: Path
    image: Image
    link: Link
    layout: Layout
