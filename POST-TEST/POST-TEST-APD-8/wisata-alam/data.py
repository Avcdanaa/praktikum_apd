tempat_wisata = {
    "Air Terjun Jantur Inar": {"jadwal": "08:00 - 16:00", "kuota": 100, "harga": 25000, "deskripsi": "Air yang deras mengalir dari atas tebing dan jatuh dengan gemuruh yang menggetarkan hati."},
    "Gunung S": {"jadwal": "04:00 - 18:00", "kuota": 150, "harga": 15000, "deskripsi": "Gunung S memiliki keunikan tak hanya terletak pada pemandangannya yang menakjubkan, namun juga pada suasana bak Negeri di Atas Awan."},
    "Lakam Bilem": {"jadwal": "08:00 - 16:00", "kuota": 200, "harga": 35000, "deskripsi": "Lakam Bilem bukan hanya memiliki sungai yang terus mengalir namun banyak opsi yang bisa kita nikmati seperti arung jeram, goa kelelawar, dan Bumi Perkemahan batu Bura."}
}

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user1": {"password": "user123", "role": "user"}
}

def hitung_total_harga(jumlah, harga):
    return jumlah * harga

def cari_tempat_wisata(kata):
    hasil = []
    for nama, data in tempat_wisata.items():
        if kata.lower() in nama.lower():
            hasil.append((nama, data))
    return hasil