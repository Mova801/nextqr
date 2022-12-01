from new.app.app import App
from new.libs import nextqr
from new.libs import filedialog_manager


def generate_qr(app: App) -> None:
    """
    Generates a qr code.
    """
    name: str = app.rf_entry_name.get()

    path: str = filedialog_manager.get_path_dialog(
        filetypes=[("png", "*.png"), ],
        initialfile=name
    )
    path, name = path.rsplit("/", 1)
    content: str = app.rf_textbox_content.get(1.0, "end")
    image: str = app.imf_entry_path.get()
    qr: nextqr.QR = nextqr.QR(
        name=name,
        data=content,
        fill_color=app.config.qr.fill_color,
        back_color=app.config.qr.back_color
    )
    qr.add_image(image=image, dimension=app.config.qr.image_dimension)
    qr.save(path)
