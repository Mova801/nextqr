import PIL.Image
import PIL.ImageTk


# @contextlib.contextmanager
# def open_image(path: str) -> PIL.ImageTk.PhotoImage:
#     """"""
#     image = PIL.Image.open(path)
#     yield image
#     image.close()


def open_image(image_name: str, size: int) -> PIL.ImageTk.PhotoImage:
    """Opens and resizes an image file and returns it as PhotoImage."""
    image = PIL.Image.open(image_name)
    if size > 0:
        image = image.resize((size, size), PIL.Image.ANTIALIAS)
    return PIL.ImageTk.PhotoImage(image)


def show_image(path: str) -> None:
    """
    Shows the image at the given path.
    :param path: image to show (with path)
    :return: None
    """
    if path:
        PIL.Image.open(path).show()


def load_images(images_to_load: list[dict[[str, int], [str, str]]]) -> dict[str, PIL.ImageTk]:
    """
    Loads the image at the given path, each image has a size.
    :param images_to_load: list of image to load (and path)
    """
    loaded_images = {}
    for image in images_to_load:
        image_key: str = image["path"].split("/")[-1][:-4]
        loaded_images[image_key] = open_image(image["path"], image["size"])
    return loaded_images
