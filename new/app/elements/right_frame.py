import customtkinter as ct

from new.app.app import App


def build_right_frame_generate(app: App) -> ct.CTkFrame:
    """
    Builds the layout of the right frame used to generate a new qr code.
    :param app: master of the frame
    :return: right frame
    """
    scale_factor: int = 5
    rf_padding: int = 10
    rf_corner_radius: int = 15
    rf_inner_padx: int = 20

    # ============ right frame setup ============
    frame_width: int = int(app.config.screen.size.split("x")[0]) // scale_factor
    app.rf = ct.CTkFrame(master=app.gui, width=frame_width, corner_radius=rf_corner_radius)
    app.rf.grid(row=0, column=1, sticky="nsew", padx=rf_padding, pady=rf_padding)

    # ============ right frame grid setup: 8x2 ============
    row_number: int = 12
    [app.rf.grid_rowconfigure(x, minsize=20, weight=1) for x in range(row_number)]
    col_number: int = 2
    [app.rf.grid_columnconfigure(x, minsize=20, weight=1) for x in range(col_number)]

    # ============ right frame title setup ============
    app.rf_label_title = ct.CTkLabel(
        master=app.rf,
        text="Generate QR Code",
        text_font=(app.config.font.roboto, int(app.config.font.size * 1.8))
    )
    app.rf_label_title.grid(row=0, column=0, padx=rf_inner_padx, sticky="w")

    # ============ right frame entry qr name ============
    app.main_entry = ct.CTkEntry(
        master=app.rf,
        width=app.config.layout.entry.width,
        height=app.config.layout.entry.height,
        placeholder_text="Enter QR name",
        text_font=(app.config.font.roboto, app.config.font.size),
    )
    app.main_entry.grid(row=1, column=0, padx=rf_inner_padx, sticky="w")

    # ============ right frame entry qr content ============
    app.main_entry = ct.CTkEntry(
        master=app.rf,
        width=app.config.layout.entry.width,
        height=app.config.layout.entry.height,
        placeholder_text="Enter QR content",
        text_font=(app.config.font.roboto, app.config.font.size),
    )
    app.main_entry.grid(row=2, column=0, padx=rf_inner_padx, sticky="w")

    return app.rf


def build_right_frame_read(app: App) -> ct.CTkFrame:
    """
    Builds the layout of the right frame used to read an existent qr code, either from camera or file.
    :param app: master of the frame
    :return: right frame
    """
    scale_factor: int = 5
    rf_padding: int = 10
    rf_corner_radius: int = 15
    rf_inner_padx: int = 20

    # ============ right frame setup ============
    frame_width: int = int(app.config.screen.size.split("x")[0]) // scale_factor
    app.rf = ct.CTkFrame(master=app.gui, width=frame_width, corner_radius=rf_corner_radius)
    app.rf.grid(row=0, column=1, sticky="nsew", padx=rf_padding, pady=rf_padding)

    # ============ right frame grid setup: 8x2 ============
    row_number: int = 12
    [app.rf.grid_rowconfigure(x, minsize=20, weight=1) for x in range(row_number)]
    col_number: int = 2
    [app.rf.grid_columnconfigure(x, minsize=20, weight=1) for x in range(col_number)]

    # ============ right frame title setup ============
    app.rf_label_title = ct.CTkLabel(
        master=app.rf,
        text="Read QR Code",
        text_font=(app.config.font.roboto, int(app.config.font.size * 1.8))
    )
    app.rf_label_title.grid(row=0, column=0, padx=rf_inner_padx, sticky="w")

    # ============ right frame entry qr name ============
    app.main_entry = ct.CTkEntry(
        master=app.rf,
        width=app.config.layout.entry.width,
        height=app.config.layout.entry.height,
        placeholder_text="Enter QR file name (png)",
        text_font=(app.config.font.roboto, app.config.font.size),
    )
    app.main_entry.grid(row=1, column=0, padx=rf_inner_padx, sticky="w")

    return app.rf
