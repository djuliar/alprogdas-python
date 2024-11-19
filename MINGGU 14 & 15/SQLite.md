### **Materi: Membuat Database dengan SQLite dalam Pemrograman Python**

SQLite adalah database ringan yang tidak memerlukan server terpisah. SQLite sangat cocok digunakan untuk aplikasi skala kecil hingga menengah dan memiliki keunggulan karena telah terintegrasi langsung dengan Python melalui modul bawaan **`sqlite3`**.

---

### **1. Konsep Dasar SQLite**
- **Database**: Tempat penyimpanan data terstruktur.
- **Tabel**: Struktur dalam database yang berisi data dalam bentuk baris (row) dan kolom (column).
- **Field**: Kolom dalam tabel yang menyimpan atribut dari data.
- **Primary Key**: Identitas unik untuk membedakan setiap baris data.

---

### **2. Membuat Database dengan SQLite**

#### **Langkah-Langkah:**
1. **Import Modul `sqlite3`**:
   Library bawaan Python untuk mengelola SQLite.
2. **Membuat atau Menghubungkan ke File Database**:
   Database otomatis dibuat jika file belum ada.
3. **Membuat Tabel**:
   Menggunakan perintah SQL `CREATE TABLE`.

---

#### **Contoh Dasar Membuat Database**
```python
import sqlite3

# Membuat atau menghubungkan ke database
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Membuat tabel jika belum ada
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    salary REAL NOT NULL
)
""")
conn.commit()
print("Database dan tabel berhasil dibuat.")

# Tutup koneksi
conn.close()
```

Penjelasan:
1. **`connect("example.db")`**: Membuat file database `example.db` jika belum ada.
2. **`CREATE TABLE`**: Membuat tabel `employees` dengan kolom:
   - `id`: Kunci utama, auto-increment.
   - `name`: Nama karyawan (teks).
   - `position`: Jabatan (teks).
   - `salary`: Gaji (angka desimal).
3. **`commit()`**: Menyimpan perubahan ke database.

---

### **3. Studi Kasus: Sistem Manajemen Karyawan**

#### **Deskripsi Kasus**
Anda diminta membuat sistem sederhana untuk mengelola data karyawan dengan fitur:
1. Membuat database karyawan.
2. Menambahkan data karyawan.
3. Melihat daftar karyawan.
4. Menghapus data karyawan.

#### **Kode Program Lengkap**
```python
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
```

---

### **Penjelasan Fitur**
1. **Inisialisasi Database**:
   - Fungsi `init_db()` membuat database dan tabel jika belum ada.
2. **Menambahkan Data**:
   - `add_employee()` menyisipkan data baru ke tabel.
3. **Melihat Data**:
   - `view_employees()` menampilkan semua data dari tabel.
4. **Menghapus Data**:
   - `delete_employee()` menghapus data berdasarkan ID.

---

### **Contoh Output Program**
1. **Menambahkan Data:**
   ```
   Masukkan nama: Alice
   Masukkan posisi: Manager
   Masukkan gaji: 8000000
   Karyawan 'Alice' berhasil ditambahkan.
   ```

2. **Melihat Data:**
   ```
   Daftar Karyawan:
   ID: 1, Nama: Alice, Posisi: Manager, Gaji: 8000000
   ```

3. **Menghapus Data:**
   ```
   Masukkan ID karyawan yang ingin dihapus: 1
   Karyawan dengan ID 1 berhasil dihapus.
   ```

---

### **Keuntungan SQLite**
- **Ringan**: Tidak memerlukan server tambahan.
- **Integrasi Mudah**: Python menyediakan dukungan bawaan.
- **Ideal untuk Prototyping**: Mudah digunakan untuk membangun aplikasi sederhana.

Kode ini bisa dikembangkan lebih lanjut, seperti menambahkan validasi input atau fitur pencarian karyawan.