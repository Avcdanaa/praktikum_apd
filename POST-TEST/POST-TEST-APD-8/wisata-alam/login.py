import os
from data import users

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def login():
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    if not username or not password:
        print("Error: Username dan password tidak boleh kosong!")
        return None
    if username in users and users[username]["password"] == password:
        return {"username": username, "role": users[username]["role"]}
    print("Error: Username atau password salah!")
    return None

def register():
    username = input("Username baru: ").strip()
    if not username:
        print("Error: Username tidak boleh kosong!")
        return False
    if username in users:
        print("Error: Username sudah terdaftar!")
        return False
    password = input("Password: ").strip()
    if not password:
        print("Error: Password tidak boleh kosong!")
        return False
    users[username] = {"password": password, "role": "user"}
    print("Registrasi berhasil! Silakan login.")
    return True