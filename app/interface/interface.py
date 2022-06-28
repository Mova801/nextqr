from asyncio import events
import PySimpleGUI as sg

BUILD = "build7.0.0.26.06.2022"


def build_layout():
    first_row = [
        [sg.Text("NextQR v7.0.0")],
    ]

    generate = [
        [sg.In("Enter QR name", text_color="gray", size=(800))],
        [sg.Multiline("Enter QR text", text_color="gray", size=(800, 10))],

        [sg.Button("Generate", button_color="#4FFFBE", mouseover_colors="#FF4297"),
         sg.Button("Cancel", button_color="#4FFFBE", mouseover_colors="#FF4297")]
    ]

    read = [
        [sg.Text("WIP")]
    ]

    second_row = [
        sg.TabGroup(
            [
                [
                    sg.Tab('Generate', layout=generate),
                    sg.Tab('Read', layout=read)
                ]
            ]
        )
    ]

    build_info_row = [
        [
            sg.VPush(),
            sg.Text(BUILD, font="italic 8")
        ]
    ]

    layout = [
        [first_row],
        [second_row],
        [build_info_row]
    ]

    return layout


def build():
    layout = build_layout()
    window = sg.Window(title="NextQR", layout=layout,
                       size=(800, 600), finalize=True)
    while True:
        event, values = window.read()

        if event == "-QUIT-" or sg.WIN_CLOSED:
            break


if __name__ == "__main__":
    build()
