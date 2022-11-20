import customtkinter as ct

from new.app.left_frame import build_left_frame
from new.conf.config import NextQrConfig


class App:
    """
    NextQR application class.
    In order to use a new app you must ensure to:
        - instantiate a new app
        - build the app
        - run the app

    If the auto_build option in the configuration file is enabled then you don't need build the app.
    The auto_build option is disabled by default.
    """

    def __init__(self, config: NextQrConfig) -> None:
        self.running: bool = False
        self.gui = ct.CTk()
        self.gui.title(config.app.name + " " + config.app.version)
        self.gui.geometry(config.screen.size)
        self.gui.iconbitmap(config.image.logo)
        self.gui.resizable(config.screen.resizable_width, config.screen.resizable_height)
        self.gui.protocol("WM_DELETE_WINDOW", self.close)  # call self.close() when app gets closed

        # setting app theme and appearance
        self.config: NextQrConfig = config
        self.appearance_mode: str = ""
        self.color_theme: str = ""
        self.set_appearance_mode(config.screen.appearance_mode)
        self.set_color_theme(config.screen.color_theme)

        self.lf = None
        # ...
        if config.app.auto_build:
            self.build()

    def set_appearance_mode(self, appearance_mode: str) -> None:
        """Changes the appearance of the application."""
        # Modes: "System" (standard), "Dark", "Light"
        self.appearance_mode = appearance_mode
        if not appearance_mode:
            self.appearance_mode = "Dark"
        ct.set_appearance_mode(self.appearance_mode)

    def set_color_theme(self, color_theme: str) -> None:
        """Changes the color theme of the application."""
        # Themes: "blue" (standard), "green", "dark-blue"
        self.color_theme = color_theme
        if not color_theme:
            self.color_theme = "blue"
        ct.set_default_color_theme(self.color_theme)

    def build(self) -> any:
        """Builds the application layout."""
        self.gui.grid_columnconfigure(1, weight=1)
        self.gui.grid_rowconfigure(0, weight=1)
        build_left_frame(self)

    def generate_button_event(self) -> None:
        """Handles the left frame generate button click."""
        print("Generate button clicked!")

    def read_button_event(self) -> None:
        """Handles the left frame generate button click."""
        print("Read button clicked!")

    def run(self) -> None:
        """Runs the application instance."""
        if self:
            self.gui.mainloop()

    def close(self) -> None:
        """Destroy the window when closed."""
        self.gui.destroy()
