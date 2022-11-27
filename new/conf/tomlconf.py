import tomllib
from typing import Any
from enum import StrEnum, auto

from new.conf import config
import new.conf.image_config as ic
import new.conf.layout_config as lc


class ConfigElements(StrEnum):
    APP = auto()
    SCREEN = auto()
    FONT = auto()
    PATH = auto()
    LINK = auto()
    IMAGE = auto()
    LAYOUT = auto()


def _toml_to_nextqrconfig(tomlconf: dict[str, Any]) -> config.NextQrConfig:
    """
    Converts a TOML configuration to a NextQrConfig configuration.
    :param tomlconf: TOML configuration to convert
    :return: NextQrConfig configuration
    """
    app = tomlconf[ConfigElements.APP.value]
    screen = tomlconf[ConfigElements.SCREEN.value]
    font = tomlconf[ConfigElements.FONT.value]
    path = tomlconf[ConfigElements.PATH.value]
    link = tomlconf[ConfigElements.LINK.value]
    image = tomlconf[ConfigElements.IMAGE.value]
    layout = tomlconf[ConfigElements.LAYOUT.value]

    nqc = config.NextQrConfig(
        app=config.App(
            build=app["build"],
            name=app["name"],
            version=app["version"],
            auto_build=app["auto_build"]
        ),
        screen=config.Screen(
            size=screen["size"],
            resizable_width=screen["resizable_width"],
            resizable_height=screen["resizable_height"],
            appearance_mode=screen["appearance_mode"],
            color_theme=screen["color_theme"]
        ),
        font=config.Font(
            size_S=font["size_S"],
            size_M=font["size_M"],
            title_size_M=font["title_size_M"],
            title_size_L=font["title_size_L"],
            roboto=font["roboto"]
        ),
        path=config.Path(icons=path["icons"]),
        link=config.Link(github=link["github"]),
        layout=config.Layout(
            button=lc.Button(
                width=layout["button"]["width"],
                height=layout["button"]["height"],
                img_position=layout["button"]["img_position"]
            ),
            entry=lc.Entry(
                width=layout["entry"]["width"],
                height=layout["entry"]["height"]
            ),
            textbox=lc.TextBox(
                width=layout["textbox"]["width"],
                height=layout["textbox"]["height"]
            ),
            image_frame=lc.ImageFrame(
                width=layout["image_frame"]["width"],
                height=layout["image_frame"]["height"]
            ),
            left_frame=lc.LeftFrame(
                scale_factor=layout["left_frame"]["scale_factor"],
                inner_padx=layout["left_frame"]["inner_padx"],
                sticky=layout["left_frame"]["sticky"]
            ),
            right_frame=lc.RightFrame(
                scale_factor=layout["right_frame"]["scale_factor"],
                padding=layout["right_frame"]["padding"],
                corner_radius=layout["right_frame"]["corner_radius"],
                inner_padx=layout["right_frame"]["inner_padx"],
                sticky=layout["right_frame"]["sticky"]
            )
        ),
        image=config.Image(
            logo=ic.Logo(path=image["logo"]["path"]),
            github=ic.Github(size=image["github"]["size"], path=image["github"]["path"]),
            bug=ic.Bug(size=image["bug"]["size"], path=image["bug"]["path"])
        )
    )
    return nqc


def load_configuration(filename: str, path: str = "") -> dict[str, Any]:
    """
    Loads a TOML configuration from a file.
    :param filename: configuration file name
    :param path: path to the conf file
    :return: TOML configuration
    """
    if path != "":
        path = path + "\\"
    fto: str = f"{path}{filename}.toml"
    with open(fto, "rb") as f:
        data = tomllib.load(f)
    return data


def load_nextqr_configuration(filename: str, path: str = "") -> config.NextQrConfig:
    """
    Loads a config file and returns it as a NextQrConfig.
    :param filename: configuration file name
    :param path: path to the conf file
    :return: NextQrConfig configuration
    """
    toml_conf = load_configuration(filename, path)
    return _toml_to_nextqrconfig(toml_conf)
