from tkinter import filedialog
from typing import Optional

from new.app.app import App
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
        initialfile: str = "",
        title: Optional[str] = "Select A Path",
        initialdir: Optional[str] = "/") -> str:
    """
    Opens a file dialog and returns the selected path and the selected filename (restricted to the given filetypes).
    :param filetypes: list o selectable file types
    :param initialfile: initial file name
    :param title: title of the file dialog
    :param initialdir: initial file dialog directory
    :return: selected path and file name
    """
    return filedialog.asksaveasfilename(
        title=title,
        filetypes=filetypes,
        initialdir=initialdir,
        initialfile=initialfile
    )


def generate_qr(app: App) -> None:
    name: str = app.rf_entry_name.get()

    path: str = get_path_dialog(
        filetypes=[("png", "*.png"), ],
        initialfile=name
    )
    path, name = path.rsplit("/", 1)
    content: str = app.rf_textbox_content.get(1.0, "end")
    image: str = app.imf_entry_path.get()
    qr: nextqr.QR = nextqr.QR(
        name=name,
        data=content,
        fill_color=app.config.qr.fill_color,
        back_color=app.config.qr.back_color
    )
    qr.add_image(image=image, dimension=app.config.qr.image_dimension)
    qr.save(path)
