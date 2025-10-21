import os

tempat_wisata = {
    "Air Terjun Jantur Inar": {"jadwal": "08:00 - 16:00","kuota": 100,"harga": 25000,"deskripsi": "Air yang deras mengalir dari atas tebing dan jatuh dengan gemuruh yang menggetarkan hati. Suara gemuruh air terjun yang indah mengalir dalam keheningan hutan, menciptakan suasana yang menenangkan dan menyejukkan jiwa. Keindahan ini menarik perhatian para wisatawan yang ingin menjauh sejenak dari hiruk-pikuk kehidupan perkotaan."},
    "Gunung S": {"jadwal": "04:00 - 18:00","kuota": 150,"harga": 15000, "deskripsi": "Gunung S memiliki keunikan tak hanya terletak pada pemandangannya yang menakjubkan, namun juga pada suasana bak Negeri di Atas Awan Selain itu, kamu juga bisa mencoba olahraga paralayang. Gunung S menjadi lokasi favorit bagi atlet paralayang nasional untuk mengeksplorasi keindahan alam Kutai Barat dari ketinggian."},
    "Lakam Bilem": {"jadwal": "08:00 - 16:00","kuota": 200,"harga": 35000, "deskripsi": "Lakam Bilem bukan hanya memiliki sungai yang terus mengalir namun banyak opsi yang bisa kita nikmati seperti arung jeram, goa kelelawar, dan Bumi Perkemahan batu Bura."}
}

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user1": {"password": "user123", "role": "user"}
}

is_running = True
os.system('cls' if os.name == 'nt' else 'clear')
print("Selamat datang di Program Manajemen Tempat Wisata!")

while is_running:
    print("\n1. Login")
    print("2. Register")
    print("3. Keluar")
    choice = input("Pilih (1-3): ").strip()
    
    if choice == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LOGIN ===")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        if not username or not password:
            print("Error: Username dan password tidak boleh kosong!")
            input("Tekan Enter untuk kembali...")
            continue
        
        role = None
        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
        
        if role is None:
            print("Error: Username atau password salah!")
            input("Tekan Enter untuk kembali...")
            continue
        
        menu_running = True
        while menu_running:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== PROGRAM MANAJEMEN TEMPAT WISATA ===")
            if role == "admin":
                print("1. Create (Tambah Tempat Wisata)")
                print("2. Read (Lihat/Cari Tempat Wisata)")
                print("3. Update (Ubah Data)")
                print("4. Delete (Hapus Data)")
                print("5. Keluar")
                menu_choice = input("Pilih menu (1-5): ").strip()
                if not menu_choice.isdigit() or int(menu_choice) < 1 or int(menu_choice) > 5:
                    print("Error: Pilihan tidak valid!")
                    input("Tekan Enter untuk lanjut...")
                    continue
                menu_choice = int(menu_choice)
            else:
                print("1. Read (Lihat/Cari Tempat Wisata)")
                print("2. Pesan Tiket (Book Tickets)")
                print("3. Keluar")
                menu_choice = input("Pilih menu (1-3): ").strip()
                if not menu_choice.isdigit() or int(menu_choice) < 1 or int(menu_choice) > 3:
                    print("Error: Pilihan tidak valid!")
                    input("Tekan Enter untuk lanjut...")
                    continue
                menu_choice = int(menu_choice)
            
            if menu_choice == 1:
                if role == "admin":
                    os.system('cls' if os.name == 'nt' else 'clear')
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
                        kuota_input = input("Kuota pengunjung harian: ").strip()
                        if kuota_input.isdigit() and int(kuota_input) > 0:
                            kuota = int(kuota_input)
                        else:
                            print("Error: Masukkan angka positif yang valid!")
                    
                    harga = 0
                    while harga <= 0:
                        harga_input = input("Harga tiket: ").strip()
                        if harga_input.isdigit() and int(harga_input) > 0:
                            harga = int(harga_input)
                        else:
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
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== LIHAT TEMPAT WISATA ===")
                    if not tempat_wisata:
                        print("Tidak ada data tempat wisata.")
                        input("Tekan Enter untuk kembali...")
                        continue
                    
                    print("\nDaftar Tempat Wisata:")
                    print(f"{'No':<5} {'Nama':<30} {'Jadwal':<15} {'Kuota':<10} {'Harga':<15} {'Ketersediaan':<15}")
                    print("-" * (5 + 30 + 15 + 10 + 15 + 15 + 5*5))
                    
                    i = 1
                    for nama, data in tempat_wisata.items():
                        ketersediaan = 'Tersedia' if data["kuota"] > 0 else 'Penuh'
                        print(f"{i:<5} {nama:<30} {data['jadwal']:<15} {data['kuota']:<10} {'Rp ' + format(data['harga'], ','):<15} {ketersediaan:<15}")
                        i += 1
                    
                    print("\nDeskripsi Detail:")
                    i = 1
                    for nama, data in tempat_wisata.items():
                        print(f"{i}. {nama}: {data['deskripsi']}")
                        i += 1
                    
                    cari = input("\nCari nama tempat (kosongkan untuk skip): ").strip().lower()
                    if cari:
                        found = False
                        for nama, data in tempat_wisata.items():
                            if cari in nama.lower():
                                print(f"\nDitemukan: {nama}")
                                print(f"Jadwal: {data['jadwal']} | Harga: Rp {data['harga']:,} | Ketersediaan: {data['kuota']} slot")
                                found = True
                        if not found:
                            print("Tidak ditemukan!")
                    
                    input("\nTekan Enter untuk kembali...")
            
            elif menu_choice == 2:
                if role == "admin":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== LIHAT TEMPAT WISATA ===")
                    if not tempat_wisata:
                        print("Tidak ada data tempat wisata.")
                        input("Tekan Enter untuk kembali...")
                        continue
                    
                    print("\nDaftar Tempat Wisata:")
                    print(f"{'No':<5} {'Nama':<30} {'Jadwal':<15} {'Kuota':<10} {'Harga':<15} {'Ketersediaan':<15}")
                    print("-" * (5 + 30 + 15 + 10 + 15 + 15 + 5*5))
                    
                    i = 1
                    for nama, data in tempat_wisata.items():
                        ketersediaan = 'Tersedia' if data["kuota"] > 0 else 'Penuh'
                        print(f"{i:<5} {nama:<30} {data['jadwal']:<15} {data['kuota']:<10} {'Rp ' + format(data['harga'], ','):<15} {ketersediaan:<15}")
                        i += 1
                    
                    print("\nDeskripsi Detail:")
                    i = 1
                    for nama, data in tempat_wisata.items():
                        print(f"{i}. {nama}: {data['deskripsi']}")
                        i += 1
                    
                    cari = input("\nCari nama tempat (kosongkan untuk skip): ").strip().lower()
                    if cari:
                        found = False
                        for nama, data in tempat_wisata.items():
                            if cari in nama.lower():
                                print(f"\nDitemukan: {nama}")
                                print(f"Jadwal: {data['jadwal']} | Harga: Rp {data['harga']:,} | Ketersediaan: {data['kuota']} slot")
                                found = True
                        if not found:
                            print("Tidak ditemukan!")
                    
                    input("\nTekan Enter untuk kembali...")
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== PESAN TIKET WISATA ===")
                    if not tempat_wisata:
                        print("Tidak ada data tempat wisata untuk dipesan.")
                        input("Tekan Enter untuk kembali...")
                        continue
                    
                    print("\nDaftar Tempat Wisata Tersedia:")
                    print(f"{'No':<5} {'Nama':<30} {'Jadwal':<15} {'Kuota':<10} {'Harga':<15} {'Ketersediaan':<15}")
                    print("-" * (5 + 30 + 15 + 10 + 15 + 15 + 5*5))
                    
                    i = 1
                    for nama, data in tempat_wisata.items():
                        ketersediaan = 'Tersedia' if data["kuota"] > 0 else 'Penuh'
                        print(f"{i:<5} {nama:<30} {data['jadwal']:<15} {data['kuota']:<10} {'Rp ' + format(data['harga'], ','):<15} {ketersediaan:<15}")
                        i += 1
                    
                    pilihan = 0
                    while pilihan < 1 or pilihan > len(tempat_wisata):
                        pilihan_input = input("Pilih nomor tempat wisata untuk pesan tiket: ").strip()
                        if pilihan_input.isdigit() and int(pilihan_input) > 0:
                            pilihan = int(pilihan_input)
                        else:
                            print("Error: Masukkan angka positif yang valid!")
                    
                    nama_pilih = None
                    data_pilih = None
                    i = 1
                    for nama, data in tempat_wisata.items():
                        if i == pilihan:
                            nama_pilih = nama
                            data_pilih = data
                            break
                        i += 1
                    
                    if data_pilih["kuota"] <= 0:
                        print("Maaf, kuota untuk tempat ini sudah penuh!")
                        input("Tekan Enter untuk kembali...")
                        continue
                    
                    jumlah_tiket = 0
                    while jumlah_tiket <= 0 or jumlah_tiket > data_pilih["kuota"]:
                        jumlah_input = input("Masukkan jumlah tiket yang diinginkan: ").strip()
                        if jumlah_input.isdigit() and int(jumlah_input) > 0:
                            jumlah_tiket = int(jumlah_input)
                            if jumlah_tiket > data_pilih["kuota"]:
                                print(f"Error: Kuota tersedia hanya {data_pilih['kuota']} tiket!")
                                jumlah_tiket = 0
                        else:
                            print("Error: Masukkan angka positif yang valid!")
                    
                    tempat_wisata[nama_pilih]["kuota"] -= jumlah_tiket  
                    total_harga = jumlah_tiket * data_pilih["harga"]
                    print(f"Pemesanan berhasil! Anda memesan {jumlah_tiket} tiket untuk {nama_pilih}.")
                    print(f"Total harga: Rp {total_harga:,}")
                    print(f"Kuota tersisa: {tempat_wisata[nama_pilih]['kuota']}")
                    input("Tekan Enter untuk kembali...")
            
            elif menu_choice == 3:
                if role == "admin":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== UPDATE TEMPAT WISATA ===")
                    if not tempat_wisata:
                        print("Tidak ada data untuk diupdate.")
                        input("Tekan Enter untuk kembali...")
                        continue
                    
                    i = 1
                    for nama, data in tempat_wisata.items():
                        print(f"{i}. {nama}")
                    i += 1
                    
                    pilihan = 0
                    while pilihan < 1 or pilihan > len(tempat_wisata):
                        pilihan_input = input("Pilih nomor tempat untuk update: ").strip()
                        if pilihan_input.isdigit() and int(pilihan_input) > 0:
                            pilihan = int(pilihan_input)
                        else:
                            print("Error: Masukkan angka positif yang valid!")
                    
                    nama_pilih = None
                    data_pilih = None
                    i = 1
                    for nama, data in tempat_wisata.items():
                        if i == pilihan:
                            nama_pilih = nama
                            data_pilih = data
                            break
                        i += 1
                    
                    print(f"\nData saat ini: {nama_pilih} - {data_pilih}")
                    
                    print("1. Ubah kuota pengunjung")
                    print("2. Ubah harga tiket")
                    print("3. Ubah jadwal")
                    print("4. Ubah deskripsi")
                    sub_pilihan = 0
                    while sub_pilihan < 1 or sub_pilihan > 4:
                        sub_input = input("Pilih field untuk update (1-4): ").strip()
                        if sub_input.isdigit() and int(sub_input) >= 1 and int(sub_input) <= 4:
                            sub_pilihan = int(sub_input)
                        else:
                            print("Error: Pilihan tidak valid!")
                    
                    if sub_pilihan == 1:
                        new_kuota = 0
                        while new_kuota <= 0:
                            kuota_input = input("Kuota baru: ").strip()
                            if kuota_input.isdigit() and int(kuota_input) > 0:
                                new_kuota = int(kuota_input)
                            else:
                                print("Error: Masukkan angka positif yang valid!")
                        tempat_wisata[nama_pilih]["kuota"] = new_kuota
                    elif sub_pilihan == 2:
                        new_harga = 0
                        while new_harga <= 0:
                            harga_input = input("Harga baru: ").strip()
                            if harga_input.isdigit() and int(harga_input) > 0:
                                new_harga = int(harga_input)
                            else:
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
                else:
                    menu_running = False
            
            elif menu_choice == 4 and role == "admin":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== HAPUS TEMPAT WISATA ===")
                if not tempat_wisata:
                    print("Tidak ada data untuk dihapus.")
                    input("Tekan Enter untuk kembali...")
                    continue
                
                i = 1
                for nama, data in tempat_wisata.items():
                    print(f"{i}. {nama}")
                    i += 1
                
                pilihan = 0
                while pilihan < 1 or pilihan > len(tempat_wisata):
                    pilihan_input = input("Pilih nomor tempat untuk hapus: ").strip()
                    if pilihan_input.isdigit() and int(pilihan_input) > 0:
                        pilihan = int(pilihan_input)
                    else:
                        print("Error: Masukkan angka positif yang valid!")
                
                nama_hapus = None
                i = 1
                for nama, data in tempat_wisata.items():
                    if i == pilihan:
                        nama_hapus = nama
                        break
                    i += 1
                
                confirm = input(f"Yakin hapus '{nama_hapus}'? (y/n): ").strip().lower()
                if confirm == 'y':
                    del tempat_wisata[nama_hapus]
                    print("Hapus berhasil!")
                else:
                    print("Batal hapus.")
                
                input("Tekan Enter untuk kembali...")
            
            elif menu_choice == 5 and role == "admin":
                menu_running = False
    
    elif choice == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== REGISTRASI USER BARU ===")
        username = input("Masukkan username baru: ").strip()
        
        if not username:
            print("Error: Username tidak boleh kosong!")
            input("Tekan Enter untuk kembali...")
            continue
        
        if username in users:
            print("Error: Username sudah terdaftar!")
            input("Tekan Enter untuk kembali...")
            continue
        
        password = input("Masukkan password: ").strip()
        if not password:
            print("Error: Password tidak boleh kosong!")
            input("Tekan Enter untuk kembali...")
            continue
        
        users[username] = {"password": password, "role": "user"}
        print("Registrasi berhasil! Anda sekarang bisa login.")
        input("Tekan Enter untuk kembali...")
    
    elif choice == '3':
        is_running = False
        print("Terima kasih telah menggunakan program ini!")