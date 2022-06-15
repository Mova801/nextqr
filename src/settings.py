import utility as uti
from utility import dec, config, io
from color_class import Color

def main() -> None:
    io.clear_terminal()
    if dec.pretty(" [::] ", color="magenta", mymsg=True, input=True, clear=True) != config.get_version()[:4]:
        io.clear_terminal()
        return
    try:
        max_page = 2
        page = 1
        while True:
            #dec.pretty("CURRENT_PAGE", color="green", clear=True, format=[page, max_page])
            dec.pretty(f"SETT_MENU_PAG{page}", format=[page, max_page])

            menu_input = dec.pretty(
                " ► ", color="magenta", input=True, mymsg=True)

            # options
            match menu_input:
                # opzione che torna al menu precedente
                case "-":
                    break

                # opzione che scorre alla pagina successiva
                case ">":
                    if page in range(1, max_page):
                        page += 1
                        io.clear_terminal()
                        continue

                # opzione che scorre alla pagina precedente
                case "<":
                    if page in range(2, max_page+1):
                        page -= 1
                        io.clear_terminal()
                        continue

                # opzione che  resetta il file di configurazione
                case "opt:reset":
                    dec.pretty("MSG_VALID_INPUT", color="green", clear=True)
                    dec.pretty("SETT_RESET", color="yellow")
                    config.reset()
                    uti.update_config()
                    continue
                    # exe_path = io.join_path(config.get_exe_location(), "starter.py")
                    # os.system(exe_path)
                    # exit()

                # opzione che mostra le impostazioni correnti
                case "opt:show":
                    dec.pretty("MSG_VALID_INPUT", color="green", clear=True)
                    config.show_conf()
                    dec.pretty("\n ► press 'Enter[←]' to continue ", mymsg=True, color="magenta", input=True, clear=True)
                    continue

                # opzione per impostare il colore di riempimento del QR
                case "qr:fill":
                    fill_color = Color(config.get_fill_color())
                    fill_color << uti.get_new_parameter("qr_fill", fill_color)
                    config.set_fill_color(fill_color)
                    uti.update_config()
                    config.show_conf()
                    dec.pretty("\n ► press 'Enter[←]' to continue ", mymsg=True, color="magenta", input=True, clear=True)
                    continue

                # opzione per impostare il colroe di background del QR
                case "qr:back":
                    back_color = Color(config.get_back_color())
                    back_color << uti.get_new_parameter("qr_back", back_color)
                    config.set_back_color(back_color)
                    uti.update_config()
                    config.show_conf()
                    dec.pretty("\n ► press 'Enter[←]' to continue ", mymsg=True, color="magenta", input=True, clear=True)
                    continue

                # opzione per impostare la dimensione del logo del QR
                case "qr:logo":
                    dim_logo = config.get_logo_dim()
                    new_value = uti.get_new_parameter("logo_dim", dim_logo)
                    try:
                        new_value = int(new_value)
                    except ValueError as error:
                        uti.generate_log(error)

                    if config.set_logo_dim(new_value):
                        uti.update_config()
                        config.show_conf()
                        dec.pretty("\n ► press 'Enter[←]' to continue ", mymsg=True, color="magenta", input=True, clear=True)
                        continue

                
                case "app:outpath":
                    path = config.get_out_dir()
                    new_value = uti.get_new_parameter("output_directory", path)
                    if config.set_out_dir(new_value):
                        uti.update_config()
                        config.show_conf()
                        dec.pretty("\n ► press 'Enter[←]' to continue ", mymsg=True, color="magenta", input=True, clear=True)
                        continue

                case "app:inpath":
                    path = config.get_input_dir()
                    new_value = uti.get_new_parameter("input_directory", path)
                    if config.set_input_dir(new_value):
                        uti.update_config()
                        config.show_conf()
                        dec.pretty("\n ► press 'Enter[←]' to continue ", mymsg=True, color="magenta", input=True, clear=True)
                        continue

                case "app:cwidth":
                    width = config.get_console_width()
                    new_value = uti.get_new_parameter("cwidth", width)
                    try:
                        new_value = int(new_value)
                    except ValueError as error:
                        uti.generate_log(error)

                    if config.set_console_width(new_value):
                        uti.update_config()
                        dec.pretty("APP_RESTART", color="cyan")
                        # exe_path = io.join_path(config.get_exe_location(), "starter.py")
                        # os.system(exe_path)
                        # exit()
                        continue

                case "app:clines":
                    lines = config.get_console_lines()
                    new_value = uti.get_new_parameter("clines", lines)
                    try:
                        new_value = int(new_value)
                    except ValueError as error:
                        uti.generate_log(error)

                    new_value = int(new_value)
                    if config.set_console_lines(new_value):
                        uti.update_config()
                        dec.pretty("APP_RESTART", color="cyan")
                        # exe_path = io.join_path(config.get_exe_location(), "starter.py")
                        # os.system(exe_path)
                        # exit()
                        continue

                case "cam:showcam":
                    show = config.get_camera()
                    new_value = uti.get_new_parameter("camera", show)
                    match new_value:
                        case "True"|"true":
                            new_value = True
                        case "False"|"false":
                            new_value = False
                    if config.set_camera(new_value):
                        uti.update_config()
                        config.show_conf()
                        dec.pretty("\n ► press 'Enter[←]' to continue ", color="magenta", mymsg=True, input=True, clear=True)
                        continue                  

            dec.pretty("ERR_INV_INPUT", color="red", clear=True)

        io.clear_terminal()
        return True

    except FileNotFoundError as error:
            uti.generate_log(error)
    except PermissionError as error:
            uti.generate_log(error)
    io.clear_terminal()
    return False


if __name__ == "__main__":
    main()
