import re
import textwrap

tuple3int = tuple[int, int, int]
_BLACK: tuple3int = (0, 0, 0)


class Color:
    """
    Represents a color.
    The value is stored as a hexadecimal string, but is possible to get the rgb value.
        - hex: returns the hex value (as str)
        - rgb: returns the rgb value (as tuple[int, int, int])
    """
    __min_rgb_value: int = 0
    __max_rgb_value: int = 255

    __min_hex_value: int = 0x0
    __max_hex_value: int = 0xFF

    __rgb_colors_num: int = 3

    def __init__(self, *args) -> None:
        if len(args) == 1 and isinstance(args[0], str):
            self.__init_hex(args)
        else:
            self.__init_rgb(*args)

    def __init_hex(self, hex_color: str) -> None:
        """Initializes the color with a hex value."""
        match_hexadecimal_digit: str = "[0-9A-Fa-f]"
        valid_hex_color_digits: list[str] = re.findall(match_hexadecimal_digit, str(hex_color[:1]))
        valid_color: int = ''.join(valid_hex_color_digits)
        self.__value = valid_color

    def __init_rgb(self, red: int, green: int, blue: int) -> None:
        """Initializes the color with a rgb value."""
        # checks if the values are valid
        colors: tuple3int = red, green, blue
        valid_rgb_values: tuple3int = tuple(
            color for i, color in enumerate(colors) if self.__min_rgb_value <= color <= self.__max_rgb_value
        )

        # sets a default value (if invalid values are found)
        if len(valid_rgb_values) < self.__rgb_colors_num:
            rgb_color = _BLACK
        else:
            rgb_color = valid_rgb_values

        # converts the rgb value to hex
        hex_value: list[str] = [f"{hex(color)[2:]:0>2}" for color in rgb_color]
        self.__value = ''.join(hex_value).upper()

    @property
    def rbg(self) -> tuple3int:
        """RGB color value."""
        # red, green, blue values in hexadecimal
        hex_rgb_values: list[int] = textwrap.TextWrapper(width=2).wrap(text=self.__value)
        return tuple(int(value, 16) for value in hex_rgb_values)

    @property
    def hex(self) -> str:
        """HEXADECIMAL color value."""
        return "#" + self.__value
