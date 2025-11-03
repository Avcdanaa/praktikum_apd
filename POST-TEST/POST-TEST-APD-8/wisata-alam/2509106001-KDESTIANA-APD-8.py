import sys
import time
from login import login, register, clear_screen
from sistem import admin, user

def main():
    while True:
        clear_screen()
        print("-" * 11, "Main Menu", "-" * 11, "\n1. Login\n2. Register\n0. Keluar")
        
        pilih = input("\nPilih Menu: ")
        
        if pilih == "1":
            user_data = login()
            if user_data:
                if user_data["role"] == "admin":
                    admin(user_data["username"])
                else:
                    user(user_data["username"])
        elif pilih == "2":
            register()
        elif pilih == "0":
            clear_screen()
            kalimat = "Terimakasih sudah menggunakan Sistem kami:)\n\tHave a nice day!"
            for char in kalimat:
                sys.stdout.write(char)
                time.sleep(0.03)
            break
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()