# imports
from colorama import init

from genqr import generate_qr
from readqr import read_qr
from keyboardhandler.keyboard_handler import KeyboardHandler
from messagehandler.message_handler import MessageHandler
from ios.iostream import IOstream, Configuration, DESKTOP


def main() -> None:
    config = Configuration()
    config.load("src\\nextqr.ini")
    if config['APP'].get("launches", False) == 0:
        config['APP']['output_directory'] = config['APP']['output_directory'] = DESKTOP
        config.save()

    IOstream.update_terminal()
    init()
    msg = MessageHandler(debug=True, _import="messagehandler.messages")
    msg.colprint("APP_INFO", "cyan", clear=True)
    msg.colprint("APP_DEV", "cyan", clear=True)
    msg.colprint("APP_START", "cyan", clear=True, input=True, )

    key = KeyboardHandler('-','+','#','*','o')
    key.listen()
    while True:
        msg.iprint("APP_MENU")
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
                settings()
                continue

            case 'o':
                IOstream.open_link('https://github.com/Mova801')
                IOstream.clear_terminal()
                continue

            case _:
                msg.colprint("ERR_INV_INPUT", "red", clear=True)


if __name__ == '__main__':
    main()
