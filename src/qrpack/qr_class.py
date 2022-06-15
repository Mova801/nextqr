import os
import time
from PIL import Image
from dataclasses import dataclass

import qrcode


def ExceptionHandler(func):
    def wrapper(*args, **kwargs):
        qr = args[0]
        try:
            message = None
            func(args, kwargs)
        except FileNotFoundError as error:
            message = error

        if qr._ExceptionHandler and message is not None:
            print(error)
        return qr
    return wrapper


@dataclass
class QR:
    _image: bytes
    _debug: bool

    def __init__(self, debug=False) -> None:
        self._debug = debug

    # aggiunge il logo passato al QR
    @ExceptionHandler
    def add_logo(self, logo: str, dim: int):
        logo_display = Image.open(logo)
        logo_display.thumbnail((dim, dim))
        logo_pos = ((self._image.size[0] - logo_display.size[0]) // 2,
                    (self._image.size[1] - logo_display.size[1]) // 2)
        self._image.paste(logo_display, logo_pos)
        return self

    # aggiunge i dati passati al QR
    @ExceptionHandler
    def add_data(self, data: str, fill_col: tuple, back_col: tuple = None):
        if back_col is None:
            back_col = fill_col
        # creates a qr code obj
        qr = qrcode.QRCode(version=1,
                           error_correction=qrcode.constants.ERROR_CORRECT_L,
                           box_size=20,
                           border=2)
        qr.add_data(data)
        qr.make(fit=True)
        self._image = qr.make_image(
            fill_color=fill_col.rgb(), back_color=back_col.rgb())
        return self

    # generates a QR from the user input
    @ExceptionHandler
    def generate(self, name: str, path: str):
        if not name:
            name = f"next_qr_{time.strftime('%H%M%S')}.png"
        name = os.path.join(path, name)
        self._image.save(name)
        return self
