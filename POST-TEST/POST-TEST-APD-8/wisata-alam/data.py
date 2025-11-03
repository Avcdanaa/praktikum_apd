tempat_wisata = {
    "Air Terjun Jantur Inar": {"jadwal": "08:00 - 16:00", "kuota": 100, "harga": 25000, "deskripsi": "Air yang deras mengalir dari atas tebing dan jatuh dengan gemuruh yang menggetarkan hati. Suara gemuruh air terjun yang indah mengalir dalam keheningan hutan, menciptakan suasana yang menenangkan dan menyejukkan jiwa. Keindahan ini menarik perhatian para wisatawan yang ingin menjauh sejenak dari hiruk-pikuk kehidupan perkotaan."},
    "Gunung S": {"jadwal": "04:00 - 18:00", "kuota": 150, "harga": 15000, "deskripsi": "Gunung S memiliki keunikan tak hanya terletak pada pemandangannya yang menakjubkan, namun juga pada suasana bak Negeri di Atas Awan Selain itu, kamu juga bisa mencoba olahraga paralayang. Gunung S menjadi lokasi favorit bagi atlet paralayang nasional untuk mengeksplorasi keindahan alam Kutai Barat dari ketinggian."},
    "Lakam Bilem": {"jadwal": "08:00 - 16:00", "kuota": 200, "harga": 35000, "deskripsi": "Lakam Bilem bukan hanya memiliki sungai yang terus mengalir namun banyak opsi yang bisa kita nikmati seperti arung jeram, goa kelelawar, dan Bumi Perkemahan batu Bura."}
}

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user1": {"password": "user123", "role": "user"}
}

def hitung_total_kuota(index=0, total=0):
    if index >= len(tempat_wisata):
        return total
    nama = list(tempat_wisata.keys())[index]
    total += tempat_wisata[nama]["kuota"]
    return hitung_total_kuota(index + 1, total)

def hitung_total_harga(jumlah_tiket, harga_per_tiket):
    return jumlah_tiket * harga_per_tiket

def cari_tempat_wisata(nama_cari):
    hasil = []
    for nama, data in tempat_wisata.items():
        if nama_cari.lower() in nama.lower():
            hasil.append((nama, data))
    return hasil

def jumlah_tempat_wisata():
    return len(tempat_wisata)