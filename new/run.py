"""
Created by Marco Vita (aka Mova801) on 16/09/2022
Module that runs NextQR app.
"""
import hydra
from hydra.core.config_store import ConfigStore
from hydra import MissingConfigException

from app.app import App
from conf.config import NextQrConfig

CONFIG_PATH: str = "conf"
CONFIG_FILE: str = "conf.yaml"

cf = ConfigStore.instance()
cf.store(name="nextqr_config", node=NextQrConfig)


@hydra.main(config_path=CONFIG_PATH, config_name=CONFIG_FILE, version_base="1.2")
def main(config) -> None:
    """Creates and runs a new app."""
    app = App(config)
    app.build()
    app.run()


if __name__ == '__main__':
    try:
        main()
    except MissingConfigException as e:
        print(e)
