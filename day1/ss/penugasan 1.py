import PySimpleGUI as sg

sg.theme('LightBlue')

layout = [
    [sg.Text('PROGRAM KASIR', font=('Arial', 16))],

    [sg.Text('Nama Barang', size=(12, 1)), sg.Input(key='-NAMA-')],
    [sg.Text('Harga', size=(12, 1)), sg.Input(key='-HARGA-')],
    [sg.Text('Jumlah', size=(12, 1)), sg.Input(key='-JUMLAH-')],

    [sg.Button('Hitung'), sg.Button('Reset'), sg.Button('Exit')],

    [sg.HorizontalSeparator()],

    [sg.Text('Total Bayar', size=(12, 1)), sg.Text('Rp 0', key='-TOTAL-', font=('Arial', 12))]
]

window = sg.Window('Kasir Sederhana', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Hitung':
        try:
            harga = int(values['-HARGA-'])
            jumlah = int(values['-JUMLAH-'])
            total = harga * jumlah
            window['-TOTAL-'].update(f'Rp {total}')
        except:
            sg.popup('Masukkan harga dan jumlah dengan benar!')

    if event == 'Reset':
        window['-NAMA-'].update('')
        window['-HARGA-'].update('')
        window['-JUMLAH-'].update('')
        window['-TOTAL-'].update('Rp 0')

window.close()