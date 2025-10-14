import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

tempat_wisata = [
    ["Air Terjun Jantur Inar", "08:00 - 16:00", 100, 25000, "Air yang deras mengalir dari atas tebing dan jatuh dengan gemuruh yang menggetarkan hati. Suara gemuruh air terjun yang indah mengalir dalam keheningan hutan, menciptakan suasana yang menenangkan dan menyejukkan jiwa. Keindahan ini menarik perhatian para wisatawan yang ingin menjauh sejenak dari hiruk-pikuk kehidupan perkotaan."],
    ["Gunung S", "04:00 - 18:00", 150, 15000, "Gunung S memiliki keunikan tak hanya terletak pada pemandangannya yang menakjubkan, namun juga pada suasana bak Negeri di Atas Awan Selain itu, kamu juga bisa mencoba olahraga paralayang. Gunung S menjadi lokasi favorit bagi atlet paralayang nasional untuk mengeksplorasi keindahan alam Kutai Barat dari ketinggian."],
    ["Lakam Bilem", "08:00 - 16:00", 200, 35000, "Lakam Bilem bukan hanya memiliki sungai yang terus mengalir namun banyak opsi yang bisa kita nikmati seperti arung jeram, goa kelelawar, dan Bumi Perkemahan batu Bura."]
]

users = [
    ["admin", "admin123", "admin"],
    ["user1", "user123", "user"]
]

def register():
    clear_screen()
    print("=== REGISTRASI USER BARU ===")
    username = input("Masukkan username baru: ").strip()
    
    if not username:
        print("Error: Username tidak boleh kosong!")
        input("Tekan Enter untuk kembali...")
        return
    
    for user in users:
        if user[0] == username:
            print("Error: Username sudah terdaftar!")
            input("Tekan Enter untuk kembali...")
            return
    
    password = input("Masukkan password: ").strip()
    if not password:
        print("Error: Password tidak boleh kosong!")
        input("Tekan Enter untuk kembali...")
        return
    
    users.append([username, password, "user"])
    print("Registrasi berhasil! Anda sekarang bisa login.")
    input("Tekan Enter untuk kembali...")

def login():
    clear_screen()
    print("=== LOGIN ===")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    if not username or not password:
        print("Error: Username dan password tidak boleh kosong!")
        input("Tekan Enter untuk kembali...")
        return None
    
    for user in users:
        if user[0] == username and user[1] == password:
            return user[2] 
    
    print("Error: Username atau password salah!")
    input("Tekan Enter untuk kembali...")
    return None

def show_main_menu(role):
    clear_screen()
    print("=== PROGRAM MANAJEMEN TEMPAT WISATA ===")
    if role == "admin":
        print("1. Create (Tambah Tempat Wisata)")
        print("2. Read (Lihat/Cari Tempat Wisata)")
        print("3. Update (Ubah Data)")
        print("4. Delete (Hapus Data)")
        print("5. Keluar")
        return int(input("Pilih menu (1-5): "))
    else:  
        print("1. Read (Lihat/Cari Tempat Wisata)")
        print("2. Pesan Tiket (Book Tickets)")
        print("3. Keluar")
        return int(input("Pilih menu (1-3): "))

def get_valid_int(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Error: Masukkan angka positif yang valid!")

def get_valid_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: Input tidak boleh kosong!")

def create_wisata():
    clear_screen()
    print("=== TAMBAH TEMPAT WISATA BARU ===")
    nama = get_valid_string("Nama tempat wisata: ")
    jadwal = get_valid_string("Jadwal buka (contoh: 08:00 - 17:00): ")
    kuota = get_valid_int("Kuota pengunjung harian: ")
    harga = get_valid_int("Harga tiket: ")
    deskripsi = get_valid_string("Deskripsi: ")
    
    tempat_wisata.append([nama, jadwal, kuota, harga, deskripsi])
    print("Tempat wisata berhasil ditambahkan!")
    input("Tekan Enter untuk kembali...")

def read_wisata(role):
    clear_screen()
    print("=== LIHAT TEMPAT WISATA ===")
    if not tempat_wisata:
        print("Tidak ada data tempat wisata.")
        input("Tekan Enter untuk kembali...")
        return
    
    print("\nDaftar Tempat Wisata:")
    print(f"{'No':<5} {'Nama':<30} {'Jadwal':<15} {'Kuota':<10} {'Harga':<15} {'Ketersediaan':<15}")
    print("-" * (5 + 30 + 15 + 10 + 15 + 15 + 5*5))
    
    for i, data in enumerate(tempat_wisata, 1):
        ketersediaan = 'Tersedia' if data[2] > 0 else 'Penuh'
        print(f"{i:<5} {data[0]:<30} {data[1]:<15} {data[2]:<10} {'Rp ' + format(data[3], ','):<15} {ketersediaan:<15}")
    
    print("\nDeskripsi Detail:")
    for i, data in enumerate(tempat_wisata, 1):
        print(f"{i}. {data[0]}: {data[4]}")
    
    cari = input("\nCari nama tempat (kosongkan untuk skip): ").strip().lower()
    if cari:
        found = False
        for data in tempat_wisata:
            if cari in data[0].lower():
                print(f"\nDitemukan: {data[0]}")
                print(f"Jadwal: {data[1]} | Harga: Rp {data[3]:,} | Ketersediaan: {data[2]} slot")
                found = True
        if not found:
            print("Tidak ditemukan!")
    
    input("\nTekan Enter untuk kembali...")

def book_tiket():
    clear_screen()
    print("=== PESAN TIKET WISATA ===")
    if not tempat_wisata:
        print("Tidak ada data tempat wisata untuk dipesan.")
        input("Tekan Enter untuk kembali...")
        return
    
    print("\nDaftar Tempat Wisata Tersedia:")
    print(f"{'No':<5} {'Nama':<30} {'Jadwal':<15} {'Kuota':<10} {'Harga':<15} {'Ketersediaan':<15}")
    print("-" * (5 + 30 + 15 + 10 + 15 + 15 + 5*5))
    
    for i, data in enumerate(tempat_wisata, 1):
        ketersediaan = 'Tersedia' if data[2] > 0 else 'Penuh'
        print(f"{i:<5} {data[0]:<30} {data[1]:<15} {data[2]:<10} {'Rp ' + format(data[3], ','):<15} {ketersediaan:<15}")
    
    pilihan = get_valid_int("Pilih nomor tempat wisata untuk pesan tiket: ")
    if pilihan < 1 or pilihan > len(tempat_wisata):
        print("Error: Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")
        return
    
    index = pilihan - 1
    if tempat_wisata[index][2] <= 0:
        print("Maaf, kuota untuk tempat ini sudah penuh!")
        input("Tekan Enter untuk kembali...")
        return
    
    jumlah_tiket = get_valid_int("Masukkan jumlah tiket yang diinginkan: ")
    if jumlah_tiket > tempat_wisata[index][2]:
        print(f"Error: Kuota tersedia hanya {tempat_wisata[index][2]} tiket!")
        input("Tekan Enter untuk kembali...")
        return
    
    tempat_wisata[index][2] -= jumlah_tiket  
    total_harga = jumlah_tiket * tempat_wisata[index][3]
    print(f"Pemesanan berhasil! Anda memesan {jumlah_tiket} tiket untuk {tempat_wisata[index][0]}.")
    print(f"Total harga: Rp {total_harga:,}")
    print(f"Kuota tersisa: {tempat_wisata[index][2]}")
    input("Tekan Enter untuk kembali...")

def update_wisata():
    clear_screen()
    print("=== UPDATE TEMPAT WISATA ===")
    if not tempat_wisata:
        print("Tidak ada data untuk diupdate.")
        input("Tekan Enter untuk kembali...")
        return
    
    for i, data in enumerate(tempat_wisata, 1):
        print(f"{i}. {data[0]}")
    
    pilihan = get_valid_int("Pilih nomor tempat untuk update: ")
    if pilihan < 1 or pilihan > len(tempat_wisata):
        print("Error: Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")
        return
    
    index = pilihan - 1
    print(f"\nData saat ini: {tempat_wisata[index]}")
    
    print("1. Ubah kuota pengunjung")
    print("2. Ubah harga tiket")
    print("3. Ubah jadwal")
    print("4. Ubah deskripsi")
    sub_pilihan = get_valid_int("Pilih field untuk update (1-4): ")
    
    if sub_pilihan == 1:
        new_kuota = get_valid_int("Kuota baru: ")
        tempat_wisata[index][2] = new_kuota
    elif sub_pilihan == 2:
        new_harga = get_valid_int("Harga baru: ")
        tempat_wisata[index][3] = new_harga
    elif sub_pilihan == 3:
        new_jadwal = get_valid_string("Jadwal baru: ")
        tempat_wisata[index][1] = new_jadwal
    elif sub_pilihan == 4:
        new_desk = get_valid_string("Deskripsi baru: ")
        tempat_wisata[index][4] = new_desk
    else:
        print("Error: Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")
        return
    
    print("Update berhasil!")
    input("Tekan Enter untuk kembali...")

def delete_wisata():
    clear_screen()
    print("=== HAPUS TEMPAT WISATA ===")
    if not tempat_wisata:
        print("Tidak ada data untuk dihapus.")
        input("Tekan Enter untuk kembali...")
        return
    
    for i, data in enumerate(tempat_wisata, 1):
        print(f"{i}. {data[0]}")
    
    pilihan = get_valid_int("Pilih nomor tempat untuk hapus: ")
    if pilihan < 1 or pilihan > len(tempat_wisata):
        print("Error: Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")
        return
    
    confirm = input(f"Yakin hapus '{tempat_wisata[pilihan-1][0]}'? (y/n): ").strip().lower()
    if confirm == 'y':
        del tempat_wisata[pilihan - 1]
        print("Hapus berhasil!")
    else:
        print("Batal hapus.")
    
    input("Tekan Enter untuk kembali...")

# Program utama
def main():
    clear_screen()
    print("Selamat datang di Program Manajemen Tempat Wisata!")
    
    while True:
        print("\n1. Login")
        print("2. Register")
        print("3. Keluar")
        choice = input("Pilih (1-3): ").strip()
        
        if choice == '1':
            role = login()
            if role:
                while True:
                    menu_choice = show_main_menu(role)
                    if menu_choice == 1:
                        if role == "admin":
                            create_wisata()
                        else:
                            read_wisata(role)
                    elif menu_choice == 2:
                        if role == "admin":
                            read_wisata(role)
                        else:  # User
                            book_tiket()
                    elif menu_choice == 3:
                        if role == "admin":
                            update_wisata()
                        else:
                            break  
                    elif menu_choice == 4 and role == "admin":
                        delete_wisata()
                    elif menu_choice == 5 and role == "admin":
                        break
        elif choice == '2':
            register()
        elif choice == '3':
            print("Kembali ke menu utama.")
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk lanjut...")

if __name__ == "__main__":
    main()