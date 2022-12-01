import customtkinter as ct

from new.popup import popup
from new.utility import colors


class WarningPopup(popup.Popup):

    def __init__(
            self,
            win_title: str = "Popup",
            title: str = "Popup",
            msg: str = "Hellooo") -> None:
        self.title: str = title

        self.msg: str = msg

        self.win = ct.CTk()
        self.win.title(win_title)
        self.win.geometry(f"{popup.WIN_WIDTH}x{popup.WIN_HEIGHT}")
        self.win.protocol("WM_DELETE_WINDOW", self.close)  # call self.close() when app gets closed
        ct.set_appearance_mode("Dark")
        ct.set_default_color_theme("blue")

        self.label_title: ct.CTkLabel = ...
        self.frame_msg: ct.CTkFrame = ...
        self.error_msg: ct.CTkLabel = ...

        self.build()

    def build(self) -> None:
        # build popup grid
        row_number: int = 2
        [self.win.grid_rowconfigure(x, minsize=10, weight=1) for x in range(row_number)]
        self.win.grid_columnconfigure(0, minsize=popup.WIN_WIDTH, weight=1)

        self.label_title = ct.CTkLabel(
            master=self.win,
            text=self.title,
            text_font=(popup.FONT, popup.TITLE_SIZE, 'bold')
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
            text_font=(popup.FONT, popup.FONT_SIZE),
            text_color=colors.GREEN
        )
        self.error_msg.pack(padx=20, pady=20, expand=True)

    def show(self, msg: str) -> None:
        self.error_msg.configure(text=msg)
        if self:
            self.win.mainloop()

    def close(self) -> None:
        self.win.destroy()
