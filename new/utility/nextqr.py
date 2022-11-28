import time
import PIL.Image
import qrcode

from new.utility import utility
from new.utility import colors


class QR:
    def __init__(
            self,
            name: str,
            data: str,
            fill_color: tuple[int, int, int] = "white",
            back_color: tuple[int, int, int] = "black"
    ) -> None:
        if not name:
            name = f"qr_{time.strftime('%H%M%S')}:_^2"
        self.name: str = utility.sanitize_file_name(name)
        self.data: str = data
        # TODO: check if fill and back color are valid
        self.fill_color: colors.color = fill_color
        self.back_color: colors.color = back_color

        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=20,
            border=2
        )
        self.qr.add_data(data)
        self.qr.make(fit=True)
        self.qr_image: PIL.Image = self.qr.make_image(fill_color=self.fill_color, back_color=self.back_color)

    def add_image(self, image: str, dimension: int) -> None:
        """"""
        if not image:
            return

        print(rf"{image}")
        img = PIL.Image.open(rf"{image}")
        img.thumbnail((dimension, dimension))
        position = (
            self.qr_image.size[0] - img.size // 2,
            self.qr_image.size[1] - img.size // 2
        )
        self.qr_image.paste(img, position)

    def add_data(self, data: str) -> None:
        """"""
        self.data = data

    def generate(self, path: str = "") -> None:
        """"""
        print(f"{path}/{self.name}.png")
        self.qr_image.save(f"{path}/{self.name}.png")
