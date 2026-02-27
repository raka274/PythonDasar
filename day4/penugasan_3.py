import tkinter as tk
from tkinter import messagebox

def tambah_data():
    nama = entry_nama.get()
    nis = entry_nis.get()
    kelas = entry_kelas.get()
    
    if nama == "" or nis == "" or kelas == "":
        messagebox.showwarning("Peringatan", "Semua data harus diisi!")
    else:
        listbox.insert(tk.END, f"Nama: {nama} | NIS: {nis} | Kelas: {kelas}")
        entry_nama.delete(0, tk.END)
        entry_nis.delete(0, tk.END)
        entry_kelas.delete(0, tk.END)

def hapus_data():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        messagebox.showwarning("Peringatan", "Pilih data yang ingin dihapus!")

root = tk.Tk()
root.title("Program Data Siswa")
root.geometry("400x400")

tk.Label(root, text="PROGRAM DATA SISWA", font=("Arial", 14)).pack(pady=10)

tk.Label(root, text="Nama").pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

tk.Label(root, text="NIS").pack()
entry_nis = tk.Entry(root)
entry_nis.pack()

tk.Label(root, text="Kelas").pack()
entry_kelas = tk.Entry(root)
entry_kelas.pack()

tk.Button(root, text="Tambah Data", command=tambah_data).pack(pady=5)
tk.Button(root, text="Hapus Data", command=hapus_data).pack()

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

root.mainloop()