# imports
from colorama import init
import sys

# tmp path
sys.path.append(
    "C:\\Users\\marco\\OneDrive\\Documenti\\GitHub")

from genqr import generate_qr
from readqr import read_qr
from settings import app_settings
from LIB.zkeyboardhandler.keyboard_handler import KeyboardHandler
from LIB.messagehandler.message_handler import MessageHandler
from LIB.ios.iostream import IOstream, Configuration
from src.constants import CONF_LOCATION, MAIN_KEYS


def pprint(*args, **kwargs):
    key.pause()
    input = msg.print(*args, **kwargs)
    key.unpause()
    key.reset_input()
    return input


def start_config():
    config = Configuration()
    config.load(CONF_LOCATION)
    launches = int(config['APP'].get("launches"))
    if launches == 0:
        config['APP']['output_directory'] = config["APP"]['output_directory'] = "qrs"
    config['APP']['launches'] = str(launches + 1)
    config.save()
    messages_path = config['PATH'].get("messages_path")
    github_link = config['DEV'].get("github_link")
    return config, messages_path, github_link


def main() -> None:
    global key, msg
    config, messages_path, github_link = start_config()

    name, width, height = config['CONSOLE'].values()

    IOstream.update_terminal(name=name, width=int(width), height=int(height))
    init()
    key = KeyboardHandler(MAIN_KEYS)
    key.listen()
    msg = MessageHandler(_import=messages_path)
    pprint("APP_INFO", color="cyan", clear=True)
    pprint("APP_DEV", color="cyan")
    pprint("APP_START", color="cyan")
    while True:
        match key.get_input():
            case 'e':
                break
            case '-' | 'esc':
                exit(0)

    msg.print("APP_MENU", clear=True)
    while True:

        match key.get_input():
            case '-':
                exit(0)

            case '+':
                generate_qr()
                pprint("APP_MENU", clear=True)
                continue

            case '#':
                read_qr()
                pprint("APP_MENU", clear=True)
                continue

            case '*':
                app_settings()
                pprint("APP_MENU", clear=True)
                continue

            case 'o':
                IOstream.open_link(github_link)
                continue


if __name__ == '__main__':
    main()
