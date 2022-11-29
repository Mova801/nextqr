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
            fill_color: tuple[int, int, int] = (0, 0, 0),
            back_color: tuple[int, int, int] = (255, 255, 255)
    ) -> None:
        if not name:
            name = f"qr_{time.strftime('%H%M%S'):_^2}"
        self.name: str = utility.sanitize_file_name(name)
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
        """
        Adds an image to the qr.
        :param image: image path
        :param dimension: image dimension (in pixels) on the qr
        :return: None
        """
        if not image:
            return

        img = PIL.Image.open(rf"{image}")
        img.thumbnail((dimension, dimension))
        position = (
            (self.qr_image.size[0] - img.size[0]) // 2,
            (self.qr_image.size[1] - img.size[1]) // 2
        )
        self.qr_image.paste(img, position)

    def add_data(self, data: str) -> None:
        """
        Replaces qr data.
        :param data: data to insert into the qr
        :return: None
        """
        self.qr.add_data(data)

    def save(self, path: str = "") -> None:
        """
        Saves the qr code as png file at the given path.
        :param path: final path
        :return: None
        """
        self.qr_image.save(f"{path}/{self.name}.png")
