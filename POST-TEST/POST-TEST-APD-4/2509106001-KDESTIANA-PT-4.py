import sys
import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== SELAMAT DATANG DI SISTEM BELANJA JUS ===")
    while True:
        is_member_input = input("Apakah Anda member? (yes/no): ").strip().lower()
        if is_member_input:
            break
        print("Input tidak boleh kosong atau hanya spasi. Coba lagi.")
    
    is_member = False
    if is_member_input == 'yes':
        max_attempts = 3
        for attempt in range(1, max_attempts + 1):
            while True:
                username = input("Username: ").strip()
                if username:
                    break
                print("Input tidak boleh kosong atau hanya spasi. Coba lagi.")
            
            password = input("Password: ").strip()
            if not password:
                print("Password tidak boleh kosong.")
                continue
            
            if username == 'Desti' and password == '001':
                print("Login successful")
                is_member = True
                break
            else:
                remaining = max_attempts - attempt
                if remaining > 0:
                    print(f"Login failed. Sisa percobaan: {remaining}")
                else:
                    print("Login failed setelah 3 percobaan. Anda akan dianggap sebagai non-member.")
        if not is_member:
            print("Melanjutkan sebagai non-member (tanpa diskon).")
    else:
        print("Melanjutkan sebagai non-member (tanpa diskon).")

    keranjang = ""  
    total = 0
    while True:
        print(f"\n┌{'─'*48}┐")
        print(f"│{'MENU':^48}│")
        print(f"├{'─'*48}┤")
        print(f"│{'No':<4}{'Menu Item':<24}{'Price':<20}│")
        print(f"├{'─'*48}┤")
        print(f"│{'1':<4}{'jus tomato':<24}{'Rp10.000':<20}│")
        print(f"│{'2':<4}{'air kelapa':<24}{'Rp14.000':<20}│")
        print(f"│{'3':<4}{'jus alpukat':<24}{'Rp17.000':<20}│")
        print(f"│{'4':<4}{'Checkout':<24}{'Selesaikan Belanja':<20}│")
        print(f"└{'─'*48}┘")
        
        while True:
            pilihan_input = input("Pilih (1-4): ").strip()
            if pilihan_input:
                break
            print("Input tidak boleh kosong atau hanya spasi. Coba lagi.")
        
        if not pilihan_input.isdigit() or int(pilihan_input) not in [1, 2, 3, 4]:
            print("Pilihan tidak valid. Masukkan 1-4.")
            continue
        pilihan = int(pilihan_input)
        
        if pilihan == 4:
            if not keranjang.strip():  # Check if keranjang empty
                print("Keranjang kosong. Tidak ada transaksi.")
                break
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\n┌{'─'*60}┐") 
            print(f"│{'STRUK PEMBELIAN':^60}│")
            print(f"├{'─'*60}┤")
            print(f"│{'Item':<30}{'Qty':<5}{'Harga':<10}{'Subtotal':<15}│")
            print(f"├{'─'*60}┤")
            
            items_lines = keranjang.strip().split('\n')
            for line in items_lines:
                if line.strip(): 
                    padded_line = line.ljust(60)
                    print(f"│{padded_line}│")
            
            if is_member:
                print(f"├{'─'*60}┤")
                print(f"│{'Subtotal':<45}{f'Rp{total:,}':<15}│")
                diskon = round(total * 0.15, 0)  
                harga_akhir = total - diskon
                print(f"│{'Diskon (15%)':<45}{f'-Rp{diskon:,.0f}':<15}│")
                print(f"├{'─'*60}┤")
                print(f"│{'TOTAL BAYAR':<45}{f'Rp{harga_akhir:,.0f}':<15}│")
            else:
                print(f"├{'─'*60}┤")
                print(f"│{'TOTAL BAYAR':<45}{f'Rp{total:,}':<15}│")
            
            print(f"└{'─'*60}┘")
            break
        elif pilihan in [1, 2, 3]:
            while True:
                quantity_input = input("Quantity: ").strip()
                if quantity_input:
                    break
                print("Input tidak boleh kosong atau hanya spasi. Coba lagi.")
            
            if not quantity_input.isdigit() or int(quantity_input) <= 0:
                print("Quantity harus lebih dari 0 dan angka valid.")
                continue
            quantity = int(quantity_input)
            
            if pilihan == 1:
                name = "jus tomato"
                price = 10000
            elif pilihan == 2:
                name = "air kelapa"
                price = 14000
            elif pilihan == 3:
                name = "jus alpukat"
                price = 17000
            else:
                total, keranjang = total, keranjang  
                continue
            
            subtotal = quantity * price
            item_detail = f"{name:<30}{f'{quantity}x':<5}{f'Rp{price:,}':<10}{f'Rp{subtotal:,}':<15}\n"
            keranjang += item_detail
            total += subtotal
            print(f"{quantity}x {name} berhasil ditambahkan ke keranjang!")
            print(f"Total sementara: Rp{total:,}")
    
    while True:
        new_txn = input("\nIngin memulai transaksi baru? (yes/no): ").strip().lower()
        if new_txn:
            break
        print("Input tidak boleh kosong atau hanya spasi. Coba lagi.")
    
    if new_txn != 'yes':
        print("Terima kasih! Telah Berbelanja.")
        sys.exit()