import os
import time
from PIL import Image
from dataclasses import dataclass

from LIB.exceptionpack.exception_handler import handle_exceptions
import qrcode


class MissingQRColorError(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class QR:
    _image: bytes
    _debug: bool

    def __init__(self, debug=False) -> None:
        self._debug = debug

    # aggiunge il logo passato al QR
    @handle_exceptions
    def add_logo(self, logo: str, dim: int):
        logo_display = Image.open(logo)
        logo_display.thumbnail((dim, dim))
        logo_pos = ((self._image.size[0] - logo_display.size[0]) // 2,
                    (self._image.size[1] - logo_display.size[1]) // 2)
        self._image.paste(logo_display, logo_pos)
        return self

    # aggiunge i dati passati al QR
    @handle_exceptions
    def add_data(self, data: str, fill_col: tuple = None, back_col: tuple = None):
        if back_col is None:
            raise MissingQRColorError
        # creates a qr code obj
        qr = qrcode.QRCode(version=1,
                           error_correction=qrcode.constants.ERROR_CORRECT_L,
                           box_size=20,
                           border=2)
        qr.add_data(data)
        qr.make(fit=True)
        self._image = qr.make_image(
            fill_color=fill_col, back_color=back_col)
        return self

    # generates a QR from the user input
    @handle_exceptions
    def generate(self, name: str, path: str):
        if not name:
            name = f"next_qr_{time.strftime('%H%M%S')}"
        name += ".png"
        name = os.path.join(path, name)
        self._image.save(name)
        return self
