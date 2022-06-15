from pynput import keyboard

# lib info
__email__: str = "imova2882@gmail.com"
__version__: str = "0.1.0"
__author__: str = "Mova801"


class KeyboardHandler:
    _listener: keyboard.Listener
    _controller: keyboard.Controller
    _keys: list
    _key_input: any

    def __init__(self, *args) -> None:
        self._listener = keyboard.Listener(on_press=self.on_press)
        self._controller = keyboard.Controller()
        if isinstance(args, (list, tuple, set)):
            self._keys = args[0]
        else:
            self._keys = args
        self._key_input = None
        self._paused = False

    def on_press(self, key):
        if self._paused is False:
            if key is False:
                return False  # stop listener
            try:
                k = key.char  # single-char keys
            except:
                k = key.name  # other keys

            if k in self._keys:  # keys of interest
                #print('Key pressed: ' + k)
                self._key_input = k
                # return False  # stop listeneer; remove this if want more keys

    def press_key(self):
        self._controller.press(keyboard.Key.backspace)
        self._controller.release(keyboard.Key.backspace)

    # start to listen on a separate thread

    def listen(self):
        try:
            self._listener.start()
            self._paused = False
        except RuntimeError as error:
            print(error)

    def update_key_inputs(self, *args):
        self._key_input = args

    def reset_input(self):
        self._key_input = None

    def pause(self):
        self._paused = True

    def unpause(self):
        self._paused = False

    def get_input(self):
        key = self._key_input
        self._key_input = None
        return key

    def stop(self):
        self.on_press(False)
        # self._listener.join()
