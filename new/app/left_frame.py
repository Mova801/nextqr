import customtkinter as ct


# from new.app.app import App

def _build_left_frame_buttons(app, frame_width: int) -> None:
    lf_buttons_padx: int = 20

    # ============ left frame <generate> button ============
    app.lf_btn_generate = ct.CTkButton(
        master=app.lf,
        text="Generate",
        # image=,
        text_font=(app.config.font.roboto, app.config.font.size),
        command=app.generate_button_event,
        height=app.config.layout.button.height,
        width=frame_width
    )
    app.lf_btn_generate.grid(row=1, column=0, padx=lf_buttons_padx)

    # ============ left frame <read> button ============
    app.lf_btn_generate = ct.CTkButton(
        master=app.lf,
        text="Read",
        # image=,
        text_font=(app.config.font.roboto, app.config.font.size),
        command=app.read_button_event,
        height=app.config.layout.button.height,
        width=frame_width
    )
    app.lf_btn_generate.grid(row=2, column=0, padx=lf_buttons_padx)


def build_left_frame(app) -> None:
    scale_factor: int = 5

    # ============ left frame setup ============
    frame_width: int = int(app.config.screen.size.split("x")[0]) // scale_factor
    app.lf = ct.CTkFrame(master=app.gui, width=frame_width, corner_radius=0)
    app.lf.grid(row=0, column=0, sticky="nsew")

    # ============ left frame grid setup: 12x1 ============
    [app.lf.grid_rowconfigure(x, minsize=20, weight=1) for x in range(12)]

    # ============ left frame title setup ============
    app.lf_label_title = ct.CTkLabel(
        master=app.lf,
        text=app.config.app.name,
        text_font=(app.config.font.roboto, int(app.config.font.size * 1.4))
    )
    app.lf_label_title.grid(row=0, column=0)

    # ============ left frame buttons setup ============
    _build_left_frame_buttons(app, frame_width)

    # ============ left frame build info setup ============
    app.lf_label_build = ct.CTkLabel(
        master=app.lf,
        text=f"build {app.config.app.build} v{app.config.app.version}",
        text_font=(app.config.font.roboto, int(app.config.font.size // 1.4))
    )
    app.lf_label_build.grid(row=11, column=0)
