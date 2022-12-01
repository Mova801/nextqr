import customtkinter as ct

from new.app import controller
from new.libs import constants
from new.popup import popup

_WIN_WIDTH: int = 450
_WIN_HEIGHT: int = 200
_TITLE_SIZE: str = 20
_FONT: str = "Roboto Medium"
_FONT_SIZE: str = 12


class ErrorPopup(popup.Popup):

    def __init__(
            self,
            win_title: str = "Error Popup",
            title: str = "Error Popup",
            msg: str = "Something went wrong :(",
            link: str = "") -> None:
        self.title: str = title
        self.msg: str = msg
        self.link: str = link

        self.win = ct.CTk()
        self.win.title(win_title)
        self.win.geometry(f"{_WIN_WIDTH}x{_WIN_HEIGHT}")
        self.win.protocol("WM_DELETE_WINDOW", self.close)  # call self.close() when app gets closed
        ct.set_appearance_mode("Dark")
        ct.set_default_color_theme("blue")

        self.label_title: ct.CTkLabel = ...
        self.frame_msg: ct.CTkFrame = ...
        self.error_msg: ct.CTkLabel = ...

        self.build()

    def build(self) -> None:
        # build popup grid
        row_number: int = 3
        [self.win.grid_rowconfigure(x, minsize=10, weight=1) for x in range(row_number)]
        self.win.grid_columnconfigure(0, minsize=_WIN_WIDTH, weight=1)

        self.label_title = ct.CTkLabel(
            master=self.win,
            text=self.title,
            text_font=(_FONT, _TITLE_SIZE, 'bold')
        )
        self.label_title.grid(row=0, padx=5, sticky="swe")

        self.frame_msg = ct.CTkFrame(
            master=self.win,
            corner_radius=16
        )
        self.frame_msg.grid(row=1, padx=20, pady=20, sticky="nsew")

        self.error_msg = ct.CTkLabel(
            master=self.frame_msg,
            text=self.msg,
            text_font=(_FONT, _FONT_SIZE),
            text_color=constants.LIGHT_RED.hex
        )
        self.error_msg.pack(padx=20, pady=10, expand=True)

        # ============ left frame <report bug> button ============
        self.win.btn_bug = ct.CTkButton(
            master=self.win,
            text="Report to Devs",
            text_font=(_FONT, _FONT_SIZE, 'bold'),
            command=lambda: controller.follow_dev_button_callback(self.link)
        )
        self.win.btn_bug.grid(row=2, sticky="new", padx=10)

    def show(self, msg: str) -> None:
        self.error_msg.configure(text=msg)
        if self:
            self.win.mainloop()

    def close(self) -> None:
        self.win.destroy()
