from data import tempat_wisata, cari_tempat_wisata, hitung_total_harga  
from login import clear_screen 
from prettytable import PrettyTable

def tampilkan_daftar_wisata():
    if not tempat_wisata:
        print("Tidak ada data tempat wisata.")
        return
    
    table = PrettyTable()
    table.field_names = ["No", "Nama", "Jadwal", "Kuota", "Harga", "Ketersediaan"]
    
    i = 1
    for nama, data in tempat_wisata.items():
        ketersediaan = 'Tersedia' if data["kuota"] > 0 else 'Penuh'
        table.add_row([i, nama, data['jadwal'], data['kuota'], f"Rp {data['harga']:,}", ketersediaan])
        i += 1
    
    print("\nDaftar Tempat Wisata:")
    print(table)
    
    print("\nDeskripsi Detail:")
    i = 1
    for nama, data in tempat_wisata.items():
        print(f"{i}. {nama}: {data['deskripsi']}")
        i += 1

def admin(current_user):
    menu_running = True
    while menu_running:
        clear_screen()
        print("=== MENU ADMIN ===")
        print(f"User: {current_user}")
        print("1. Create (Tambah Tempat Wisata)")
        print("2. Read (Lihat/Cari Tempat Wisata)")
        print("3. Update (Ubah Data)")
        print("4. Delete (Hapus Data)")
        print("5. Keluar")
        try:
            menu_choice = int(input("Pilih menu (1-5): ").strip())
            if menu_choice < 1 or menu_choice > 5:
                raise ValueError
        except ValueError:
            print("Error: Masukkan angka yang valid!")
            input("Tekan Enter untuk lanjut...")
            continue
        
        if menu_choice == 1:
            clear_screen()
            print("=== TAMBAH TEMPAT WISATA BARU ===")
            nama = ""
            while not nama:
                nama = input("Nama tempat wisata: ").strip()
                if not nama:
                    print("Error: Input tidak boleh kosong!")
                elif nama in tempat_wisata:
                    print("Error: Nama tempat wisata sudah ada!")
                    nama = ""
            
            jadwal = ""
            while not jadwal:
                jadwal = input("Jadwal buka (contoh: 08:00 - 17:00): ").strip()
                if not jadwal:
                    print("Error: Input tidak boleh kosong!")
            
            kuota = 0
            while kuota <= 0:
                try:
                    kuota = int(input("Kuota pengunjung harian: ").strip())
                    if kuota <= 0:
                        raise ValueError
                except ValueError:
                    print("Error: Masukkan angka positif yang valid!")
            
            harga = 0
            while harga <= 0:
                try:
                    harga = int(input("Harga tiket: ").strip())
                    if harga <= 0:
                        raise ValueError
                except ValueError:
                    print("Error: Masukkan angka positif yang valid!")
            
            deskripsi = ""
            while not deskripsi:
                deskripsi = input("Deskripsi: ").strip()
                if not deskripsi:
                    print("Error: Input tidak boleh kosong!")
            
            tempat_wisata[nama] = {
                "jadwal": jadwal,
                "kuota": kuota,
                "harga": harga,
                "deskripsi": deskripsi
            }
            print("Tempat wisata berhasil ditambahkan!")
            input("Tekan Enter untuk kembali...")
        
        elif menu_choice == 2:
            clear_screen()
            print("=== LIHAT TEMPAT WISATA ===")
            tampilkan_daftar_wisata()
            
            cari = input("\nCari nama tempat (kosongkan untuk skip): ").strip().lower()
            if cari:
                hasil_cari = cari_tempat_wisata(cari)
                if hasil_cari:
                    for nama, data in hasil_cari:
                        print(f"\nDitemukan: {nama}")
                        print(f"Jadwal: {data['jadwal']} | Harga: Rp {data['harga']:,} | Ketersediaan: {data['kuota']} slot")
                else:
                    print("Tidak ditemukan!")
            
            input("\nTekan Enter untuk kembali...")
        
        elif menu_choice == 3:
            clear_screen()
            print("=== UPDATE TEMPAT WISATA ===")
            if not tempat_wisata:
                print("Tidak ada data untuk diupdate.")
                input("Tekan Enter untuk kembali...")
                continue
            
            i = 1
            for nama in tempat_wisata.keys():
                print(f"{i}. {nama}")
                i += 1
            
            pilihan = 0
            while pilihan < 1 or pilihan > len(tempat_wisata):
                try:
                    pilihan = int(input("Pilih nomor tempat untuk update: ").strip())
                    if pilihan < 1:
                        raise ValueError
                except ValueError:
                    print("Error: Masukkan angka positif yang valid!")
            
            nama_pilih = list(tempat_wisata.keys())[pilihan - 1]
            data_pilih = tempat_wisata[nama_pilih]
            
            print(f"\nData saat ini: {nama_pilih} - {data_pilih}")
            
            print("1. Ubah kuota pengunjung")
            print("2. Ubah harga tiket")
            print("3. Ubah jadwal")
            print("4. Ubah deskripsi")
            sub_pilihan = 0
            while sub_pilihan < 1 or sub_pilihan > 4:
                try:
                    sub_pilihan = int(input("Pilih field untuk update (1-4): ").strip())
                    if sub_pilihan < 1 or sub_pilihan > 4:
                        raise ValueError
                except ValueError:
                    print("Error: Pilihan tidak valid!")
            
            if sub_pilihan == 1:
                new_kuota = 0
                while new_kuota <= 0:
                    try:
                        new_kuota = int(input("Kuota baru: ").strip())
                        if new_kuota <= 0:
                            raise ValueError
                    except ValueError:
                        print("Error: Masukkan angka positif yang valid!")
                tempat_wisata[nama_pilih]["kuota"] = new_kuota
            elif sub_pilihan == 2:
                new_harga = 0
                while new_harga <= 0:
                    try:
                        new_harga = int(input("Harga baru: ").strip())
                        if new_harga <= 0:
                            raise ValueError
                    except ValueError:
                        print("Error: Masukkan angka positif yang valid!")
                tempat_wisata[nama_pilih]["harga"] = new_harga
            elif sub_pilihan == 3:
                new_jadwal = ""
                while not new_jadwal:
                    new_jadwal = input("Jadwal baru: ").strip()
                    if not new_jadwal:
                        print("Error: Input tidak boleh kosong!")
                tempat_wisata[nama_pilih]["jadwal"] = new_jadwal
            elif sub_pilihan == 4:
                new_desk = ""
                while not new_desk:
                    new_desk = input("Deskripsi baru: ").strip()
                    if not new_desk:
                        print("Error: Input tidak boleh kosong!")
                tempat_wisata[nama_pilih]["deskripsi"] = new_desk
            
            print("Update berhasil!")
            input("Tekan Enter untuk kembali...")
        
        elif menu_choice == 4:
            clear_screen()
            print("=== HAPUS TEMPAT WISATA ===")
            if not tempat_wisata:
                print("Tidak ada data untuk dihapus.")
                input("Tekan Enter untuk kembali...")
                continue
            
            i = 1
            for nama in tempat_wisata.keys():
                print(f"{i}. {nama}")
                i += 1
            
            pilihan = 0
            while pilihan < 1 or pilihan > len(tempat_wisata):
                try:
                    pilihan = int(input("Pilih nomor tempat untuk hapus: ").strip())
                    if pilihan < 1:
                        raise ValueError
                except ValueError:
                    print("Error: Masukkan angka positif yang valid!")
            
            nama_hapus = list(tempat_wisata.keys())[pilihan - 1]
            
            confirm = input(f"Yakin hapus '{nama_hapus}'? (y/n): ").strip().lower()
            if confirm == 'y':
                del tempat_wisata[nama_hapus]
                print("Hapus berhasil!")
            else:
                print("Batal hapus.")
            
            input("Tekan Enter untuk kembali...")
        
        elif menu_choice == 5:
            menu_running = False

def user(current_user):
    menu_running = True
    while menu_running:
        clear_screen()
        print("=== MENU USER ===")
        print(f"User: {current_user}")
        print("1. Read (Lihat/Cari Tempat Wisata)")
        print("2. Pesan Tiket (Book Tickets)")
        print("3. Keluar")
        try:
            menu_choice = int(input("Pilih menu (1-3): ").strip())
            if menu_choice < 1 or menu_choice > 3:
                raise ValueError
        except ValueError:
            print("Error: Masukkan angka yang valid!")
            input("Tekan Enter untuk lanjut...")
            continue
        
        if menu_choice == 1:
            clear_screen()
            print("=== LIHAT TEMPAT WISATA ===")
            tampilkan_daftar_wisata()
            
            cari = input("\nCari nama tempat (kosongkan untuk skip): ").strip().lower()
            if cari:
                hasil_cari = cari_tempat_wisata(cari)
                if hasil_cari:
                    for nama, data in hasil_cari:
                        print(f"\nDitemukan: {nama}")
                        print(f"Jadwal: {data['jadwal']} | Harga: Rp {data['harga']:,} | Ketersediaan: {data['kuota']} slot")
                else:
                    print("Tidak ditemukan!")
            
            input("\nTekan Enter untuk kembali...")
        
        elif menu_choice == 2:
            clear_screen()
            print("=== PESAN TIKET WISATA ===")
            if not tempat_wisata:
                print("Tidak ada data tempat wisata untuk dipesan.")
                input("Tekan Enter untuk kembali...")
                continue
            
            tampilkan_daftar_wisata()
            
            pilihan = 0
            while pilihan < 1 or pilihan > len(tempat_wisata):
                try:
                    pilihan = int(input("Pilih nomor tempat wisata untuk pesan tiket: ").strip())
                    if pilihan < 1:
                        raise ValueError
                except ValueError:
                    print("Error: Masukkan angka positif yang valid!")
            
            nama_pilih = list(tempat_wisata.keys())[pilihan - 1]
            data_pilih = tempat_wisata[nama_pilih]
            
            if data_pilih["kuota"] <= 0:
                print("Maaf, kuota untuk tempat ini sudah penuh!")
                input("Tekan Enter untuk kembali...")
                continue
            
            jumlah_tiket = 0
            while jumlah_tiket <= 0 or jumlah_tiket > data_pilih["kuota"]:
                try:
                    jumlah_tiket = int(input("Masukkan jumlah tiket yang diinginkan: ").strip())
                    if jumlah_tiket <= 0:
                        raise ValueError
                    if jumlah_tiket > data_pilih["kuota"]:
                        print(f"Error: Kuota tersedia hanya {data_pilih['kuota']} tiket!")
                        jumlah_tiket = 0
                except ValueError:
                    print("Error: Masukkan angka positif yang valid!")
            
            tempat_wisata[nama_pilih]["kuota"] -= jumlah_tiket
            total_harga = hitung_total_harga(jumlah_tiket, data_pilih["harga"])
            print(f"Pemesanan berhasil! Anda memesan {jumlah_tiket} tiket untuk {nama_pilih}.")
            print(f"Total harga: Rp {total_harga:,}")
            print(f"Kuota tersisa: {tempat_wisata[nama_pilih]['kuota']}")
            input("Tekan Enter untuk kembali...")
        
        elif menu_choice == 3:
            menu_running = False
