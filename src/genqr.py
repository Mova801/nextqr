from PIL import Image

from messagehandler.message_handler import MessageHandler
from ios.iostream import IOstream, Configuration, Log
from qrpack.qr_class import QR


def generate_qr() -> None:
    msg = MessageHandler(debug=True, _import="messagehandler.messages")
    msg.colprint("QGEN_START", "cyan", clear=True)

    qrname = IOstream.invalid_char(msg.iprint("QGEN_ENTER_NAME"))
    data = msg.iprint("QGEN_ENTER_DATA")

    config = Configuration()
    config.load("src\\nextqr.ini")
    fill_col = config['QR'].get("fill_color", (0, 0, 0))
    back_col = config['QR'].get("back_color", (0, 0, 0))
    dir1 = config['APP'].get("directory_1", "logs")
    dir2 = config['QR'].get("directory_2", "log")
    in_dir = config['APP'].get("input_directory", "")
    out_dir = config['APP'].get("output_directory", "")
    log = Log(f"log[{IOstream.get_time}]", dir1=dir1, dir2=dir2)

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
