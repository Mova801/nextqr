"""
Created by Marco Vita (aka Mova801) on 16/09/2022
Module that runs NextQR app.
"""

from app.app import App
from new.conf.tomlconf import load_nextqr_configuration

CONFIG_PATH: str = "conf"
CONFIG_FILE: str = "conf"


def main() -> None:
    """Creates and runs a new app."""
    config = load_nextqr_configuration(filename=CONFIG_FILE, path=CONFIG_PATH)
    app = App(config)
    app.build()
    app.run()


if __name__ == '__main__':
    main()
