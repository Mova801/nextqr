import PIL.ImageTk
import customtkinter as ct

from new.app import elements
from new.conf.config import NextQrConfig
from new.conf.image_config import image_list_from_config
from new.exceptions import nextqr_exceptions
from new.utility import utility

ImageTkdictionary = dict[str, PIL.ImageTk]


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

        self.images: ImageTkdictionary = utility.load_images(image_list_from_config(self.config.image))
        self.rf_generating: bool = False

        self.lf: ct.CTkFrame = ...
        self.rf: ct.CTkFrame = ...

        self.imf: ct.CTkFrame = ...
        self.imf_entry_path: ct.CTkEntry = ...
        self.rf_entry_name: ct.CTkEntry = ...
        self.rf_textbox_content: ct.CTkTextbox = ...

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

        # set gui grid
        self.gui.grid_columnconfigure(1, weight=1)
        self.gui.grid_rowconfigure(0, weight=1)
        # left frame
        elements.left_frame.build_left_frame(self)
        # default right frames
        elements.right_frame.build_right_frame_generate(self)
        self.rf_generating = True

    def run(self) -> None:
        """Runs the application instance."""
        if self:
            self.gui.mainloop()

    def close(self) -> None:
        """Destroy the window when closed."""
        self.gui.destroy()
