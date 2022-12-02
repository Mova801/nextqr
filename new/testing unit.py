import re

from new.libs.color import Color


def main() -> None:
    print("testing unit")
    print("testing color class exceptions")
    value = "#E0EE"
    print(f"Color value: {value}")
    col = Color(value)
    print(f"Color RGB value: {col.rbg}")
    print(f"Color HEX value: {col.hex}")


if __name__ == "__main__":
    main()
