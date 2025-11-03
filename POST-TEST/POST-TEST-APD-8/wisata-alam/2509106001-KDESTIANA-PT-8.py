from prettytable import PrettyTable
from login import login, register, clear_screen
from sistem import admin, user

def tampilkan_menu():
    table = PrettyTable()
    table.title = "MAIN MENU"
    table.field_names = ["No", "Menu"]
    table.align = "l"
    table.add_row(["1", "Login"])
    table.add_row(["2", "Register"])
    table.add_row(["3", "Keluar"])
    print(table)

def main():
    while True:
        clear_screen()
        tampilkan_menu()
        pilih = input("\nPilih Menu (1/2/3): ").strip()
        if pilih == "1":
            user_data = login()
            if user_data:
                if user_data["role"] == "admin":
                    admin(user_data["username"])
                else:
                    user(user_data["username"])
        elif pilih == "2":
            register()
            input("\nTekan Enter untuk kembali...")
        elif pilih == "3":
            clear_screen()
            print("Terima kasih sudah menggunakan Sistem kami :)\n\tHave a nice day!")
            break
        else:
            print("\nPilihan tidak valid!")
            input("Tekan Enter untuk lanjut...")

if __name__ == "__main__":
    main()