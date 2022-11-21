import customtkinter as ct
import PIL.ImageTk

from new.utility import utility_functions


# from new.app.app import App


def _build_left_frame_buttons(app, frame_width: int, rows: int) -> None:
    """
    Builds the left frame option buttons.
    :param app: master of the frame
    :param frame_width: frame width dimension (pixel)
    :param rows: number of rows for the frame
    :return: None
    """
    lf_buttons_padx: int = 20

    # ============ left frame <generate> button ============
    app.lf_btn_generate = ct.CTkButton(
        master=app.lf,
        text="Generate",
        # image=,
        text_font=(app.config.font.roboto, app.config.font.size),
        command=app.generate_button_clik_event,
        height=app.config.layout.button.height,
        width=frame_width
    )
    app.lf_btn_generate.grid(row=1, column=0, padx=lf_buttons_padx)

    # ============ left frame <read file> button ============
    app.lf_btn_generate = ct.CTkButton(
        master=app.lf,
        text="Read file",
        # image=,
        text_font=(app.config.font.roboto, app.config.font.size),
        command=app.read_button_clik_event,
        height=app.config.layout.button.height,
        width=frame_width
    )
    app.lf_btn_generate.grid(row=2, column=0, padx=lf_buttons_padx)

    # ============ left frame <read cam> button ============
    app.lf_btn_generate = ct.CTkButton(
        master=app.lf,
        text="Read From Camera",
        # image=,
        text_font=(app.config.font.roboto, app.config.font.size),
        command=app.read_button_clik_event,
        height=app.config.layout.button.height,
        width=frame_width
    )
    app.lf_btn_generate.grid(row=3, column=0, padx=lf_buttons_padx)

    # ============ left frame <premium> button ============
    GITHUB_ICON: PIL.ImageTk.PhotoImage = utility_functions.open_image(app.config.image.github, app.config.image.size)
    app.lf_btn_generate = ct.CTkButton(
        master=app.lf,
        text="Follow Dev",
        # image=,
        text_font=(app.config.font.roboto, app.config.font.size),
        height=app.config.layout.button.height,
        width=frame_width,
        fg_color="#FFB144",
        hover_color="#99692A",
        text_color="Black",
        command=app.follow_dev_clik_event,
        image=GITHUB_ICON,
        compound=app.config.layout.button.img_position
    )
    app.lf_btn_generate.grid(row=rows - 2, column=0, padx=lf_buttons_padx)


def build_left_frame(app) -> ct.CTkFrame:
    """
    Builds the layout of the left frame, contains many options.
    :param app: master of the frame
    :return: left frame
    """
    scale_factor: int = 5

    # ============ left frame setup ============
    frame_width: int = int(app.config.screen.size.split("x")[0]) // scale_factor
    app.lf = ct.CTkFrame(master=app.gui, width=frame_width, corner_radius=0)
    app.lf.grid(row=0, column=0, sticky="nsew")

    # ============ left frame grid setup: 12x1 ============
    row_number: int = 14
    [app.lf.grid_rowconfigure(x, minsize=20, weight=1) for x in range(row_number)]

    # ============ left frame title setup ============
    app.rf_label_title = ct.CTkLabel(
        master=app.lf,
        text=app.config.app.name,
        text_font=(app.config.font.roboto, int(app.config.font.size * 1.8))
    )
    app.rf_label_title.grid(row=0, column=0)

    # ============ left frame buttons setup ============
    _build_left_frame_buttons(app, frame_width, row_number)

    # ============ left frame build info setup ============
    app.rf_label_build = ct.CTkLabel(
        master=app.lf,
        text=f"build {app.config.app.build} v{app.config.app.version}",
        text_font=(app.config.font.roboto, int(app.config.font.size // 1.2))
    )
    app.rf_label_build.grid(row=row_number - 1, column=0)

    return app.lf
