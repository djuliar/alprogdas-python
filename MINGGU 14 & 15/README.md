### **Materi: Init Database Read, Create, Update, dan Delete dalam Pemrograman Python**

Dalam pemrograman Python, operasi **CRUD** (Create, Read, Update, Delete) merupakan dasar dalam pengelolaan database. Operasi ini digunakan untuk memanipulasi data dalam database, seperti SQLite, MySQL, atau PostgreSQL. 

Python menyediakan berbagai library untuk berinteraksi dengan database, salah satunya adalah **SQLite** melalui modul bawaan `sqlite3`.

---

### **1. Tahap Awal: Init Database**
Sebelum melakukan operasi CRUD, kita perlu:
1. Menginisialisasi koneksi ke database.
2. Membuat tabel jika belum ada.

Contoh:
```python
import sqlite3

# Inisialisasi koneksi ke database
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Membuat tabel jika belum ada
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")
conn.commit()
print("Database initialized.")
```

---

### **2. Operasi CRUD**
#### **(a) Create - Menambahkan Data**
Menambahkan data baru ke tabel menggunakan query `INSERT INTO`.

```python
def create_user(name, age):
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    print(f"User '{name}' added.")

# Contoh penggunaan
create_user("Alice", 25)
create_user("Bob", 30)
```

#### **(b) Read - Membaca Data**
Mengambil data dari tabel menggunakan query `SELECT`.

```python
def read_users():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Contoh penggunaan
print("User List:")
read_users()
```

#### **(c) Update - Memperbarui Data**
Memperbarui data di tabel menggunakan query `UPDATE`.

```python
def update_user(user_id, name, age):
    cursor.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, user_id))
    conn.commit()
    print(f"User with ID {user_id} updated.")

# Contoh penggunaan
update_user(1, "Alice Smith", 26)
```

#### **(d) Delete - Menghapus Data**
Menghapus data dari tabel menggunakan query `DELETE`.

```python
def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    print(f"User with ID {user_id} deleted.")

# Contoh penggunaan
delete_user(2)
```

---

### **Studi Kasus: Manajemen Data Pengguna**
Bayangkan Anda memiliki aplikasi untuk mengelola daftar pengguna dengan fitur:
1. Menambahkan pengguna baru.
2. Menampilkan daftar pengguna.
3. Memperbarui data pengguna.
4. Menghapus pengguna.

Berikut implementasinya:
```python
def menu():
    while True:
        print("\n=== User Management Menu ===")
        print("1. Add User")
        print("2. View Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            create_user(name, age)
        elif choice == "2":
            print("User List:")
            read_users()
        elif choice == "3":
            user_id = int(input("Enter user ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            update_user(user_id, name, age)
        elif choice == "4":
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Jalankan aplikasi
menu()

# Jangan lupa menutup koneksi
conn.close()
```

---

### **Penjelasan Studi Kasus**
1. **Init Database**: Koneksi ke database dan pembuatan tabel dilakukan hanya sekali di awal.
2. **Create**: Data pengguna baru disimpan ke database.
3. **Read**: Daftar pengguna ditampilkan di layar.
4. **Update**: Data pengguna dapat diperbarui berdasarkan ID.
5. **Delete**: Pengguna dapat dihapus berdasarkan ID.

### **Output:**
- Pengguna dapat dengan mudah mengelola data melalui menu interaktif.
- Semua operasi CRUD akan langsung tercermin dalam database.

Ini adalah contoh sederhana yang dapat dikembangkan lebih lanjut, seperti menambahkan validasi atau menggunakan framework seperti SQLAlchemy atau Django ORM untuk kemudahan pengelolaan database.