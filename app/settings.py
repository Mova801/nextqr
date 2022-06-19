import os

from LIB.messagehandler.message_handler import MessageHandler
from LIB.ios.iostream import IOstream, Configuration, Log
from src.constants import MAX_PAGES
from LIB.exceptionpack.exception_handler import handle_exceptions


@handle_exceptions
def update_parameter(config: Configuration, parameter: str, param_value: any) -> str:
    """
    Data una stringa che identifica un parametro del file di conf, e dato il rispettivo valore, chiede all'utente
    un nuovo valore per il parametro (include messaggi di aggiornamento a schermo)
    """
    msg.clsprint("SETT_CONFIGURATION", color="cyan")
    return msg.myprint(f"{config}\n REDEFINE → {parameter}({param_value}): ", color="cyan", input=True)


# resetta il file di configurazione e, se l'operazione ha successo, visualizza a video un messaggio di aggiornamento
@handle_exceptions
def reset(config: Configuration) -> None:
    config['APP']['output_directory'] = ""
    config['APP']['input_directory'] = ""
    config['QR']['fill_color'] = (0, 0, 0)
    config['QR']['back_color'] = (37, 147, 229)
    config['QR']['logo_dim'] = 60
    config['CONSOLE']['name'] = "NextQR"
    config['CONSOLE']['width'] = 80
    config['CONSOLE']['name'] = "NextQR"
    config['CAMERA']['show_camera'] = "True"

    config['APP']["last_modify"] = IOstream.get_date() + "-" + \
        IOstream.get_time()


def app_settings(msg_: MessageHandler) -> None:
    global msg
    msg = msg_
    config = Configuration()
    config.load("src\\nextqr.ini")
    version = config['APP'].get("version", "")
    # if the right password (current version) is entered then continue else return
    if msg.myprint("@_> ", color="cyan", input=True) != version:
        return

    dir1 = config['APP'].get("directory_1", "logs")
    dir2 = config['QR'].get("directory_2", "log")
    log = Log(f"log[{IOstream.get_time}]", dir1=dir1, dir2=dir2)

    try:
        current_page = 1
        while True:
            msg.print(f"MENU_PAG{current_page}", clear=True)
            menu_input = msg.myprint(" ► ", color="magenta", input=True)

            # options
            match menu_input:
                # opzione che torna al menu precedente
                case "-":
                    break

                # opzione che scorre alla pagina successiva
                case ">":

                    if current_page < MAX_PAGES:
                        current_page += 1
                        continue

                # opzione che scorre alla pagina precedente
                case "<":
                    if current_page > 1:
                        current_page -= 1
                        continue

                # opzione che  resetta il file di configurazione
                case "opt:reset":
                    msg.colprint("SETT_RESET", "yellow")
                    reset(config)
                    config.save()
                    msg.clsprint("MSG_UPDATE", color="magenta")
                    continue
                    # exe_path = io.join_path(config.get_exe_location(), "starter.py")
                    # os.system(exe_path)
                    # exit()

                # opzione che mostra le impostazioni correnti
                case "opt:show":
                    msg.colprint("SETT_CONFIGURATION", "cyan")
                    msg.myprint(
                        f"{config}\n ► press 'Enter[←]' to continue ", color="magenta", clear=True)
                    continue

                # opzione per impostare il colore di riempimento/background del QR
                case "qr:fill" | "qr:back":
                    if menu_input == "qr:fill":
                        color_opt = "fill_color"
                    else:
                        color_opt = "back_color"
                    color = config['QR'].get(color_opt, (0, 0, 0))
                    color = update_parameter(config, color_opt, color)
                    if not isinstance(color, tuple) and len(color) != 3:
                        config['QR'][color_opt] = color
                        config.save()
                    else:
                        msg.print("ERR_INV_INPUT")
                        continue

                    msg.myprint(
                        f"{config}\n ► press 'Enter[←]' to continue ", color="magenta", clear=True)
                    continue

                # opzione per impostare la dimensione del logo del QR
                case "qr:logo":
                    logo_dim = config['QR'].get("logo_dim", 60)
                    try:
                        logo_dim = update_parameter(config, "logo_dim", logo_dim)
                    except ValueError as error:
                        log.log(error)
                        msg.print("ERR_INV_INPUT")
                        continue

                    config.save()
                    msg.myprint(
                        f"{config}\n ► press 'Enter[←]' to continue ", color="magenta", clear=True)
                    continue

                case "app:outpath" | "app:inpath":
                    if menu_input == "app:outpath":
                        dir_opt = "output_directory"
                    else:
                        dir_opt = "input_directory"
                    dir = config['APP'].get(dir_opt, (0, 0, 0))
                    dir = update_parameter(config, dir_opt, dir)
                    if os.path.isdir(dir) or not dir:
                        config['APP'][dir_opt] = dir
                        config.save()
                    else:
                        msg.print("ERR_INV_INPUT")
                        continue

                    msg.myprint(
                        f"{config}\n ► press 'Enter[←]' to continue ", color="magenta", clear=True)
                    continue

                case "app:cwidth" | "app:clines":
                    if menu_input == "app:cwidth":
                        cons_opt = "width"
                    else:
                        cons_opt = "height"
                    cons = config['APP'].get(cons_opt, 65)
                    cons = int(update_parameter(config, f"c{cons_opt}", cons))
                    if isinstance(cons, int):
                        config['APP'][cons_opt] = cons
                        config.save()
                    else:
                        msg.print("ERR_INV_INPUT")
                        continue
                    msg.myprint(
                        f"{config}\n ► press 'Enter[←]' to continue ", color="magenta", clear=True)
                    continue

                case "cam:showcam":
                    cam = config['APP'].get("show_camera", True)
                    try:
                        cam = bool(update_parameter(config, f"c{menu_input}", cam))
                    except ValueError as error:
                        log.log(error)
                        msg.print("ERR_INV_INPUT")
                        continue
                    config['APP']['show_camera'] = cam
                    config.save()
                    msg.myprint(
                        f"{config}\n ► press 'Enter[←]' to continue ", color="magenta", clear=True)
                    continue

            msg.colprint("ERR_INV_INPUT", "red", clear=True)

        return True

    except FileNotFoundError as error:
        log.log(error)
    except PermissionError as error:
        log.log(error)
    IOstream.clear_terminal()
    return False


if __name__ == "__main__":
    app_settings()
