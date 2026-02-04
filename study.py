catatan = []
target_harian = None

def tambah_catatan():
    mapel = input("Mapel: ").strip()
    topik = input("Topik: ").strip()
    while True:
        durasi_input = input("Durasi belajar (menit): ").strip()
        try:
            durasi = int(durasi_input)
            if durasi <= 0:
                print("Masukkan angka durasi lebih dari 0.")
                continue
            break
        except ValueError:
            print("Input tidak valid. Masukkan angka (mis. 30).")
    entry = {"mapel": mapel, "topik": topik, "durasi": durasi}
    catatan.append(entry)
    print("Catatan berhasil ditambahkan.")

def lihat_catatan():
    if not catatan:
        print("Belum ada catatan belajar.")
        return
    print("\nDaftar catatan belajar:")
    for i, c in enumerate(catatan, 1):
        print(f"{i}. Mapel: {c['mapel']}, Topik: {c['topik']}, Durasi: {c['durasi']} menit")

def total_waktu():
    if not catatan:
        print("Total waktu: 0 menit")
        return
    total = sum(c.get("durasi", 0) for c in catatan)
    jam = total // 60
    menit = total % 60
    if jam:
        print(f"Total waktu belajar: {jam} jam {menit} menit ({total} menit)")
    else:
        print(f"Total waktu belajar: {menit} menit ({total} menit)")

def set_target_harian():
    global target_harian
    while True:
        inp = input("Atur target harian (menit): ").strip()
        if inp == "":
            print("Batal. Target tidak diubah.")
            return
        try:
            t = int(inp)
            if t <= 0:
                print("Masukkan angka lebih dari 0.")
                continue
            target_harian = t
            print(f"Target harian diset: {target_harian} menit")
            return
        except ValueError:
            print("Input tidak valid. Masukkan angka (mis. 60).")

def lihat_progress_target():
    if target_harian is None:
        print("Target harian belum diset. Gunakan menu 'Atur target harian'.")
        return
    total = sum(c.get("durasi", 0) for c in catatan)
    sisa = target_harian - total
    persen = (total / target_harian) * 100 if target_harian > 0 else 0
    print(f"Target harian: {target_harian} menit")
    print(f"Total tercatat: {total} menit ({persen:.1f}%)")
    if sisa > 0:
        jam = sisa // 60
        menit = sisa % 60
        if jam:
            print(f"Sisa untuk mencapai target: {jam} jam {menit} menit")
        else:
            print(f"Sisa untuk mencapai target: {menit} menit")
    else:
        print(f"Target tercapai! Melebihi {abs(sisa)} menit.")

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Atur target harian")
    print("5. Lihat progress target")
    print("6. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        set_target_harian()
    elif pilihan == "5":
        lihat_progress_target()
    elif pilihan == "6":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")