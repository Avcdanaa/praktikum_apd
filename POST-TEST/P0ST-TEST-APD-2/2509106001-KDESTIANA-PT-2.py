# input data dari pasien
namapasien = str(input("masukan nama pasien: "))
tinggibadan = int(input("masukan tinggi badan 'cm' : "))
beratbadan = int(input("masukan berat badan 'kg' : "))

# hitung berat badan ideal dan status
beratbadanideal = tinggibadan - 100
iskelebihan  = beratbadan > beratbadanideal

# gunakan list untuk status
statusList = ["berat badan normal", "kelebihan berat badan"]
status = statusList[int(iskelebihan)]

#output hasil tabel
print("-" * 70)
print("|{:^68}|".format("HASIL CEK BERAT BADAN"))
print("-" * 70)
print(f"| {'Nama Pasien':<20}: {namapasien:<45}|")
print(f"| {'Tinggi Badan':<20}: {tinggibadan:<42} cm|")
print(f"| {'Berat Badan':<20}: {beratbadan:<42} kg|")
print(f"| {'Berat Ideal':<20}: {beratbadanideal:<42} kg|")
print(f"| {'Status':<20}: {statusList[int(iskelebihan)]:<45}|")
print("-" * 70)
