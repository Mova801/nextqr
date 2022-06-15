from dataclasses import dataclass

@dataclass
class Color:
    r: int = None
    g: int = None
    b: int = None

    # costruttore della classe colore
    def __init__(self, *color: list) -> None:
        # 
        if len(color) == 1:
            color = color[0]
            if type(color) is Color:
                self.r, self.g, self.b = color.rgb()
            elif type(color) is list or type(color) is tuple or type(color) is set:
                self.r, self.g, self.b = tuple(color)
            elif type(color) is str:
                self.r, self.g, self.b = self.to_int_tuple(color)

        elif len(color) == 3:
            self.r = color[0]
            self.g = color[1]
            self.b = color[2]      

        else:
            self.r, self.g, self.b = 0

    def to_int_tuple(self, string: str) -> tuple:
        try:
            if string.startswith("(") and string.endswith(")"):
                string = string[1:-1]
                return tuple([int(x) for x in string.split(",")])
            else:
                return None
        except:
            return (0,0,0)
            

    def __rshift__(self, other: object) -> object:
        other.set_color(self.red(), self.green(), self.blue())
        return other

    def __lshift__(self, *val) -> object:
        if type(val[0]) is str:
            val = self.to_int_tuple(val[0])
            if val is None:
                return None

        if len(val) == 1:
            self.r, self.g, self.b = val[0]

        elif len(val) == 3:
            self.r = val[0]
            self.g = val[1]
            self.b = val[2]      

        else:
            self.r, self.g, self.b = 0
        
        return (self.r, self.g, self.b)
    

    def __str__(self) -> str:
        return f"({self.r},{self.g},{self.b})"
        #f"({colored(self.r, 'red')},{colored(self.g, 'green')},{colored(self.b, 'blue')})"

    def __add__(self, other: object) -> object:
        sum = [self.red()+other.red(), self.green()+other.green(), self.blue()+other.blue()]
        for i in range(len(sum)):
            if sum[i] not in range(0, 256):
                sum[i] = 255
        return Color(sum)

    def __sub__(self, other: object) -> object:
        sub = [self.red()-other.red(), self.green()-other.green(), self.blue()-other.blue()]
        for i in range(len(sub)):
            if sub[i] not in range(0, 256):
                sub[i] = 0
        return Color(sub)


    def red(self) -> int:
        return self.r

    def green(self) -> int:
        return self.g

    def blue(self) -> int:
        return self.b

    def rgb(self) -> tuple:
        return tuple((self.r, self.g, self.b))

    def set_color(self, color: tuple) -> None:
        for i in range(len(color)):
            if i not in range(0, 256):
                sum[i] = 0
        self.r, self.g, self.b = color

    def set_color(self, r: int, g: int, b: int) -> None:
        color = [r,g,b]
        for i in range(len(color)):
            if i not in range(0, 256):
                sum[i] = 0
        self.r, self.g, self.b = color