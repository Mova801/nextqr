import PIL.Image
import PIL.ImageTk
import webbrowser as wb


def open_image(image_name: str, size: int) -> PIL.ImageTk.PhotoImage:
    """Opens and resizes an image file and returns it as PhotoImage."""
    image = PIL.Image.open(image_name).resize((size, size), PIL.Image.ANTIALIAS)
    return PIL.ImageTk.PhotoImage(image)


def show_image(image_path: str) -> None:
    """Shows an image file on screen."""
    if image_path:
        PIL.Image.open(image_path).show()


def open_link(link: str) -> None:
    """
    Opens the given link.
    :param link: link to open
    :return: None
    """
    if link:
        wb.open(link)
