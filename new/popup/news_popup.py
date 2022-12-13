import tkinter as tk
import customtkinter as ct

from new.libs import constants
from new.popup import popup


class NewsPopup(popup.Popup):

    def __init__(
            self,
            win_title: str = "News Popup",
            title: str = "News Popup",
            news: list[str] = None) -> None:
        self.title: str = title

        self.news: str = news

        self.win = ct.CTk()
        self.win.title(win_title)
        self.win.geometry(f"{popup.WIN_WIDTH}x{popup.WIN_HEIGHT * 1.5}")
        self.win.protocol("WM_DELETE_WINDOW", self.close)  # call self.close() when gui gets closed
        ct.set_appearance_mode("Dark")
        ct.set_default_color_theme("blue")

        self.label_title: ct.CTkLabel = ...
        self.frame_msg: ct.CTkFrame = ...
        self.news_textbox: ct.CTkTextbox = ...

        self.build()

    def build(self) -> None:
        # build popup grid
        row_number: int = 2
        [self.win.grid_rowconfigure(x, minsize=25, weight=1) for x in range(row_number)]
        self.win.grid_columnconfigure(0, minsize=popup.WIN_WIDTH, weight=1)

        self.label_title = ct.CTkLabel(
            master=self.win,
            text=self.title,
            text_font=(popup.FONT, popup.TITLE_SIZE, 'bold'),
            text_color=constants.GREEN.hex
        )
        self.label_title.grid(row=0, padx=5, sticky="nsew")

        self.news_textbox = ct.CTkTextbox(
            master=self.win,
            text_font=(popup.FONT, popup.FONT_SIZE, 'bold')
        )
        self.news_textbox.grid(row=1, padx=10, pady=10, sticky="nsew")

        [self.news_textbox.insert(f"{i}.0", "▶ " + news + "\n") for i, news in enumerate(self.news)]
        self.news_textbox.configure(state=tk.DISABLED)

        # self.news_textbox.insert("0.0", self.news)

    def show(self, news: list[str] = "") -> None:
        if news:
            self.news_textbox.configure(text=news)
        if self:
            self.win.mainloop()

    def close(self) -> None:
        self.win.destroy()
