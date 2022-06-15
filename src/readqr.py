import time

from ios.iostream import IOstream
from messagehandler.message_handler import MessageHandler
from keyboardhandler.keyboard_handler import KeyboardHandler


msg = MessageHandler(debug=True, _input="messagehandler.messages")
key = KeyboardHandler('c', 'f', '-', 'esc')


def camera_main() -> None:
    dec.pretty("QREAD_DETECTING", color="yellow", clear=True)
    dec.pretty(" ► press '[-]' to interrupt the scan... ",
               color="magenta", mymsg=True)

    if img.find_qr_in_camera(showCamera=config.get_camera()) is None:
        dec.pretty("QREAD_ERR_DATA", color="red", clear=True)
        return

    dec.pretty("QREAD_START", color="cyan", clear=True)
    data = img.get_data()
    dec.pretty("QREAD_DATA_QR", add=data)

    if data == "" or data is None:
        dec.pretty("QREAD_ERR_QR", color="red", clear=True)
        return

    user_input = dec.pretty("QREAD_SAVE_DATA", input=True)
    match user_input:
        case 'Y':
            file = File(
                f"nextqr_reading_{time.strftime('%d%m%Y')}_{time.strftime('%H%M%S')}.txt", data, config.get_out_dir(), "a")
            file << ""
    uti.link_menu(data)
    io.clear_terminal()


def read_qr_from_file() -> None:
    msg.colprint("QREAD_START", "cyan", clear=True)
    filename = msg.iprint("QREAD_ENTER_QR") + ".png"
    path = IOstream.join_path(config.get_input_dir(), filename)

    if img.open_image(path) is None:
        dec.pretty("QREAD_ERR_FILE", color="red", clear=True)
        return

    if img.find_qr() is None:
        dec.pretty("QREAD_ERR_QR", color="red", clear=True)
        return

    img.display()
    data = img.get_data()
    dec.pretty("QREAD_DATA_QR", add=data)

    user_input = dec.pretty("QREAD_SAVE_DATA", input=True)
    match user_input:
        case 'Y':
            file = File(
                f"nextqr_reading_{time.strftime('%d%m%Y')}_{time.strftime('%H%M%S')}.txt", data=data, path=config.get_out_dir(), mode="a")
            io << file
    uti.link_menu(data)
    io.clear_terminal()


def read_qr() -> None:
    key.listen()
    while True:
        msg.iprint("QREAD_MENU", clear=True)
        match key.get_input():
            case 'c':
                camera_main()
                continue

            case 'f':
                file_main()
                continue

            case '-':
                break

            case _:
                msg.colprint("ERR_INV_INPUT", "red", clear=True)


if __name__ == "__main__":
    read_qr()
