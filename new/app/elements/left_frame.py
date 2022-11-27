import customtkinter as ct

from new.utility.colors import Color
from new.conf.image_config import AvailableImages
from new.app.app import App


def _build_left_frame_buttons(app, frame_width: int, rows: int) -> None:
    """
    Builds the left frame option buttons.
    :param app: master of the frame
    :param frame_width: frame width dimension (pixel)
    :param rows: number of rows for the frame
    :return: None
    """
    btn_generate_text: str = "Generate QR"
    btn_read_file_text: str = "Read QR from file"
    btn_read_cam_text: str = "Read QR from camera"
    btn_follow_dev_text: str = "Follow Dev"

    # ============ left frame <generate> button ============
    app.lf_btn_generate = ct.CTkButton(
        master=app.lf,
        text=btn_generate_text,
        # image=,
        text_font=(app.config.font.roboto, app.config.font.size_M),
        command=app.generate_button_clik_event,
        height=app.config.layout.button.height,
        width=frame_width
    )
    app.lf_btn_generate.grid(row=1, column=0, padx=app.config.layout.left_frame.inner_padx)

    # ============ left frame <read file> button ============
    app.lf_btn_generate = ct.CTkButton(
        master=app.lf,
        text=btn_read_file_text,
        # image=,
        text_font=(app.config.font.roboto, app.config.font.size_M),
        command=app.read_button_clik_event,
        height=app.config.layout.button.height,
        width=frame_width
    )
    app.lf_btn_generate.grid(row=2, column=0, padx=app.config.layout.left_frame.inner_padx)

    # ============ left frame <read cam> button ============
    app.lf_btn_generate = ct.CTkButton(
        master=app.lf,
        text=btn_read_cam_text,
        # image=,
        text_font=(app.config.font.roboto, app.config.font.size_M),
        command=app.read_button_clik_event,
        height=app.config.layout.button.height,
        width=frame_width
    )
    app.lf_btn_generate.grid(row=3, column=0, padx=app.config.layout.left_frame.inner_padx)

    # ============ left frame <premium> button ============
    app.lf_btn_generate = ct.CTkButton(
        master=app.lf,
        text=btn_follow_dev_text,
        text_font=(app.config.font.roboto, app.config.font.size_M),
        height=app.config.layout.button.height,
        width=frame_width,
        fg_color=str(Color.GOLD.value),
        hover_color=str(Color.DARK_GOLD.value),
        text_color=str(Color.BLACK.value),
        command=app.follow_dev_clik_event,
        image=app.images[AvailableImages.GITHUB.value],
        compound=app.config.layout.button.img_position
    )
    app.lf_btn_generate.grid(row=rows - 2, column=0, padx=app.config.layout.left_frame.inner_padx)

    # ============ left frame <report bug> button ============
    app.lf_btn_generate = ct.CTkButton(
        master=app.lf,
        text="",
        width=app.config.image.bug.size,
        height=app.config.image.bug.size,
        fg_color=str(Color.DARK_GRAY.value),
        hover_color=str(Color.DARK_GRAY.value),
        text_color=str(Color.BLACK.value),
        command=app.follow_dev_clik_event,
        image=app.images[AvailableImages.BUG.value],
        compound=app.config.layout.button.img_position
    )
    app.lf_btn_generate.grid(row=rows - 1, column=0, sticky="e", padx=app.config.layout.left_frame.inner_padx // 2)


def build_left_frame(app: App) -> ct.CTkFrame:
    """
    Builds the layout of the left frame, contains many options.
    :param app: master of the frame
    :return: left frame
    """

    # ============ left frame setup ============
    frame_width: int = int(app.config.screen.size.split("x")[0]) // app.config.layout.left_frame.scale_factor
    app.lf = ct.CTkFrame(master=app.gui, width=frame_width, corner_radius=0)
    app.lf.grid(row=0, column=0, sticky=app.config.layout.left_frame.sticky)

    # ============ left frame grid setup: 12x1 ============
    row_number: int = 14
    [app.lf.grid_rowconfigure(x, minsize=20, weight=1) for x in range(row_number)]

    # ============ left frame title setup ============
    app.rf_label_title = ct.CTkLabel(
        master=app.lf,
        text=app.config.app.name,
        text_font=(app.config.font.roboto, int(app.config.font.title_size_L))
    )
    app.rf_label_title.grid(row=0, column=0)

    # ============ left frame buttons setup ============
    _build_left_frame_buttons(app, frame_width, row_number)

    # ============ left frame build info setup ============
    app.rf_label_build = ct.CTkLabel(
        master=app.lf,
        text=f"build {app.config.app.build} v{app.config.app.version}",
        text_font=(app.config.font.roboto, int(app.config.font.size_S))
    )
    app.rf_label_build.grid(row=row_number - 1, column=0, sticky="w", padx=app.config.layout.left_frame.inner_padx)

    return app.lf
