import tkinter as tk
from tkinter import messagebox

def hitung_total():
    try:
        harga = int(entry_harga.get())
        jumlah = int(entry_jumlah.get())
        total = harga * jumlah
        label_total.config(text=f"Total: Rp {total}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang benar!")

def reset():
    entry_harga.delete(0, tk.END)
    entry_jumlah.delete(0, tk.END)
    label_total.config(text="Total: Rp 0")

root = tk.Tk()
root.title("Program Kasir Sederhana")
root.geometry("300x250")

tk.Label(root, text="PROGRAM KASIR", font=("Arial", 14)).pack(pady=10)

tk.Label(root, text="Harga Barang").pack()
entry_harga = tk.Entry(root)
entry_harga.pack()

tk.Label(root, text="Jumlah Barang").pack()
entry_jumlah = tk.Entry(root)
entry_jumlah.pack()

tk.Button(root, text="Hitung Total", command=hitung_total).pack(pady=5)
tk.Button(root, text="Reset", command=reset).pack()

label_total = tk.Label(root, text="Total: Rp 0", font=("Arial", 12))
label_total.pack(pady=10)

root.mainloop()