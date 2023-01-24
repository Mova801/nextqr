import tkinter as tk
import customtkinter as ct

from new.controller import controller
from new.gui import news
from new.popup import preset_popups
from new.libs import constants
from new.conf import image_config


def _build_left_frame_buttons(app, frame_width: int, rows: int) -> None:
    """
    Builds the left frame option buttons.
    :param app: master of the frame
    :param frame_width: frame width dimension (pixel)
    :param rows: number of rows for the frame
    :return: None
    """
    btn_generate_text: str = "Generate QR"
    btn_read_file_text: str = "Read QR"
    btn_follow_dev_text: str = "Follow Dev"
    btn_news_dev: str = "Features Updates"

    # ============ left frame <generate> button ============
    app.lf_btn_generate = ct.CTkButton(
        master=app.lf,
        text=btn_generate_text,
        image=app.images[image_config.AvailableImages.QR],
        compound=app.config.layout.button.img_position,
        font=(app.config.font.roboto, app.config.font.size_M),
        command=lambda: controller.generate_button_callback(app),
        height=app.config.layout.button.height,
        width=frame_width
    )
    app.lf_btn_generate.grid(row=1, column=0, padx=app.config.layout.left_frame.inner_padx)

    # ============ left frame <read file> button ============
    app.lf_btn_generate = ct.CTkButton(
        master=app.lf,
        text=btn_read_file_text,
        image=app.images[image_config.AvailableImages.SCAN],
        compound=app.config.layout.button.img_position,
        font=(app.config.font.roboto, app.config.font.size_M),
        command=lambda: controller.read_button_callback(app),
        height=app.config.layout.button.height,
        width=frame_width,
        fg_color=constants.LIGHT_CYAN.hex,
        state=tk.DISABLED
    )
    app.lf_btn_generate.grid(row=2, column=0, padx=app.config.layout.left_frame.inner_padx)

    # ============ left frame <premium> button ============
    app.lf_btn_generate = ct.CTkButton(
        master=app.lf,
        text=btn_follow_dev_text,
        font=(app.config.font.roboto, app.config.font.size_M),
        height=app.config.layout.button.height,
        width=frame_width,
        command=lambda: controller.follow_dev_button_callback(app.config.link.github),
        image=app.images[image_config.AvailableImages.GITHUB.value],
        compound=app.config.layout.button.img_position
    )
    app.lf_btn_generate.grid(row=3, column=0, padx=app.config.layout.left_frame.inner_padx)

    # ============ left frame <report bug> button ============
    app.lf_btn_generate = ct.CTkButton(
        master=app.lf,
        text="",
        width=app.config.image.bug.size,
        height=app.config.image.bug.size,
        fg_color=constants.DARK_GRAY.hex,
        hover_color=constants.DARK_GRAY.hex,
        text_color=constants.BLACK.hex,
        command=lambda: controller.follow_dev_button_callback(app.config.link.github),
        image=app.images[image_config.AvailableImages.BUG.value],
        compound=app.config.layout.button.img_position
    )
    app.lf_btn_generate.grid(row=rows - 1, column=0, sticky="e", padx=app.config.layout.left_frame.inner_padx)

    # ============ left frame <report bug> button ============
    app.lf_btn_generate = ct.CTkButton(
        master=app.lf,
        text=btn_news_dev,
        font=(app.config.font.roboto, app.config.font.size_M),
        text_color=constants.WHITE.hex,
        fg_color=constants.GREEN.hex,
        hover_color=constants.DARK_GREEN.hex,
        height=app.config.layout.button.height,
        width=frame_width,
        command=lambda: preset_popups.get_news_popup(news.NEWS).show(),
        image=app.images[image_config.AvailableImages.MEGAPHONE.value],
        compound=app.config.layout.button.img_position
    )
    app.lf_btn_generate.grid(row=4, column=0, sticky="w", padx=app.config.layout.left_frame.inner_padx)


def build_left_frame(app) -> ct.CTkFrame:
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
        font=(app.config.font.roboto, int(app.config.font.title_size_L))
    )
    app.rf_label_title.grid(row=0, column=0)

    # ============ left frame buttons setup ============
    _build_left_frame_buttons(app, frame_width, row_number)

    # ============ left frame build info setup ============
    app.rf_label_build = ct.CTkLabel(
        master=app.lf,
        text=f"build {app.config.app.build} v{app.config.app.version}",
        font=(app.config.font.roboto, int(app.config.font.size_S))
    )
    app.rf_label_build.grid(row=row_number - 1, column=0, sticky="w", padx=app.config.layout.left_frame.inner_padx)

    return app.lf
