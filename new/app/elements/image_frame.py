import customtkinter as ct

from new.app.app import App
from new.utility.colors import Color


def build_image_frame(app: App) -> None:
    """
    Builds the layout of the image frame used to read qr image path and display the image.
    :param app: master of the frame
    :return: None
    """
    entry_path_text: str = "Enter Image Path"
    btn_browse_text: str = "Browse"

    # ============ right frame image frame ============
    app.rf_frame_image = ct.CTkFrame(
        master=app.rf,
        width=app.config.layout.image_frame.width,
        height=app.config.layout.image_frame.height,
        fg_color=Color.DARK_GRAY.value
    )
    app.rf_frame_image.grid(row=6, column=0, padx=app.config.layout.right_frame.inner_padx)

    # ============ right frame grid setup: 1x2 ============
    col_number: int = 2
    imf_minsize: int = app.config.layout.image_frame.width // col_number
    [app.rf_frame_image.grid_columnconfigure(x, minsize=imf_minsize, weight=1) for x in range(col_number)]

    # ============ image frame entry img path ============
    app.imf_entry_path = ct.CTkEntry(
        master=app.rf_frame_image,
        width=app.config.layout.entry.width,
        height=app.config.layout.entry.height,
        placeholder_text=entry_path_text,
        text_font=(app.config.font.roboto, app.config.font.size_M),
    )
    app.imf_entry_path.grid(
        row=1,
        column=0,
        sticky="w"
    )

    # ============ image frame entry img path ============
    app.imf_btn_validate_img_path = ct.CTkButton(
        master=app.rf_frame_image,
        width=app.config.layout.button.width // 2,
        height=app.config.layout.button.height,
        text=btn_browse_text,
        # image=,
        text_font=(app.config.font.roboto, app.config.font.size_M),
        command=app.browse_click_event,
    )
    app.imf_btn_validate_img_path.grid(row=1, column=1, padx=1, sticky="w")
