
# stampa un messaggio "dati trovati nel qr" e li visualizza a schermo
def show_qr_data() -> None:
    dec.pretty("QREAD_DATA_QR", color="green")
    dec.pretty(f"\n  {img.get_data()}\n", mymsg=True, input=True, color="cyan")




""" # data una stringa la divide per ogni occorrenza di "," e ne crea una tuple, che restituisce, se l'operazione fallisce, crea un LOG
def to_int_tuple(string: str) -> tuple:
    try:
        return tuple([int(x) for x in string.split(",")])
    except ValueError as error:
        generate_log(error) """


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
