import PySimpleGUI as sg

sg.theme('LightBlue')

layout = [
    [sg.Text('PROGRAM DATA SISWA', font=('Arial', 16))],

    [sg.Text('NIS', size=(12, 1)), sg.Input(key='-NIS-')],
    [sg.Text('Nama', size=(12, 1)), sg.Input(key='-NAMA-')],
    [sg.Text('Kelas', size=(12, 1)),
     sg.Combo(['X', 'XI', 'XII'], key='-KELAS-', readonly=True)],
    [sg.Text('Nilai', size=(12, 1)), sg.Input(key='-NILAI-')],

    [sg.Button('Simpan'), sg.Button('Reset'), sg.Button('Exit')],

    [sg.HorizontalSeparator()],

    [sg.Text('Data Siswa:', font=('Arial', 12))],
    [sg.Multiline(size=(40, 5), key='-OUTPUT-', disabled=True)]
]

window = sg.Window('Data Siswa', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Simpan':
        try:
            nis = values['-NIS-']
            nama = values['-NAMA-']
            kelas = values['-KELAS-']
            nilai = float(values['-NILAI-'])

            data = (
                f"NIS   : {nis}\n"
                f"Nama  : {nama}\n"
                f"Kelas : {kelas}\n"
                f"Nilai : {nilai}\n"
                "--------------------------\n"
            )

            window['-OUTPUT-'].update(data, append=True)
        except:
            sg.popup('Pastikan semua data diisi dengan benar!')

    if event == 'Reset':
        window['-NIS-'].update('')
        window['-NAMA-'].update('')
        window['-KELAS-'].update('')
        window['-NILAI-'].update('')
        window['-OUTPUT-'].update('')

window.close()