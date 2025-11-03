from data import tempat_wisata, cari_tempat_wisata, hitung_total_harga
from login import clear_screen
from prettytable import PrettyTable

def tampilkan_wisata():
    if not tempat_wisata:
        print("Tidak ada data tempat wisata.")
        return
    table = PrettyTable()
    table.field_names = ["No", "Nama", "Jadwal", "Kuota", "Harga", "Status"]
    table.align = "l"
    for i, (nama, data) in enumerate(tempat_wisata.items(), 1):
        status = "Tersedia" if data["kuota"] > 0 else "Penuh"
        harga = f"Rp {data['harga']:,}"
        table.add_row([i, nama, data["jadwal"], data["kuota"], harga, status])
    print(table)

def admin(current_user):
    while True:
        clear_screen()
        menu = PrettyTable()
        menu.title = f"MENU ADMIN — {current_user}"
        menu.field_names = ["No", "Menu"]
        menu.align = "l"
        menu.add_row(["1", "Create — Tambah Tempat Wisata"])
        menu.add_row(["2", "Read — Lihat/Cari Tempat Wisata"])
        menu.add_row(["3", "Update — Ubah Data Tempat"])
        menu.add_row(["4", "Delete — Hapus Tempat Wisata"])
        menu.add_row(["5", "Keluar"])
        print(menu)

        pilih = input("\nPilih (1-5): ").strip()

        if pilih == "1":
            clear_screen()
            print("=== TAMBAH TEMPAT WISATA ===")
            nama = input("Nama tempat: ").strip()
            if not nama:
                print("Error: Nama tidak boleh kosong!")
            elif nama in tempat_wisata:
                print("Error: Nama sudah ada!")
            else:
                jadwal = input("Jadwal: ").strip()
                kuota = int(input("Kuota harian: "))
                harga = int(input("Harga tiket: "))
                desc = input("Deskripsi: ").strip()
                tempat_wisata[nama] = {
                    "jadwal": jadwal,
                    "kuota": kuota,
                    "harga": harga,
                    "deskripsi": desc
                }
                print("Tempat wisata berhasil ditambahkan!")
            input("\nTekan Enter untuk kembali...")

        elif pilih == "2":
            clear_screen()
            print("=== DAFTAR TEMPAT WISATA ===")
            tampilkan_wisata()
            cari = input("\nCari tempat (kosongkan untuk skip): ").strip()
            if cari:
                hasil = cari_tempat_wisata(cari)
                if hasil:
                    t = PrettyTable()
                    t.field_names = ["Nama", "Jadwal", "Harga", "Kuota"]
                    t.align = "l"
                    for n, d in hasil:
                        t.add_row([n, d["jadwal"], f"Rp {d['harga']:,}", d["kuota"]])
                    print("\nHasil Pencarian:")
                    print(t)
                else:
                    print("\nTidak ditemukan.")
            input("\nTekan Enter untuk kembali...")

        elif pilih == "3":
            clear_screen()
            print("=== UBAH DATA TEMPAT ===")
            if not tempat_wisata:
                print("Tidak ada data untuk diubah.")
                input("\nTekan Enter...")
                continue
            tampilkan_wisata()
            try:
                no = int(input("\nPilih nomor tempat untuk diubah: "))
                nama = list(tempat_wisata.keys())[no - 1]
                tempat_wisata[nama]["jadwal"] = input(f"Jadwal baru (sekarang: {tempat_wisata[nama]['jadwal']}): ").strip() or tempat_wisata[nama]["jadwal"]
                tempat_wisata[nama]["kuota"] = int(input(f"Kuota baru (sekarang: {tempat_wisata[nama]['kuota']}): ") or tempat_wisata[nama]["kuota"])
                tempat_wisata[nama]["harga"] = int(input(f"Harga baru (sekarang: {tempat_wisata[nama]['harga']}): ") or tempat_wisata[nama]["harga"])
                tempat_wisata[nama]["deskripsi"] = input(f"Deskripsi baru: ").strip() or tempat_wisata[nama]["deskripsi"]
                print("Update berhasil!")
            except (ValueError, IndexError):
                print("Input tidak valid!")
            input("\nTekan Enter untuk kembali...")

        elif pilih == "4":
            clear_screen()
            print("=== HAPUS TEMPAT WISATA ===")
            if not tempat_wisata:
                print("Tidak ada data untuk dihapus.")
                input("\nTekan Enter...")
                continue
            tampilkan_wisata()
            try:
                no = int(input("\nPilih nomor tempat untuk dihapus: "))
                nama = list(tempat_wisata.keys())[no - 1]
                if input(f"Yakin hapus '{nama}'? (y/n): ").lower() == "y":
                    del tempat_wisata[nama]
                    print("Berhasil dihapus!")
                else:
                    print("Dibatalkan.")
            except (ValueError, IndexError):
                print("Pilihan tidak valid!")
            input("\nTekan Enter untuk kembali...")

        elif pilih == "5":
            break

        else:
            print("Pilihan tidak valid!")
            input("\nTekan Enter untuk lanjut...")

def user(current_user):
    while True:
        clear_screen()
        menu = PrettyTable()
        menu.title = f"MENU USER — {current_user}"
        menu.field_names = ["No", "Menu"]
        menu.align = "l"
        menu.add_row(["1", "Lihat/Cari Tempat Wisata"])
        menu.add_row(["2", "Pesan Tiket"])
        menu.add_row(["3", "Keluar"])
        print(menu)

        pilih = input("\nPilih (1-3): ").strip()
        if pilih == "1":
            clear_screen()
            print("=== DAFTAR TEMPAT WISATA ===")
            tampilkan_wisata()
            cari = input("\nCari tempat (kosongkan untuk skip): ").strip()
            if cari:
                hasil = cari_tempat_wisata(cari)
                if hasil:
                    t = PrettyTable()
                    t.field_names = ["Nama", "Jadwal", "Harga", "Kuota"]
                    t.align = "l"
                    for n, d in hasil:
                        t.add_row([n, d["jadwal"], f"Rp {d['harga']:,}", d["kuota"]])
                    print("\nHasil Pencarian:")
                    print(t)
                else:
                    print("\nTidak ditemukan.")
            input("\nTekan Enter untuk kembali...")
        elif pilih == "2":
            if not tempat_wisata:
                print("\nTidak ada tempat wisata.")
                input("Tekan Enter...")
                continue
            clear_screen()
            tampilkan_wisata()
            try:
                no = int(input("\nPilih nomor tempat: "))
                nama = list(tempat_wisata.keys())[no - 1]
                data = tempat_wisata[nama]
                if data["kuota"] <= 0:
                    print("Kuota penuh!")
                else:
                    jumlah = int(input("Jumlah tiket: "))
                    if 1 <= jumlah <= data["kuota"]:
                        tempat_wisata[nama]["kuota"] -= jumlah
                        total = hitung_total_harga(jumlah, data["harga"])
                        print(f"\nPemesanan berhasil!")
                        print(f"Total: Rp {total:,}")
                    else:
                        print("Jumlah melebihi kuota!")
            except (ValueError, IndexError):
                print("Input tidak valid!")
            input("\nTekan Enter untuk kembali...")
        elif pilih == "3":
            break
        else:
            print("Pilihan tidak valid!")
            input("\nTekan Enter untuk lanjut...")