import customtkinter as ct

from new.popup import popup


class ErrorPopup(popup.Popup):

    def __init__(self, title: str = "Error Popup") -> None:
        self.title = title
        self.win = ct.CTk()
        self.win.title("Error Popup")
        self.win.geometry("450x100")
        self.win.resizable(False, False)
        self.win.protocol("WM_DELETE_WINDOW", self.close)  # call self.close() when app gets closed
        ct.set_appearance_mode("Dark")
        ct.set_default_color_theme("blue")

        self.label_title: ct.CTkLabel = ...
        self.frame_msg: ct.CTkFrame = ...
        self.error_msg: ct.CTkLabel = ...

    def show(self, msg: str) -> None:
        self.label_title = ct.CTkLabel(
            master=self.win,
            text=self.title,
            text_font=("Roboto Medium", 12)
        )
        self.label_title.pack(expand=True)

        self.frame_msg = ct.CTkFrame(
            master=self.win
        )
        self.frame_msg.pack(expand=True)
        self.error_msg = ct.CTkLabel(
            master=self.win,
            text=msg,
            text_font=("Roboto Medium", 12)
        )
        self.error_msg.pack(expand=True)  # , sticky="nsew")
        if self:
            self.win.mainloop()

    def close(self) -> None:
        self.win.destroy()
