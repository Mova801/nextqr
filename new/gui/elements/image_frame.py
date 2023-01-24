import customtkinter as ct

from new.controller import controller
from new.libs import constants


def build_image_frame(app, row_index: int) -> None:
    """
    Builds the layout of the image frame used to read qr image path and display the image.
    :param app: master of the frame
    :param row_index: image_frame row index
    :return: None
    """
    entry_path_text: str = "Enter Image Path"
    btn_browse_text: str = "Browse"
    btn_show_text: str = "Show"

    # ============ right frame image frame ============
    app.rf_frame_image = ct.CTkFrame(
        master=app.rf,
        width=app.config.layout.image_frame.width,
        height=app.config.layout.image_frame.height,
        fg_color=constants.DARK_GRAY.hex
    )
    app.rf_frame_image.grid(row=row_index, column=0, padx=app.config.layout.right_frame.inner_padx)

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
        font=(app.config.font.roboto, app.config.font.size_M),
    )
    app.imf_entry_path.grid(
        row=1,
        column=0,
        sticky="w"
    )

    # ============ image frame <browse> button ============
    app.imf_btn_browse = ct.CTkButton(
        master=app.rf_frame_image,
        width=app.config.layout.button.width // 2,
        height=app.config.layout.button.height,
        text=btn_browse_text,
        # image=,
        font=(app.config.font.roboto, app.config.font.size_M),
        command=lambda: controller.browse_button_callback(app),
    )
    app.imf_btn_browse.grid(row=1, column=1, padx=1, sticky="w")

    # ============ image frame <show> button ============
    app.imf_btn_show_image = ct.CTkButton(
        master=app.rf_frame_image,
        width=app.config.layout.button.width // 2,
        height=app.config.layout.button.height,
        text=btn_show_text,
        # image=,
        font=(app.config.font.roboto, app.config.font.size_M),
        command=lambda: controller.start_thread(
            controller.show_image_button_callback,
            app.imf_entry_path.get()
        )
    )
    app.imf_btn_show_image.grid(row=1, column=1, padx=app.config.layout.button.width // 1.25, sticky="w")

    # thread to check if the <show img button> should be disabled or not
    controller.activate_btn_if_entry(app.imf_entry_path, app.imf_btn_show_image, app.config.app.update_time_ms)
