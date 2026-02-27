import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menghitung biaya parkir
def hitung_parkir():
    try:
        plat = entry_plat.get()
        jenis = combo_jenis.get()
        jam_masuk = float(entry_masuk.get())
        jam_keluar = float(entry_keluar.get())
        
        if jam_keluar < jam_masuk:
            messagebox.showerror("Error", "Jam keluar tidak boleh kurang dari jam masuk")
            return

        lama_parkir = jam_keluar - jam_masuk
        
        # Tarif: Mobil 5000/jam, Motor 2000/jam
        if jenis == "Mobil":
            tarif = 5000
        else:
            tarif = 2000
            
        total_bayar = lama_parkir * tarif
        
        # Tampilkan hasil
        lbl_hasil.config(text=f"Plat: {plat}\nJenis: {jenis}\nLama: {lama_parkir} Jam\nTotal: Rp {total_bayar:,}")
        
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan angka valid untuk jam")

# Setup GUI
root = tk.Tk()
root.title("Program Parkir Sederhana")
root.geometry("300x400")

# Input Field
tk.Label(root, text="SISTEM PARKIR", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Plat Nomor:").pack()
entry_plat = tk.Entry(root)
entry_plat.pack()

tk.Label(root, text="Jenis Kendaraan:").pack()
combo_jenis = tk.StringVar(root)
combo_jenis.set("Motor") # default
tk.OptionMenu(root, combo_jenis, "Motor", "Mobil").pack()

tk.Label(root, text="Jam Masuk:").pack()
entry_masuk = tk.Entry(root)
entry_masuk.pack()

tk.Label(root, text="Jam Keluar:").pack()
entry_keluar = tk.Entry(root)
entry_keluar.pack()

# Tombol Hitung
btn_hitung = tk.Button(root, text="Hitung Biaya", command=hitung_parkir, bg="blue", fg="white")
btn_hitung.pack(pady=15)

# Label Hasil
lbl_hasil = tk.Label(root, text="", font=("Arial", 10, "bold"), fg="green")
lbl_hasil.pack()

root.mainloop()