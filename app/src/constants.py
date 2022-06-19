import os

MAX_PAGES = 2
# posizione del file .exe di NextQR
EXE_LOCATION = os.path.dirname(os.path.realpath(__file__))
# posizione del file di configurazione delle impostazioni di NextQR
CONF_LOCATION = "nextqr\\app\\src\\nextqr.ini"
MAIN_KEYS = ('-', '+', '#', '*', 'o', 'esc', 'e')
MAIN_READQR_KEYS = ('c', 'f', '-', 'esc', 'Y')
# MESSAGES_PATH = "nextqr.app.messages.messages"
SCAN_WINDOW_NAME = "NextQR - ScanningQR"

