import PIL.Image
import PIL.ImageTk
import webbrowser as wb
import re


def sanitize_file_name(filename: str) -> str:
    """
    Removes any invalid character from the given filename.
    :param filename: filename to sanitize
    :return: sanitized filename
    """
    invalid_chars = [r'\\', r'\/', r'\:', r'\*', r'\?', r'\"', r'\<', r'\>', r'\|']
    for char in invalid_chars:
        filename = re.sub(char, "", filename)
    return filename


def open_image(image_name: str, size: int) -> PIL.ImageTk.PhotoImage:
    """Opens and resizes an image file and returns it as PhotoImage."""
    image = PIL.Image.open(image_name).resize((size, size), PIL.Image.ANTIALIAS)
    return PIL.ImageTk.PhotoImage(image)


def load_images(images_to_load: list[dict[[str, int], [str, str]]]) -> dict[str, PIL.ImageTk]:
    """Loads the image at the given path, each image has a size.
    :param images_to_load: list of image to load (and path)
    """
    loaded_images = {}
    for image in images_to_load:
        image_key: str = image["path"].split("/")[-1][:-4]
        loaded_images[image_key] = open_image(image["path"], image["size"])
    return loaded_images


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
