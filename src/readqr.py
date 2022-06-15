from imagestream.imagestream import ImageStream
from ios.iostream import IOstream, Configuration, File
from messagehandler.message_handler import MessageHandler
from keyboardhandler.keyboard_handler import KeyboardHandler
from src.constants import CONF_LOCATION, MAIN_READQR_KEYS, MESSAGES_PATH, SCAN_WINDOW_NAME

from validators import url


msg = MessageHandler(debug=True, _import=MESSAGES_PATH)
key = KeyboardHandler(MAIN_READQR_KEYS)


# data una stringa identifica se è un link o meno, in caso l'utente inserisca 't' in input il link varrà aperto
def check_if_link(string: str):
    if not url(string):
        return

    user_input = msg.clsprint("QREAD_IS_LINK", input=True)
    key.unpause()
    while True:
        match user_input:
            case 'Y':
                IOstream.open_link(string)
                break
    key.pause()


def save_data_found(data: str, out_dir: str):
    key.unpause()
    while True:
        match key.get_input():
            case 'Y':
                IOstream.mkdirs(out_dir)
                file = File(
                    f"nextqr{IOstream.get_date()}_{IOstream.get_time()}.qrs", data=data, path=out_dir, mode="a")
                file.write()
                break
    key.pause()
    IOstream.check_if_link(data)


def camera_main() -> None:
    msg.clsprint("QREAD_DETECTING", color="yellow")
    msg.myprint(" ► press '[-]' to interrupt the scan... ", color="magenta")
    config = Configuration()
    config.load(CONF_LOCATION)
    out_dir = (config['APP'].get("output_directory"))
    show_camera = bool(config['CAMERA'].get("show_camera"))
    img = ImageStream()
    data = img.search_qr_in_camera(show_camera, SCAN_WINDOW_NAME)
    msg.clsprint("QREAD_START", color="cyan")
    msg.print("QREAD_DATA_QR", add=data)

    if not data or data is None:
        msg.clsprint("QREAD_ERR_QR", color="red")
        return
    msg.print("QREAD_SAVE_DATA")
    save_data_found(data, out_dir)
    IOstream.check_if_link(data)
    IOstream.clear_terminal()


def read_qr_from_file() -> None:
    msg.colprint("QREAD_START", "cyan", clear=True)
    filename = msg.iprint("QREAD_ENTER_QR") + ".png"
    config = Configuration()
    config.load(CONF_LOCATION)
    in_dir = (config['APP'].get("input_directory"))
    out_dir = (config['APP'].get("output_directory"))
    filename = IOstream.join_path(in_dir, filename)
    img = ImageStream()
    if not img.open_image(filename):
        msg.clsprint("QREAD_ERR_FILE", color="red")
        return
    data = img.search_qr()
    if not data:
        msg.clsprint("QREAD_ERR_QR", color="red")
        return
    img.display()
    msg.print("QREAD_DATA_QR", add=data)
    msg.print("QREAD_SAVE_DATA")
    save_data_found(data, out_dir)
    IOstream.check_if_link(data)
    IOstream.clear_terminal()


def read_qr() -> None:
    key.listen()
    msg.print("QREAD_MENU", clear=True)
    while True:
        match key.get_input():
            case 'c':
                key.pause()
                key.press_key()
                camera_main()
                continue

            case 'f':
                key.pause()
                key.press_key()
                read_qr_from_file()
                continue

            case '-' | 'esc':
                break


if __name__ == "__main__":
    read_qr()
