is_member_input = input("Apakah Anda member? (yes/no): ").lower().strip()

if is_member_input != 'yes':
    print(f"exit")
else:
    username = input("Username: ")
    password = input("Password: ")
    auth_status = "Login successful" if username == "Desti" and password == "001" else "Login failed"
    print(f"{auth_status}")
    
    if auth_status == "Login successful":
        # Tabel Menu dengan border lengkap
        print(f"\n┌{'─'*48}┐")
        print(f"│{'MENU':^48}│")
        print(f"├{'─'*48}┤")
        print(f"│{'No':<4}{'Menu Item':<24}{'Price':<20}│")
        print(f"├{'─'*48}┤")
        print(f"│{'1':<4}{'jus tomato':<24}{'Rp10.000':<20}│")
        print(f"│{'2':<4}{'air kelapa':<24}{'Rp14.000':<20}│")
        print(f"│{'3':<4}{'jus alpukat':<24}{'Rp17.000':<20}│")
        print(f"└{'─'*48}┘")
        
        pilihan = int(input("Pilih (1-3): "))
        quantity = int(input("Quantity: "))
        
        if pilihan == 1:
            harga = 10000
            item_name = "jus tomat"
        elif pilihan == 2:
            harga = 14000
            item_name = "air kelapa"
        else:
            harga = 17000
            item_name = "jus alpukat"
        
        total = quantity * harga
        diskon = total * 0.15
        harga_akhir = total - diskon
        
        # Tabel Struk dengan border lengkap
        print(f"\n┌{'─'*50}┐")
        print(f"│{'STRUK PEMBELIAN':^50}│")
        print(f"├{'─'*50}┤")
        print(f"│{'Item':<22}{'Qty':<6}{'Harga':<12}{'Total':<10}│")
        print(f"├{'─'*50}┤")
        print(f"│{item_name:<22}{quantity:<6}{f'Rp{harga:,}':<12}{f'Rp{total:,}':<10}│")
        print(f"├{'─'*50}┤")
        print(f"│{'Subtotal':<34}{'Rp{total:,}':<16}│")
        print(f"│{'Diskon (15%)':<34}{f'-Rp{diskon:,.0f}':<16}│")
        print(f"├{'─'*50}┤")
        print(f"│{'TOTAL BAYAR':<34}{f'Rp{harga_akhir:,.0f}':<16}│")
        print(f"└{'─'*50}┘")
    else:
        print(f"exit")