import PySimpleGUI as sg

sg.theme('LightGreen')

layout = [
    [sg.Text('PROGRAM PARKIR', font=('Arial', 16))],

    [sg.Text('No Kendaraan', size=(15, 1)), sg.Input(key='-NOPOL-')],

    [sg.Text('Jenis Kendaraan', size=(15, 1)),
     sg.Radio('Motor', 'JENIS', key='-MOTOR-', default=True),
     sg.Radio('Mobil', 'JENIS', key='-MOBIL-')],

    [sg.Text('Lama Parkir (Jam)', size=(15, 1)), sg.Input(key='-JAM-')],

    [sg.Button('Hitung'), sg.Button('Reset'), sg.Button('Exit')],

    [sg.HorizontalSeparator()],

    [sg.Text('Biaya Parkir', size=(15, 1)),
     sg.Text('Rp 0', key='-TOTAL-', font=('Arial', 12))]
]

window = sg.Window('Parkir Sederhana', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Hitung':
        try:
            jam = int(values['-JAM-'])

            if values['-MOTOR-']:
                tarif = 2000
            else:
                tarif = 5000

            total = jam * tarif
            window['-TOTAL-'].update(f'Rp {total}')
        except:
            sg.popup('Masukkan lama parkir dengan benar!')

    if event == 'Reset':
        window['-NOPOL-'].update('')
        window['-JAM-'].update('')
        window['-TOTAL-'].update('Rp 0')

window.close()