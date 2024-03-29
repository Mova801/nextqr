import customtkinter as ct

from new.controller import controller
from new.gui.elements import image_frame
from new.libs import constants


def build_right_frame_generate(app) -> ct.CTkFrame:
    """
    Builds the layout of the right frame used to generate a new qr code.
    :param app: master of the frame
    :return: right frame
    """
    label_title_text: str = "Generate QR Code"
    entry_qrname_text: str = "Enter QR Name"
    label_qrcontent_text: str = "Enter QR Content"
    textbox_qrcontent_text: str = "Hello QR!"
    label_image_select_text: str = "Select QR Image"
    btn_generate_text: str = "Generate QR"

    # ============ right frame setup ============
    frame_width: int = int(app.config.screen.size.split("x")[0]) // app.config.layout.right_frame.scale_factor
    app.rf = ct.CTkFrame(master=app.gui, width=frame_width,
                         corner_radius=0)  # gui.config.layout.right_frame.corner_radius)
    app.rf.grid(
        row=0,
        column=1,
        sticky=app.config.layout.right_frame.sticky,
        padx=app.config.layout.right_frame.padding
    )

    # ============ right frame grid setup: 12x2 ============
    row_number: int = 8
    [app.rf.grid_rowconfigure(x, minsize=20, weight=1) for x in range(row_number)]
    col_number: int = 1
    [app.rf.grid_columnconfigure(x, minsize=20, weight=1) for x in range(col_number)]

    ri: int = 0  # row index

    # ============ right frame title setup ============
    app.rf_label_title = ct.CTkLabel(
        master=app.rf,
        text=label_title_text,
        font=(app.config.font.roboto, int(app.config.font.title_size_L))
    )
    app.rf_label_title.grid(row=ri, column=0, padx=app.config.layout.right_frame.inner_padx, sticky="w")

    # ============ right frame label qr name ============
    app.rf_label_title = ct.CTkLabel(
        master=app.rf,
        text=entry_qrname_text,
        font=(app.config.font.roboto, int(app.config.font.title_size_M))
    )
    app.rf_label_title.grid(row=ri + 1, column=0, padx=app.config.layout.right_frame.inner_padx, sticky="w")

    # ============ right frame entry qr name ============
    app.rf_entry_name = ct.CTkEntry(
        master=app.rf,
        width=app.config.layout.entry.width,
        height=app.config.layout.entry.height,
        placeholder_text=entry_qrname_text,
        font=(app.config.font.roboto, app.config.font.size_M),
    )
    app.rf_entry_name.grid(row=ri + 2, column=0, padx=app.config.layout.right_frame.inner_padx * 1.5, sticky="w")

    # ============ right frame label qr content ============
    app.rf_label_title = ct.CTkLabel(
        master=app.rf,
        text=label_qrcontent_text,
        font=(app.config.font.roboto, int(app.config.font.title_size_M))
    )
    app.rf_label_title.grid(row=ri + 3, column=0, padx=app.config.layout.right_frame.inner_padx, sticky="w")

    # ============ right frame textbox qr content ============
    app.rf_textbox_content = ct.CTkTextbox(
        master=app.rf,
        width=app.config.layout.textbox.width,
        height=app.config.layout.textbox.height,
        font=(app.config.font.roboto, app.config.font.size_M),
    )
    app.rf_textbox_content.grid(row=ri + 4, column=0, padx=app.config.layout.right_frame.inner_padx * 1.5, sticky="w")
    app.rf_textbox_content.insert("0.0", textbox_qrcontent_text)

    # ============ right frame label image select ============
    app.rf_label_title = ct.CTkLabel(
        master=app.rf,
        text=label_image_select_text,
        font=(app.config.font.roboto, int(app.config.font.title_size_M))
    )
    app.rf_label_title.grid(row=ri + 5, column=0, padx=app.config.layout.right_frame.inner_padx, sticky="w")

    # ============ right frame image frame ============
    image_frame.build_image_frame(app, ri + 6)

    app.rf_btn_generate = ct.CTkButton(
        master=app.rf,
        text=btn_generate_text,
        font=(app.config.font.roboto, int(app.config.font.title_size_M)),
        height=app.config.layout.button.height,
        fg_color=constants.WHITE.hex,
        hover_color=constants.GRAY.hex,
        text_color=constants.CYAN.hex,
        command=lambda: controller.generate_qr_callback(app)
    )
    app.rf_btn_generate.grid(row=ri + 7, column=0, padx=app.config.layout.right_frame.inner_padx, sticky="we")

    return app.rf


def build_right_frame_read(app) -> ct.CTkFrame:
    """
    Builds the layout of the right frame used to read an existent qr code, either from camera or file.
    :param app: master of the frame
    :return: right frame
    """

    # ============ right frame setup ============
    frame_width: int = int(app.config.screen.size.split("x")[0]) // app.config.layout.right_frame.scale_factor
    app.rf = ct.CTkFrame(master=app.gui, width=frame_width,
                         corner_radius=0)  # gui.config.layout.right_frame.corner_radius)
    app.rf.grid(
        row=0,
        column=1,
        sticky=app.config.layout.right_frame.sticky,
        padx=app.config.layout.right_frame.padding,
        # pady=gui.config.layout.right_frame.padding
    )

    # ============ right frame grid setup: 8x2 ============
    row_number: int = 12
    [app.rf.grid_rowconfigure(x, minsize=20, weight=1) for x in range(row_number)]
    col_number: int = 2
    [app.rf.grid_columnconfigure(x, minsize=20, weight=1) for x in range(col_number)]

    # ============ right frame title setup ============
    app.rf_label_title = ct.CTkLabel(
        master=app.rf,
        text="Read QR Code",
        font=(app.config.font.roboto, int(app.config.font.title_size_L))
    )
    app.rf_label_title.grid(row=0, column=0, padx=app.config.layout.right_frame.inner_padx, sticky="w")

    # ============ right frame entry qr name ============
    app.rf_entry_qrname = ct.CTkEntry(
        master=app.rf,
        width=app.config.layout.entry.width,
        height=app.config.layout.entry.height,
        placeholder_text="Enter QR file name (png)",
        font=(app.config.font.roboto, app.config.font.size_M),
    )
    app.rf_entry_qrname.grid(row=1, column=0, padx=app.config.layout.right_frame.inner_padx, sticky="w")

    return app.rf
