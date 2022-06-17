from dataclasses import dataclass
from json import JSONDecodeError


@dataclass
class ExceptionHandler(Exception):
    _debug: bool

    def __init__(self, debug=False, *args: object) -> None:
        self._debug = debug
        super().__init__(*args)

    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

    @classmethod
    def ExceptionHandle(self, func):
        def wrapper(*args, **kwargs):
            cls = args[0]
            try:
                message = None
                func(*args, **kwargs)
            except FileNotFoundError as error:
                message = error
            except TypeError as error:
                message = error
            except JSONDecodeError as error:
                message = error
            if  self._debug and message is not None:
                print(message, "red")
            return cls
        return wrapper
