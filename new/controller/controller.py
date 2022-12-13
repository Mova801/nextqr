"""
This module handle the calls to the App qr functions and also logs what happens.
"""
from typing import Callable
import logging
import pathlib
import threading

import tkinter as tk
import customtkinter as ct

from new.gui import elements
from new.controller import qr_facade
from new.libs import link
from new.libs import constants
from new.libs import filedialog_manager
from new.libs import image_manager

logging.basicConfig(level=logging.INFO)


def generate_button_callback(app) -> None:
    """Handles the left frame 'generate' button click."""
    logging.info("function callback to 'generate_button_callback'")
    if not app.rf_generating:
        logging.info("building 'generate qr' frame...")
        elements.right_frame.build_right_frame_generate(app)
        app.rf_generating = True


def read_button_callback(app) -> None:
    """Handles the left frame 'read' button click."""
    logging.info("function callback to 'read_button_callback'")
    if app.rf_generating:
        logging.info("building 'read qr' frame...")
        elements.right_frame.build_right_frame_read(app)
        app.rf_generating = False


def follow_dev_button_callback(url: str) -> None:
    """Handles the left frame 'follow dev' button click."""
    logging.info("function callback to 'follow_dev_button_callback'")
    logging.info(f"opening {url}...")
    link.Link(url).open()


def browse_button_callback(app) -> None:
    """Handles the right frame 'browse' button click."""
    logging.info("function callback to 'browse_button_callback'")
    logging.info("opening file dialog to select a image")
    path: str = filedialog_manager.open_file_dialog(filetypes=[("png", "*.png"), ])

    def set_entry_text(text: str) -> None:
        app.imf_entry_path.delete(0, tk.END)
        app.imf_entry_path.insert(0, text)

    if path:
        set_entry_text(path)


def show_image_button_callback(path: str) -> None:
    """Handles the right frame 'show' button click."""
    valid_path: bool = pathlib.Path(path).is_file()
    logging.info("function callback to 'show_image_button_callback'")
    logging.info(f"validation of '{path}' as valid file: {valid_path}")
    if valid_path:
        image_manager.show_image(path)


def start_thread(target_function: Callable, *args) -> None:
    """
    Starts a new daemon thread.
    :param target_function: thread target function
    :param args: args to the target_function
    :return: None
    """
    logging.info("function callback to 'start_thread'")
    th: threading = threading.Thread(target=target_function, daemon=True, args=args)
    logging.info(f"started a new daemon thread {th.name} with target '{target_function}({args})")
    th.start()


def activate_btn_if_entry(entry: ct.CTkEntry, btn_to_activate: ct.CTkButton, check_time: int) -> None:
    """..."""
    # logging.info("function callback to 'activate_btn_if_entry'")
    btn_to_activate.after(check_time, activate_btn_if_entry, entry, btn_to_activate, check_time)
    if entry.get():
        btn_to_activate.configure(state=tk.NORMAL)
        btn_to_activate.configure(fg_color=constants.CYAN.hex)
    else:
        btn_to_activate.configure(state=tk.DISABLED)
        btn_to_activate.configure(fg_color=constants.LIGHT_CYAN.hex)
    # logging.info(f"status updated for '{btn_to_activate}': {btn_to_activate.state}")


def generate_qr_callback(app) -> None:
    """
    Generates a QR code and saves it.
    """
    logging.info("function callback to 'generate_qr_callback'")
    qr_facade.generate_qr(app)
    logging.info("qrcode generated")
