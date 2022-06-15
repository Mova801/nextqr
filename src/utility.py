# imports
import ctypes
import os
import time
import validators as vl
from PIL import Image
from configurationpack.configuration import Configuration
from imagestream import ImageStream
from qrpack.qr_class import QR

dec = Decoration(show_info=False)
config = Configuration()
img = ImageStream()
new_qr = QR()
io = IOstream()

# global variables and CONSTANTS
version = config.get_version()


def get_date() -> str:
    return time.strftime("%d/%m/%Y")


def get_time() -> str:
    return time.strftime("%H:%M:%S")
s

# stampa un messaggio "dati trovati nel qr" e li visualizza a schermo
def show_qr_data() -> None:
    dec.pretty("QREAD_DATA_QR", color="green")
    dec.pretty(f"\n  {img.get_data()}\n", mymsg=True, input=True, color="cyan")


# data una stringa identifica se è un link o meno, in caso l'utente inserisca 't' in input il link varrà aperto
def link_menu(link: str) -> None:
    if vl.url(link):
        user_input = dec.pretty("QREAD_IS_LINK", input=True, clear=True)
        match user_input:
            case 'Y':
                io.open_link(link)


""" # data una stringa la divide per ogni occorrenza di "," e ne crea una tuple, che restituisce, se l'operazione fallisce, crea un LOG
def to_int_tuple(string: str) -> tuple:
    try:
        return tuple([int(x) for x in string.split(",")])
    except ValueError as error:
        generate_log(error) """


# aggiorna il file di configurazione e, se l'operazione ha successo, visualizza a video un messaggio di aggiornamento
def update_config() -> bool:
    if config.update_file():
        dec.pretty("MSG_UPDATE", color="magenta", clear=True)
        return True
    return False


# data una stringa che identifica un parametro del file di conf, e dato il rispettivo valore, chiede all'utente
# un nuovo valore per il parametro (include messaggi di aggiornamento a schermo)
def get_new_parameter(parameter: str, value: any) -> str:
    dec.pretty("MSG_VALID_INPUT", color="green", clear=True)
    dec.pretty("SETT_CONFIGURATION", color="cyan")
    dec.pretty(config.get_pretty_conf(), mymsg=True)

    return dec.pretty(f"\n REDEFINE → {parameter}({value}): ", color="cyan", input=True, mymsg=True)


"""
,
    "QR_STYLES": {
        "APP": {
            "fill": {
                "r": 0,
                "g": 0,
                "b": 0
            },
            "back": {
                "r": 37,
                "g": 147,
                "b": 229
            }
        },
        "BASIC": {
            "fill": {
                "r": 0,
                "g": 0,
                "b": 0
            },
            "back": {
                "r": 255,
                "g": 255,
                "b": 255
            }
        }
    }
    """
