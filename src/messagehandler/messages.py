from termcolor import colored

version = "b3.6.05032022"  # conf.get_version()

APP_INFO = f""" ╔{"═" * len(version)}═════════════════════════════════════╗
 ║ NextQR Generator&Reader - version: {version} ║
 ╚{"═" * len(version)}═════════════════════════════════════╝"""

APP_DEV = f""" ╔════════════════════════════════╗
 ║       Developer Contacts       ║
 ╠════════════════════════════════╣
 ║ mail: marco.vita2222@gmail.com ║
 ║ github: Mova811                ║
 ╚════════════════════════════════╝"""

APP_START = """ ╔═══════════════════════════╗
 ║ PRESS 'Enter[←]' TO START ║
 ╚═══════════════════════════╝"""

APP_RESTART = """ ╔═════════════════════════════════════════════╗
 ║ RESTART THE APP TO LOAD NEW WINDOW SETTINGS ║
 ╚═════════════════════════════════════════════╝"""

### APP START MENU ###

APP_MENU = f""" ╔════════════════════════╗
 ║ [{colored("-", "red")}]      Menu          ║
 ╠════════════════════════╣
 ║ [{colored("+", "green")}] → Generate QR      ║
 ║ [{colored("#", "cyan")}] → Scan QR          ║
 ║ [{colored("*", "magenta")}] → Edit Settings    ║
 ║ [{colored("o", "yellow")}] → Visit Dev GitHub ║
 ╚════════════════════════╝

 {colored('►', 'cyan')} """

### QR GENERATION MESSAGES ###

### --- ###

QGEN_START = """
 ╔═════════════════════╗
 ║    QR Generation    ║
 ╠═════════════════════╝"""

QGEN_NEW_QR = """ ╔═══════════════════════════════════════════╗
 ║ New QR generated! Check your main folder! ║
 ╚═══════════════════════════════════════════╝"""

### INPUT ###

QGEN_ENTER_NAME = f" {colored('╠', 'cyan')} Enter the {colored('name', 'red')} of the QR code: "

QGEN_ENTER_DATA = f" {colored('╠', 'cyan')} Enter the {colored('text', 'red')} you want to insert in the QR code: "

QGEN_ENTER_LOGO = f" {colored('╚', 'cyan')} Enter the {colored('.png', 'red')} file you want to use as QR logo (if not, leave it blank): "

### ERRORS ###

QGEN_ERR_QR = """ ╔════════════════════════════╗
 ║ Unable to generate the QR. ║
 ╚════════════════════════════╝
 """


### QR READING MESSAGES ###

### --- ###

QREAD_MENU = f""" ╔═════════════════════════════════╗
 ║ [{colored("-", "red")}]   Select Input Method       ║
 ╠═════════════════════════════════╣
 ║ [{colored("c", "cyan")}] → Camera                    ║
 ║ [{colored("f", "red")}] → File                      ║
 ╚═════════════════════════════════╝

  {colored('►', 'cyan')} """

QREAD_START = """
 ╔═══════════════╗
 ║    QR Read    ║
 ╠═══════════════╝"""

QREAD_DETECTING = """ ╔═════════════════╗
 ║ DETECTING QR... ║
 ╚═════════════════╝"""

### INPUT ###

QREAD_ENTER_QR = f" {colored('╠', 'cyan')} Enter the file to {colored('scan', 'red')}: "

QREAD_DATA_QR = f" {colored('╠', 'cyan')} {colored('Data', 'red')} found: "

QREAD_SAVE_DATA = f" {colored('╠', 'cyan')} {colored('Save', 'red')} data found [{colored('Y', 'green')}|{colored('n', 'red')}]: "

QREAD_IS_LINK = f" {colored('╚', 'cyan')} {colored('Open', 'red')} link [{colored('Y', 'green')}|{colored('n', 'red')}]: "

### ERRORS ###

QREAD_ERR_FILE = """ ╔════════════════╗
 ║ file not found ║
 ╚════════════════╝"""

QREAD_ERR_QR = """ ╔═════════════╗
 ║ no qr found ║
 ╚═════════════╝"""


### APP CONFIGURATION MESSAGES ###

SETT_CONFIGURATION = """ ╔═════════════════════╗
 ║ QRgen CONFIGURATION ║
 ╚═════════════════════╝
 """

SETT_MENU_PAG1 = f""" ╔════════════════════════════════════════════════════════════════╗
 ║ [{colored("-", "red")}]                 {colored("Edit Settings Menu", "magenta")}            PAGE 1|2 [{colored(">", "blue")}] ║
 ╠════════════════════════════════════════════════════════════════╣
 ║ [{colored("app:", "cyan")}{colored("outpath", "green")}] → Output Folder   [{colored("qr:", "cyan")}{colored("fill", "green")}] → Fill QR Color      ║
 ║ [{colored("app:", "cyan")}{colored("inpath", "green")}]  → Input Folder    [{colored("qr:", "cyan")}{colored("back", "green")}] → Back QR Color      ║
 ║ [{colored("opt:", "cyan")}{colored("show", "green")}]    → Show Settings   [{colored("qr:", "cyan")}{colored("logo", "green")}] → Logo QR Dimension  ║
 ╚════════════════════════════════════════════════════════════════╝
 """

SETT_MENU_PAG2 = f""" ╔════════════════════════════════════════════════════════════════╗
 ║ [{colored("-", "red")}]                 {colored("Edit Settings Menu", "magenta")}            PAGE 2|2 [{colored("<", "blue")}] ║
 ╠════════════════════════════════════════════════════════════════╣
 ║ [{colored("app:", "cyan")}{colored("cwidth", "green")}] → Console Width   [{colored("cam:", "cyan")}{colored("showcam", "green")}] → Console Width   ║
 ║ [{colored("app:", "cyan")}{colored("clines", "green")}] → Console Lines                                   ║
 ║ [{colored("opt:", "cyan")}{colored("reset", "green")}]  → Reset Config                                    ║
 ╚════════════════════════════════════════════════════════════════╝
 """

### OPTIONS OUTCOMES ###

SETT_RESET = """ ╔═════════════════════╗
 ║ CONFIGURATION RESET ║
 ╚═════════════════════╝"""

### OPERATION OUTCOME ###

### POSITIVE ###

MSG_VALID_INPUT = """ ╔═════════════╗
 ║ valid input ║
 ╚═════════════╝"""

MSG_UPDATE = """ ╔═════════════════╗
 ║ updated options ║
 ╚═════════════════╝"""

### OTHER ERRORS ###

ERR_INV_INPUT = """ ╔═══════════════╗
 ║ invalid input ║
 ╚═══════════════╝"""

ERR_INV_LOGO = """
 ╔═════════════════════╗
 ║ logo file not found ║
 ╚═════════════════════╝"""

ERR_INV_CHARS = """ ╔══════════════════════════════════╗
 ║ invalid chars → \ /: * ? " < > | ║
 ╚══════════════════════════════════╝"""

ERR_INTERNAL = """ ╔════════════════╗
 ║ INTERNAL ERROR ║
 ╚════════════════╝"""

ERR_INV_PATH = """ ╔════════════╗
 ║ PATH ERROR ║
 ╚════════════╝"""

ERR_PERMISSION = """
 ╔═══════════════════╗
 ║ permission denied ║
 ╚═══════════════════╝
 """
