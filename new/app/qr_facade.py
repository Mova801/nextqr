from tkinter import filedialog
from typing import Optional

from new.utility import utility, nextqr


def open_link_to_dev(link: str) -> None:
    """
    Opens the GitHub developer link.
    :param link: link to open
    :return: None
    """
    utility.open_link(link)


def show_image_from_path(image: str, ) -> None:
    """
    Opens the image at the given path.
    :param image: image to open (with path)
    :return: None
    """
    utility.show_image(image)


def open_file_dialog(
        filetypes: list[str],
        title: Optional[str] = "Select A File",
        initialdir: Optional[str] = "/") -> str:
    """
    Opens a file dialog and returns the selected file (restricted to the given filetypes).
    :param title: title of the file dialog
    :param filetypes: list o selectable file types
    :param initialdir: initial file dialog directory
    :return: selected file
    """
    return filedialog.askopenfilename(
        initialdir=initialdir, title=title, filetypes=filetypes
    )


def get_path_dialog(
        filetypes: list[str],
        title: Optional[str] = "Select A Path",
        initialdir: Optional[str] = "/") -> str:
    """
    Opens a file dialog and returns the selected path and the selected filename (restricted to the given filetypes).
    :param title: title of the file dialog
    :param filetypes: list o selectable file types
    :param initialdir: initial file dialog directory
    :return: selected path and filename
    """
    return filedialog.asksaveasfilename(title=title, filetypes=filetypes, initialdir=initialdir)


def generate_qr(name: str, text: str, path: str, image: str) -> None:
    back = (0, 0, 0)
    fill = (255, 255, 255)
    qr: nextqr.QR = nextqr.QR(name=name, data=text, fill_color=fill, back_color=back)
    qr.add_image(image, 60)
    qr.generate(path)
