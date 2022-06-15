from dataclasses import dataclass
import os
import json
import time
import utility as uti
from color_class import Color
from decorations import Decoration

@dataclass
class Configuration:
    # posizione del file .exe di NextQR
    EXE_LOCATION = os.path.dirname(os.path.realpath(__file__))
    # posizione del file di configurazione delle impostazioni di NextQR
    CONF_LOCATION = f"{EXE_LOCATION}\\next_qr.json"
    conf = None


    # costruttore della classe Configuration
    def __init__(self) -> None:
        try:
            with open(self.CONF_LOCATION, "r") as file:
                self.conf = json.load(file)
        except FileNotFoundError as error:
            uti.generate_log(error)

    # incrementa il contatore del numero di volte in cui è stata eseguita l'applicazione
    def new_launch(self) -> int:
        self.conf["APP"]["launches"] += 1
        self.update_file()
        return self.conf["APP"]["launches"]

    # restituisce la costante EXE_LOCATION
    def get_exe_location(self) -> str:
        return self.EXE_LOCATION

    # restituisce la costante CONF_LOCATION
    def get_conf_location(self) -> str:
        return self.CONF_LOCATION

    # restituisce i dati contenuti nella variabile "conf" presi dal file di configurazione
    def get_conf(self) -> dict:
        return self.conf

    # restituisce la configurazione con indentazione di 4 spazi
    def get_pretty_conf(self) -> str:
        return json.dumps(self.conf, indent=4)

    # restituisce la versione corrente dell'applicazione
    def get_version(self) -> str:
        return self.conf["APP"]["version"]

    # restituisce il colore di foreground dei QR generati
    def get_fill_color(self) -> Color:
        return Color(self.conf["QR"]["fill_color"])

    # restituisce il colore di background dei QR generati
    def get_back_color(self) -> Color:
        return Color(self.conf["QR"]["back_color"])

    # restituisce la dimensione del logo inserito nei QR
    def get_logo_dim(self) -> int:
        return int(self.conf["QR"]["logo_dim"])

    # restituisce il percorso della directory in cui vengono salvati i file di uscita
    def get_out_dir(self) -> str:
        return self.conf["APP"]["output_directory"]

    # restituisce il percorso della directory da cui vengono leggi i file
    def get_input_dir(self) -> str:
        return self.conf["APP"]["input_directory"]

    # restituisce la larghezza della console dell'applicazione
    def get_console_width(self) -> str:
        return self.conf["APP"]["console_width"]

    # restituisce l'altezza della console dell'applicazione
    def get_console_lines(self) -> str:
        return self.conf["APP"]["console_lines"]

    # restituisce il nome dell'applicazione
    def get_app_name(self) -> str:
        return self.conf["APP"]["name"]

    # restituisce se quando si legge un qr i dati dello stream video vengono mostrati a schermo o meno
    def get_camera(self) -> bool:
        return self.conf["CAMERA"]["show_camera"]

    # imposta il colore di riempimento dei QR
    def set_fill_color(self, color: Color) -> bool:
        if type(color) is not Color:
            return False

        self.conf["QR"]["fill_color"] = color.rgb()
        return True

    # imposta il colore di background dei QR
    def set_back_color(self, color: Color) -> bool:
        if type(color) is not Color:
            return False

        self.conf["QR"]["back_color"] = color.rgb()
        return True

    # imposta la directory in cui vengono salvati i file
    def set_out_dir(self, path: str) -> bool:
        try:
            if path != "":
                if os.path.isdir(path) is False:
                    return False
            self.conf["APP"]["output_directory"] = path
            return True
        except ValueError as error:
            uti.generate_log(error)
            return False

    # imposta la directory da cui vengono letti i file
    def set_input_dir(self, path) -> bool:
        try:
            if path != "":
                if os.path.isdir(path) is False:
                    return False
            self.conf["APP"]["input_directory"] = path
            return True
        except ValueError as error:
            uti.generate_log(error)
            return False

    # imposta la dimensione del logo che viene inserito nei QR
    def set_logo_dim(self, dim: int) -> bool:
        if dim in range(0, 91):
            self.conf["QR"]["logo_dim"] = dim
            return True
        return False

    # imposta la larghezza della console dell'applicazione
    def set_console_width(self, width: int) -> bool:
        if width in range(20, 151):
            self.conf["APP"]["console_width"] = width
            return True
        return False

    # imposta l'altezza della console dell'applicazione
    def set_console_lines(self, lines: int) -> bool:
        if lines in range(20, 61):
            self.conf["APP"]["console_lines"] = lines
            return True
        return False

    # aggiorna la data e l'ora in cui il file di configurazione è stato modificato l'ultima volta
    def set_last_modify(self) -> str:
        self.conf["APP"]["last_modify"] = f"{time.strftime('%d/%m/%Y')}-{time.strftime('%H:%M:%S')}"

    # imposta se mostrare la camera durante la lettura di QR
    def set_camera(self, set: bool) -> bool:
        if type(set) is not bool:
            return False
        self.conf["CAMERA"]["show_camera"] = set
        return True
    
    # stampa a video la configurazione corrente
    def show_conf(self) -> None:
        dec = Decoration()
        dec.pretty("SETT_CONFIGURATION", color="cyan")
        dec.pretty(self.get_pretty_conf(), mymsg=True)

    # aggiorna il file di configurazione
    def update_file(self) -> bool:
        self.set_last_modify()
        try:
            with open(self.CONF_LOCATION, "r+") as file:
                file.seek(0)
                json.dump(self.conf, file, indent=4)
                file.truncate()
            return True
        except PermissionError as error:
            uti.generate_log(error)
        return False

    """ def is_color(self, color: tuple) -> bool:
        if type(color) is Color:
            return True
            
        if len(color != 3):
            return False

        for x in color:
            if x not in range(0, 256):
                return False
        return True """

    # reimposta il file di configurazione con le impostazioni di base
    def reset(self) -> None:
        self.set_out_dir("")
        self.set_input_dir("")
        self.set_fill_color(Color(0, 0, 0))
        self.set_back_color(Color(37, 147, 229))
        self.set_logo_dim(60)
        self.set_console_width(80)
        self.set_console_lines(42)
        self.set_camera(True)
        self.update_file()
