import sys
username = input("Username: ")
password = input("Password: ")

login_success = username == 'desti' and password == '001'

if not login_success:
    print("Error: Login gagal.")
    sys.exit()

print(f"Login berhasil, {username}.")

is_member_input = input("Apakah Anda member? (y/n): ").lower().strip()
is_member = is_member_input == 'y'

print("\nMENU: 1. ayam geprek - 16000 2. es teh - 5000 3. jus alpukat - 17000")

pilihan = int(input("Pilih (1-3): "))
quantity = int(input("Quantity: "))

if pilihan == 1:
    harga = 16000
elif pilihan == 2:
    harga = 5000
else:
    harga = 17000

total = quantity * harga

if is_member:
    diskon = total * 0.15
    harga_akhir = total - diskon
    print(f"\nSebelum: Rp{total:,} Diskon: Rp{diskon:,.0f} Akhir: Rp{harga_akhir:,.0f}")
else:
    print(f"\nTotal: Rp{total:,}")