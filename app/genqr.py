from email import message
from PIL import Image

from LIB.messagehandler.message_handler import MessageHandler
from LIB.ios.iostream import IOstream, Configuration, Log
from qrpack.qr_class import QR
from src.constants import CONF_LOCATION


def str_to_tuple(string: str) -> tuple[int, int, int]:
    if string.startswith("(") and string.endswith(")"):
        string = string.strip("()")
        string = string.split(",")
        return tuple((int(num) for num in string))


def apply_style(styles_path: str, style: str) -> tuple[tuple[int,int,int], tuple[int,int,int]]:
    styles_ini = Configuration()
    styles_ini.load(styles_path)
    fill_col = str_to_tuple(styles_ini[style].get("fill_color"))
    back_col = str_to_tuple(styles_ini[style].get("back_color"))
    return fill_col, back_col


def start_config():
    config = Configuration()
    config.load(CONF_LOCATION)
    style = config['APP'].get("style")
    styles_path = config['PATH'].get("styles_ini_path")
    if style and IOstream.is_file(styles_path):
        fill_col, back_col = apply_style(styles_path, style)
    else:
        fill_col = str_to_tuple(config['QR'].get("fill_color", "(0,0,0)"))
        back_col = str_to_tuple(config['QR'].get("back_color", "(0,0,0)"))
    log_dir = config['APP'].get("log_directory", "logs\\log")
    in_dir = config['APP'].get("input_directory", "")
    out_dir = config['APP'].get("output_directory", "")
    log = Log(f"log[{IOstream.get_time}]", path=f"{log_dir}{IOstream.get_date()}")
    messages_path = config['PATH'].get("messages_path")
    return config, log, fill_col, back_col, in_dir, out_dir, messages_path

def generate_qr() -> None:

    config, log, fill_col, back_col, in_dir, out_dir, messages_path = start_config()

    msg = MessageHandler(_import=messages_path)
    msg.clsprint("QGEN_START", color="cyan")
    qrname = IOstream.invalid_char(msg.iprint("QGEN_ENTER_NAME"))
    data = msg.iprint("QGEN_ENTER_DATA")
    new_qr = QR()

    try:
        new_qr.add_data(data, fill_col, back_col)
    except ValueError as error:
        log.log(error)
        msg.colprint("QGEN_ERR_QR", "red", clear=True)
        return

    logo = msg.iprint("QGEN_ENTER_LOGO", clear=True)
    if logo:
        logo = f"{logo}.png"
        try:
            logo = IOstream.join_path(in_dir, logo)
            Image.open(logo)

            new_qr.add_logo(logo, config['QR'].get("logo_dim", 60))
        except FileNotFoundError as error:
            log.log(error)
            msg.colprint("ERR_INV_LOGO", "red")

    try:
        new_qr.generate(qrname, out_dir)
    except PermissionError as error:
        log.log(error)
        msg.colprint("ERR_PERMISSION", "red")
    except AttributeError as error:
        log.log(error)
        msg.colprint("QGEN_ERR_QR", "red")
    else:
        msg.colprint("QGEN_NEW_QR", "cyan")


if __name__ == "__main__":
    generate_qr()
