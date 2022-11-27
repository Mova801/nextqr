from dataclasses import dataclass


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
class TextBox:
    width: int
    height: int


@dataclass
class ImageFrame:
    width: int
    height: int


@dataclass
class LeftFrame:
    scale_factor: int
    inner_padx: int
    sticky: str


@dataclass
class RightFrame:
    scale_factor: int
    inner_padx: int
    padding: int
    corner_radius: int
    sticky: str


@dataclass
class Layout:
    button: Button
    entry: Entry
    textbox: TextBox
    image_frame: ImageFrame
    left_frame: LeftFrame
    right_frame: RightFrame
