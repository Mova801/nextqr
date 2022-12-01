import webbrowser
import validators


class Link:

    def __init__(self, url: str) -> None:
        if validators.url(url):
            self.url = url
        else:
            raise ValueError(f"{url} is not a valid url.")

    def open(self) -> None:
        """Opens the url."""
        webbrowser.open(self.url)
