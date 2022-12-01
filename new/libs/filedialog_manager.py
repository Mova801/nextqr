import tkinter.filedialog
from typing import Optional


def open_file_dialog(
        filetypes: list[tuple[str, str]],
        title: Optional[str] = "Select A File",
        initialdir: Optional[str] = "/") -> str:
    """
    Opens a file dialog and returns the selected file (restricted to the given filetypes).
    :param title: title of the file dialog
    :param filetypes: list o selectable file types
    :param initialdir: initial file dialog directory
    :return: selected file
    """
    return tkinter.filedialog.askopenfilename(
        initialdir=initialdir, title=title, filetypes=filetypes
    )


def get_path_dialog(
        filetypes: list[tuple[str, str]],
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
    return tkinter.filedialog.asksaveasfilename(
        title=title,
        filetypes=filetypes,
        initialdir=initialdir,
        initialfile=initialfile
    )
