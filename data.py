import json
import os

FILENAME = "saldo.json"

saldo = 0
transactions = []

def load_data():
    global saldo
    try:
        if os.path.exists(FILENAME):
            with open(FILENAME, "r") as f:
                data = json.load(f)
                saldo = data.get("saldo", 0)
                transactions = data.get("transactions", [])
    except Exception as e:
        print("Gagal memuat data:", e)
        saldo = 0

def save_data():
    try:
        with open(FILENAME, "w") as f:
            json.dump({"saldo": saldo, "transactions": transactions}, f)
    except Exception as e:
        print("Gagal menyimpan data:", e)

def tambah_pemasukan():
    global saldo
    try:
        jumlah = float(input("Masukkan jumlah pemasukan: "))
    except ValueError:
        print("Input tidak valid. Masukkan angka.")
        return

    if jumlah <= 0:
        print("Jumlah harus lebih dari 0")
        return

    saldo += jumlah
    # catat transaksi
    transactions.append({"type": "pemasukan", "amount": jumlah})
    save_data()
    if jumlah.is_integer():
        jumlah = int(jumlah)
    print(f"Berhasil menambahkan pemasukan sebesar {jumlah}")

def tambah_pengeluaran():
    global saldo
    try:
        jumlah = float(input("Masukkan jumlah pengeluaran: "))
    except ValueError:
        print("Input tidak valid. Masukkan angka.")
        return

    if jumlah <= 0:
        print("Jumlah harus lebih dari 0")
        return

    if jumlah > saldo:
        print("Saldo tidak cukup")
        return

    saldo -= jumlah
    # catat transaksi
    transactions.append({"type": "pengeluaran", "amount": jumlah})
    save_data()
    if jumlah.is_integer():
        jumlah = int(jumlah)
    print(f"Berhasil menambahkan pengeluaran sebesar {jumlah}")

def lihat_saldo():
    global saldo
    if isinstance(saldo, float):
        if saldo.is_integer():
            tampilan = f"{int(saldo):,}"
        else:
            tampilan = f"{saldo:,.2f}"
    else:
        tampilan = f"{saldo:,}"

    print("Saldo saat ini:", tampilan)

def laporan():
    global transactions
    if not transactions:
        print("Belum ada transaksi.")
        return

    total_pemasukan = 0
    total_pengeluaran = 0
    print("=== Laporan Transaksi ===")
    for i, t in enumerate(transactions, start=1):
        tipe = t.get("type", "")
        amt = t.get("amount", 0)
        if tipe == "pemasukan":
            total_pemasukan += amt
        elif tipe == "pengeluaran":
            total_pengeluaran += amt

        # format amount
        if isinstance(amt, float) and amt.is_integer():
            tampil = f"{int(amt):,}"
        elif isinstance(amt, float):
            tampil = f"{amt:,.2f}"
        else:
            tampil = f"{amt:,}"

        print(f"{i}. {tipe.capitalize():12} {tampil}")

    # summary
    if isinstance(total_pemasukan, float) and total_pemasukan.is_integer():
        tp = int(total_pemasukan)
    else:
        tp = total_pemasukan
    if isinstance(total_pengeluaran, float) and total_pengeluaran.is_integer():
        tg = int(total_pengeluaran)
    else:
        tg = total_pengeluaran

    print("---------------------------")
    print(f"Total pemasukan   : {tp}")
    print(f"Total pengeluaran : {tg}")

def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("5. Laporan transaksi")
    print("4. Keluar")

while True:
    load_data()
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "5":
        laporan()
    elif pilihan == "4":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid")