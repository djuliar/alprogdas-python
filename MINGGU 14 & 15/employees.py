import sqlite3

# Membuat koneksi dan tabel database
def init_db():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        position TEXT NOT NULL,
        salary REAL NOT NULL
    )
    """)
    conn.commit()
    conn.close()
    print("Database dan tabel berhasil diinisialisasi.")

# Menambahkan data karyawan
def add_employee(name, position, salary):
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)", (name, position, salary))
    conn.commit()
    conn.close()
    print(f"Karyawan '{name}' berhasil ditambahkan.")

# Melihat daftar karyawan
def view_employees():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    conn.close()
    if rows:
        print("\nDaftar Karyawan:")
        for row in rows:
            print(f"ID: {row[0]}, Nama: {row[1]}, Posisi: {row[2]}, Gaji: {row[3]}")
    else:
        print("\nBelum ada data karyawan.")

# Menghapus data karyawan
def delete_employee(employee_id):
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
    conn.commit()
    conn.close()
    print(f"Karyawan dengan ID {employee_id} berhasil dihapus.")

# Menu interaktif
def menu():
    init_db()
    while True:
        print("\n=== Sistem Manajemen Karyawan ===")
        print("1. Tambah Karyawan")
        print("2. Lihat Karyawan")
        print("3. Hapus Karyawan")
        print("4. Keluar")

        choice = input("Pilih opsi: ")
        if choice == "1":
            name = input("Masukkan nama: ")
            position = input("Masukkan posisi: ")
            salary = float(input("Masukkan gaji: "))
            add_employee(name, position, salary)
        elif choice == "2":
            view_employees()
        elif choice == "3":
            employee_id = int(input("Masukkan ID karyawan yang ingin dihapus: "))
            delete_employee(employee_id)
        elif choice == "4":
            print("Keluar dari sistem.")
            break
        else:
            print("Pilihan tidak valid.")

# Menjalankan program
menu()