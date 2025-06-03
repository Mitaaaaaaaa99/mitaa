import tkinter as tk
from tkinter import messagebox

# Data nasabah
data_nasabah = []

# --- Fungsi-fungsi umum ---
def hitung_saldo():
    try:
        nama = entry_nama.get()
        norek = entry_norek.get()
        saldo_awal = float(entry_saldo.get())
        tarik = float(entry_tarik.get())
        tanggal = entry_tanggal.get()

        if tarik > saldo_awal:
            messagebox.showerror("Error", "Penarikan melebihi saldo!")
            return

        saldo_akhir = saldo_awal - tarik

        nasabah = {
            "nama": nama.lower(),
            "norek": norek,
            "tanggal": tanggal,
            "saldo_awal": saldo_awal,
            "tarik": tarik,
            "saldo_akhir": saldo_akhir
        }
        data_nasabah.append(nasabah)

        messagebox.showinfo("Data Tersimpan", f"Data untuk {nama} berhasil disimpan.")

    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid pada saldo dan tarikan!")

def cari_nasabah(entry, role='admin'):
    keyword = entry.get().lower().strip()
    if not keyword:
        messagebox.showwarning("Peringatan", "Masukkan nama atau no. rekening!")
        return

    for nasabah in data_nasabah:
        if keyword == nasabah['nama'] or keyword == nasabah['norek']:
            info = (
                f"Nama: {nasabah['nama'].title()}\n"
                f"No. Rekening: {nasabah['norek']}\n"
                f"Tanggal: {nasabah['tanggal']}\n"
                f"Saldo Akhir: Rp {nasabah['saldo_akhir']:,.2f}"
            )
            messagebox.showinfo("Ditemukan", info)
            return

    messagebox.showerror("Tidak Ditemukan", "Data nasabah tidak ditemukan!")

# --- Frame: Pilihan Login ---
def show_login():
    clear_frame()
    tk.Label(root, text="Pilih Mode Akses").pack(pady=10)
    tk.Button(root, text="Masuk sebagai Admin", width=25, command=admin_mode).pack(pady=5)
    tk.Button(root, text="Masuk sebagai Client", width=25, command=client_mode).pack(pady=5)

# --- Frame: Admin Mode ---
def admin_mode():
    clear_frame()

    tk.Label(root, text="Admin Mode - Input Nasabah").grid(row=0, column=0, columnspan=2, pady=5)

    global entry_nama, entry_norek, entry_saldo, entry_tarik, entry_tanggal

    tk.Label(root, text="Nama Nasabah:").grid(row=1, column=0, sticky="w")
    entry_nama = tk.Entry(root)
    entry_nama.grid(row=1, column=1)

    tk.Label(root, text="No. Rekening:").grid(row=2, column=0, sticky="w")
    entry_norek = tk.Entry(root)
    entry_norek.grid(row=2, column=1)

    tk.Label(root, text="Saldo Awal (Rp):").grid(row=3, column=0, sticky="w")
    entry_saldo = tk.Entry(root)
    entry_saldo.grid(row=3, column=1)

    tk.Label(root, text="Jumlah Tarikan (Rp):").grid(row=4, column=0, sticky="w")
    entry_tarik = tk.Entry(root)
    entry_tarik.grid(row=4, column=1)

    tk.Label(root, text="Tanggal (dd-mm-yyyy):").grid(row=5, column=0, sticky="w")
    entry_tanggal = tk.Entry(root)
    entry_tanggal.grid(row=5, column=1)

    tk.Button(root, text="Simpan Data", command=hitung_saldo).grid(row=6, column=0, columnspan=2, pady=5)

    # Pencarian juga tersedia
    tk.Label(root, text="Cari Nasabah (Nama / No.Rek):").grid(row=7, column=0, sticky="w")
    entry_cari_admin = tk.Entry(root)
    entry_cari_admin.grid(row=7, column=1)

    tk.Button(root, text="Cari", command=lambda: cari_nasabah(entry_cari_admin)).grid(row=8, column=0, columnspan=2, pady=5)

    tk.Button(root, text="← Kembali", command=show_login).grid(row=9, column=0, columnspan=2)

# --- Frame: Client Mode ---
def client_mode():
    clear_frame()

    tk.Label(root, text="Client Mode - Cek Saldo").pack(pady=5)

    tk.Label(root, text="Cari Nasabah (Nama / No.Rek):").pack()
    entry_cari_client = tk.Entry(root)
    entry_cari_client.pack()

    tk.Button(root, text="Cari", command=lambda: cari_nasabah(entry_cari_client, 'client')).pack(pady=5)
    tk.Button(root, text="← Kembali", command=show_login).pack(pady=5)

# --- Fungsi Util ---
def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()

# --- GUI Main ---
root = tk.Tk()
root.title("BankApp – Mode Admin & Client")
root.geometry("350x400")
show_login()
root.mainloop()
