import hashlib
import getpass
import sqlite3

conn = sqlite3.connect('password_manager.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)''')
conn.commit()

def buat_akun():
    username = input("masukkan username: ")
    password = getpass.getpass("masukkan password: ")
    hashed_pass = hashlib.sha256(password.encode()).hexdigest()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pass))
        conn.commit()
        print("Akun berhasil dibuat")
    except sqlite3.IntegrityError:
        print("Username sudah ada, coba username lain")
    
def login():
    username = input("masukkan username: ")
    password = getpass.getpass("masukkan password: ")
    hashed_pass = hashlib.sha256(password.encode()).hexdigest()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_pass))
    result = c.fetchone()
    if result:
        print("Login sukses")
    else:
        print("Username atau password invalid")
        
def main():
    while True:
        choice = input("masukkan 1 untuk buat akun, 2 untuk login dan 0 untuk keluar: ")
        if choice == "1":
            buat_akun()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else: 
            print("inavlid input")

if __name__ == '__main__':
    main()

conn.close()