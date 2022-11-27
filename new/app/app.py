import PIL.ImageTk
import customtkinter as ct

from new.app import elements
from new.conf.config import NextQrConfig
from new.conf.image_config import image_list_from_config
from new.exceptions import nextqr_exceptions
from new.utility import utility_functions

images_dict = dict[str, PIL.ImageTk]


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
        # controller [WIP]
        self.controller = ...

        # gui
        self.gui = ct.CTk()
        self.gui.title(config.app.name + " " + config.app.version)
        self.gui.geometry(config.screen.size)
        self.gui.iconbitmap(config.image.logo.path)
        self.gui.resizable(config.screen.resizable_width, config.screen.resizable_height)
        self.gui.protocol("WM_DELETE_WINDOW", self.close)  # call self.close() when app gets closed

        # setting app theme and appearance
        self.config: NextQrConfig = config
        self.appearance_mode: str = ""
        self.color_theme: str = ""
        self.set_appearance_mode(config.screen.appearance_mode)
        self.set_color_theme(config.screen.color_theme)

        self.images: images_dict = utility_functions.load_images(image_list_from_config(self.config.image))
        self.rf_generating: bool = False
        self.lf: ct.CTkFrame = ...
        self.rf: ct.CTkFrame = ...
        # ...
        if config.app.auto_build:
            self.config.app.auto_build = False
            self.build()
            self.config.app.auto_build = True

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
        if self.config.app.auto_build:
            raise nextqr_exceptions.AutoBuildEnabledError

        # load app image
        # set gui grid
        self.gui.grid_columnconfigure(1, weight=1)
        self.gui.grid_rowconfigure(0, weight=1)
        # left frame
        elements.left_frame.build_left_frame(self)
        # default right frames
        elements.right_frame.build_right_frame_generate(self)
        self.rf_generating = True

    def generate_button_clik_event(self) -> None:
        """Handles the left frame 'generate' button click."""
        if not self.rf_generating:
            elements.right_frame.build_right_frame_generate(self)
            self.rf_generating = True

    def read_button_clik_event(self) -> None:
        """Handles the left frame 'read' button click."""
        if self.rf_generating:
            elements.right_frame.build_right_frame_read(self)
            self.rf_generating = False

    def follow_dev_clik_event(self) -> None:
        """Handles the left frame 'follow dev' button click."""
        utility_functions.open_link(self.config.link.github)

    def browse_click_event(self) -> None:
        """Handles the right frame 'browse' button click."""
        print("Browse browse brose!")

    def run(self) -> None:
        """Runs the application instance."""
        if self:
            self.gui.mainloop()

    def close(self) -> None:
        """Destroy the window when closed."""
        self.gui.destroy()
