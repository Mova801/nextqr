import os
import re
import json
import time
import ctypes
from configparser import ConfigParser

import webbrowser as wb

from dataclasses import dataclass
from termcolor import cprint

DESKTOP: str = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# lib info
__email__: str = "imova2882@gmail.com"
__version__: str = "0.4.0"
__author__: str = "Mova801"


def ExceptionsHandler(func):
    def wrapper(*args, **kwargs):
        cls = args[0]
        try:
            message = None
            func(*args, **kwargs)
        except FileNotFoundError as error:
            message = error
        except TypeError as error:
            message = error
        except json.JSONDecodeError as error:
            message = error
        if cls._debug and message is not None:
            cprint(message, "red")
        return cls
    return wrapper


@dataclass
class File:
    _path: str
    _mode: str
    _filename: str
    _data: any
    _encoding: str
    _readlines: str
    _readline: str
    _debug: bool = False

    def __init__(self, filename: str, **kwargs: any):
        self._path = kwargs.get("path", "")
        self._mode = kwargs.get("mode", "w")
        self._filename = IOstream.invalid_char(filename)
        self._data = kwargs.get("data", "")
        self._encoding = kwargs.get("encoding", None)
        self._debug = kwargs.get("debug", False)
        self._readlines = kwargs.get("readlines", False)
        self._readline = kwargs.get("readline", False)

    # legge la prima riga di un file
    @ExceptionsHandler
    def read(self):
        path: str = IOstream.join_path(self._path, self._filename)
        with open(path, self._mode, encoding=self._encoding) as f:
            if self._readlines:
                self._data = f.readlines()
            elif self._readline:
                self._data = f.readline()
            else:
                self._data = f.read()
        return self

    # crea un file e ci scrive dentro i dati presenti nell'istanza File corrente (<=)
    @ExceptionsHandler
    def write(self, data: str = None):
        if data is None:
            data = self._data
        path: str = IOstream.join_path(self._path, self._filename)
        # if file.mode == "wb":
        #     if not isinstance(path, bytes):
        #         file.data = bytes(file.data)
        data = self._data
        with open(path, self._mode, encoding=self._encoding) as f:
            if isinstance(data, list):
                f.writelines(data)
            else:
                f.write(data)
        return self

    # aggiunge dati ai vecchi dati presenti nella variabile "data" di "File" (__le__ equivale a <=)
    def __le__(self, string: str):
        self._data += string
        return self

    # sovrascrive i vecchi dati presenti nella variabile "data" di "File" (__ilshift__ equivale a <<=)
    def __ilshift__(self, string: str):
        self._data = string
        return self

    def get_data(self) -> any:
        return self._data

    def get_filename(self) -> str:
        return self._filename

    def set_filename(self, filename: str) -> None:
        self._filename = IOstream.invalid_char(filename)

    def set_mode(self, mode: str) -> bool:
        match mode:
            case 'r' | 'w' | 'wb' | 'rb' | 'r+' | 'a':
                self._mode = mode
                return True
            case _:
                return False

    def set_data(self, data: any) -> None:
        if type(data) is str or dict or tuple or list or set:
            self._data = data


class JSONFile(File):
    def __init__(self, filename: str, **kwargs: any):
        super().__init__(filename, **kwargs)

    # legge un file json, ne legge i dati e li salva in un istanza File
    @ExceptionsHandler
    def read(self):
        path: str = IOstream.join_path(self._path, self._filename)
        with open(path, 'r', encoding=self._encoding) as f:
            self._data = json.load(f)
        return self

    # crea un file json e ci scrive dentro i dati presenti nell'istanza File corrente
    @ExceptionsHandler
    def write(self, data: str = None):
        if data is None:
            data = self._data
        path: str = IOstream.join_path(self._path, self._filename)
        with open(path, 'w', encoding=self._encoding) as f:
            json.dump(self._data, f, indent=4)
        return self


# Log class inherit from File
#   a Log is a File which create 2 directories and a file in append mode
#       dir 1: contains the daily logs directories
#       dir 2: daily directory (every day a new one is generated)
#   in the log file are stored data
#
#   [!]: each time new informations are added the log write on file!

class Log(File):
    _log_dir_1: str
    _log_dir_2: str
    _log_path: str

    def __init__(self, filename: str, **kwargs: dict) -> None:
        self._log_dir_1 = IOstream.invalid_char(kwargs.get("dir1", "LOG"))
        self._log_dir_2 = IOstream.invalid_char(
            kwargs.get("dir2", f"log_{IOstream.get_date()}"))
        IOstream.mkdir(self._log_dir_1)
        log_path = IOstream.join_path(self._log_dir_1, self._log_dir_2)
        IOstream.mkdir(log_path)

        super().__init__(filename + ".log", mode='a', path=log_path)

    def log(self, data: str = None):
        if data is None:
            data = self._data
        self._data = f"[{IOstream.get_date()} - {IOstream.get_time()}] {data}\n"
        self.write()


class Configuration(ConfigParser):
    _path: str
    _debug: bool

    def __init__(self, filename: str = "", **kwargs: dict) -> None:
        self._path = kwargs.get("path", "")
        self._filename = IOstream.join_path(
            self._path, IOstream.invalid_char(filename))
        self._debug = kwargs.get("debug", False)
        return super().__init__()

    @ExceptionsHandler
    def load(self, filename: str):
        self._filename = IOstream.join_path(self._path, filename)
        self.read(self._filename)
        return self

    @ExceptionsHandler
    def save(self):
        with open(self._filename, 'w') as cf:
            self.write(cf)
        return self


@dataclass
class IOstream:
    def __init__(self, debug=None):
        if debug is None:
            self._debug = False
        else:
            self._debug = True

    @classmethod
    def get_login(cls) -> str:
        return os.getlogin()

    @classmethod
    def get_date(cls, div=".") -> str:
        return time.strftime(f"%d{div}%m{div}%Y")

    @classmethod
    def get_time(cls, div=":") -> str:
        return time.strftime(f"%H{div}%M{div}%S")

    @classmethod
    def mkdir(cls, path: str) -> bool:
        """create a new folder in the given path"""
        try:
            os.mkdir(path)
            return True
        except FileExistsError:
            return False

    @classmethod
    def mkdirs(cls, path: str) -> bool:
        """create a new folder in the given path"""
        try:
            directories = path.split("\\")
            path = ""
            for dir in directories:
                path = IOstream.join_path(path, dir)
                IOstream.mkdir(path)
            return True
        except FileExistsError:
            return False

    @classmethod
    def open_link(cls, link: str) -> None:
        """apre il link passato"""
        wb.open(link)

    @classmethod
    def join_path(cls, path1: str, path2: str) -> str:
        """unisce due percorsi e restituisce un singolo percorso (unione dei due)"""
        return os.path.join(path1, path2)

    @classmethod
    def clear_terminal(cls) -> None:
        """pulisce il terminale"""
        os.system('cls')

    @classmethod
    def invalid_char(cls, string: str) -> str:
        """controlla se nella stringa passata sono presenti caratteri invalidi per il nome di un file"""
        if string == "":
            return ""
        inv: list = [r'\\', r'\/', r'\:', r'\*',
                     r'\?', r'\"', r'\<', r'\>', r'\|']
        for char in inv:
            string = re.sub(char, "", string)
        return string

    @classmethod
    def update_terminal(cls, **kwargs: any) -> None:
        """aggiorna le impostazioni della console"""
        name: str = kwargs.get("name", "Console")
        cols: str = kwargs.get("cols", 50)
        lines: str = kwargs.get("lines", 20)

        # modifica il nome della console e lo imposta col nome dell'app nel file di configurazione
        ctypes.windll.kernel32.SetConsoleTitleW(name)
        # modifica la dimensione della console (colonne e linee)
        os.system(f"mode con cols={cols} lines={lines}")