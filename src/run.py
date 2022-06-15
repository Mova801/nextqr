# imports
from colorama import init

from genqr import generate_qr
from readqr import read_qr
from settings import app_settings
from keyboardhandler.keyboard_handler import KeyboardHandler
from messagehandler.message_handler import MessageHandler
from ios.iostream import IOstream, Configuration, DESKTOP
from src.constants import CONF_LOCATION, GITHUB_DEV_LINK, MAIN_KEYS, MESSAGES_PATH

def main() -> None:
    config = Configuration()
    config.load(CONF_LOCATION)
    launches = int(config["APP"].get("launches"))
    if launches == 0:
        config["APP"]['output_directory'] = config["APP"]['output_directory'] = "qrs"
    config['APP']['launches'] = launches + 1
    config.save()

    name, width, height = config['CONSOLE'].values()

    IOstream.update_terminal(name=name, width=int(width), height=int(height))
    init()
    key = KeyboardHandler(MAIN_KEYS)
    key.listen()
    msg = MessageHandler(_import=MESSAGES_PATH)
    msg.colprint("APP_INFO", "cyan", clear=True)
    msg.colprint("APP_DEV", "cyan")
    msg.colprint("APP_START", "cyan")
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
                continue

            case '#':
                read_qr()
                continue

            case '*':
                app_settings()
                continue

            case 'o':
                IOstream.open_link(GITHUB_DEV_LINK)
                IOstream.clear_terminal()
                continue


if __name__ == '__main__':
    main()
