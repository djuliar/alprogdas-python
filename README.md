### Materi Fundamental dan Pengantar Tentang Pemrograman Dasar Python

#### **1. Apa Itu Python?**
Python adalah bahasa pemrograman tingkat tinggi yang banyak digunakan karena kesederhanaan sintaksisnya, kemudahan dibaca, dan kemampuannya menangani berbagai jenis aplikasi, mulai dari web development hingga data science. Python bersifat **interpreted** (dieksekusi baris per baris) dan **dynamically typed** (tipe data tidak perlu dideklarasikan), menjadikannya pilihan populer untuk pemula maupun pengembang berpengalaman.

#### **2. Kelebihan Python**
- **Sintaks sederhana**: Python dirancang agar mudah dibaca dan ditulis.
- **Portabilitas**: Dapat berjalan di berbagai sistem operasi seperti Windows, Linux, dan macOS.
- **Dukungan komunitas luas**: Tersedia banyak pustaka dan modul yang dapat digunakan untuk berbagai kebutuhan.
- **Cocok untuk berbagai aplikasi**: Python digunakan di berbagai bidang, termasuk pengembangan web, kecerdasan buatan, otomatisasi skrip, hingga analisis data.

---

### **3. Instalasi Python**
Untuk memulai, instal Python dari situs resminya [python.org](https://www.python.org/). Pastikan untuk memilih versi terbaru dan tambahkan Python ke **PATH** agar bisa diakses melalui terminal atau command prompt.

---

### **4. Memulai Program Python Pertama**

Mari kita mulai dengan program dasar yang paling terkenal di dunia pemrograman, yaitu **Hello, World!**:

```python
print("Hello, World!")
```

- **Penjelasan**: `print()` adalah fungsi bawaan di Python yang digunakan untuk mencetak teks atau output ke layar.

---

### **5. Tipe Data Dasar di Python**
Python mendukung berbagai jenis tipe data dasar, seperti:

1. **Integer**: Angka bulat.
   - Contoh: `10`, `-5`, `0`
   
2. **Float**: Angka desimal atau pecahan.
   - Contoh: `3.14`, `-7.5`

3. **String**: Sekumpulan karakter yang diapit tanda kutip (`'` atau `"`).
   - Contoh: `'Hello'`, `"Python is fun!"`

4. **Boolean**: Tipe data yang hanya memiliki dua nilai: `True` atau `False`.
   - Contoh: `True`, `False`

5. **List**: Sekumpulan data yang bisa memiliki berbagai tipe data dan diubah ukurannya.
   - Contoh: `[1, 2, 3, 'Python']`

6. **Dictionary**: Struktur data yang menyimpan pasangan kunci-nilai.
   - Contoh: `{'name': 'John', 'age': 25}`

---

### **6. Variabel dan Penugasan**

Variabel adalah tempat penyimpanan data yang dapat diakses dan diubah selama program berjalan. Di Python, variabel tidak memerlukan deklarasi tipe data secara eksplisit.

#### Contoh:

```python
# Penugasan variabel
x = 10         # Integer
y = 3.14       # Float
nama = "John"  # String
```

- **Penjelasan**: `x`, `y`, dan `nama` adalah variabel yang menyimpan nilai-nilai data tertentu.

---

### **7. Operator dalam Python**

Operator digunakan untuk melakukan operasi pada variabel dan nilai. Berikut beberapa jenis operator:

1. **Operator Aritmatika**:
   - `+` (Penjumlahan), `-` (Pengurangan), `*` (Perkalian), `/` (Pembagian), `**` (Eksponen), `//` (Pembagian bulat), `%` (Modulus)
   
   **Contoh**:
   ```python
   a = 5
   b = 2
   print(a + b)  # Hasil: 7
   print(a * b)  # Hasil: 10
   ```

2. **Operator Perbandingan**:
   - `==`, `!=`, `>`, `<`, `>=`, `<=`

   **Contoh**:
   ```python
   print(5 > 3)   # True
   print(5 == 3)  # False
   ```

3. **Operator Logika**:
   - `and`, `or`, `not`
   
   **Contoh**:
   ```python
   print(True and False)  # False
   print(True or False)   # True
   ```

---

### **8. Struktur Kontrol**

Struktur kontrol digunakan untuk mengatur alur eksekusi program. Python mendukung berbagai struktur kontrol seperti:

#### a. **Kondisi `if else`**

Kondisi `if else` digunakan untuk membuat keputusan berdasarkan suatu kondisi tertentu.

**Contoh**:

```python
x = 10

if x > 5:
    print("x lebih besar dari 5")
else:
    print("x kurang dari atau sama dengan 5")
```

#### b. **Perulangan `for` dan `while`**

1. **Perulangan `for`** digunakan untuk mengulang sejumlah langkah tertentu.
   **Contoh**:
   ```python
   for i in range(5):
       print(i)
   ```

2. **Perulangan `while`** digunakan untuk mengulang langkah selama suatu kondisi bernilai benar.
   **Contoh**:
   ```python
   i = 0
   while i < 5:
       print(i)
       i += 1
   ```

---

### **9. Fungsi dalam Python**

Fungsi adalah sekumpulan instruksi yang dapat dipanggil berulang-ulang. Python memungkinkan kita mendefinisikan fungsi menggunakan kata kunci **`def`**.

#### Contoh:

```python
def hello(nama):
    print(f"Hello, {nama}!")

# Memanggil fungsi
hello("John")
```

Penjelasan:
- **`def`** digunakan untuk mendefinisikan fungsi bernama `hello`.
- Parameter `nama` digunakan untuk menerima input ketika fungsi dipanggil.

---

### **10. Input dan Output**

Untuk menerima input dari pengguna, kita bisa menggunakan fungsi **`input()`**, sedangkan untuk menampilkan output kita menggunakan **`print()`**.

#### Contoh Input:

```python
nama = input("Masukkan nama Anda: ")
print(f"Hello, {nama}!")
```

Penjelasan:
- **`input()`** digunakan untuk mengambil input dari pengguna dalam bentuk string.
- **`print()`** untuk menampilkan hasil ke layar.

---

### **11. Contoh Studi Kasus: Program Hitung Luas Lingkaran**

Misalkan kita ingin membuat program untuk menghitung luas lingkaran dengan rumus **Luas = π * r²**, di mana `r` adalah jari-jari lingkaran dan `π` adalah 3.14.

#### Contoh Program:

```python
# Program hitung luas lingkaran
r = float(input("Masukkan jari-jari lingkaran: "))
pi = 3.14
luas = pi * r ** 2
print(f"Luas lingkaran dengan jari-jari {r} adalah {luas}")
```

Penjelasan:
- Pengguna memasukkan nilai jari-jari.
- Program menggunakan rumus `π * r²` untuk menghitung luas lingkaran.

---

### **12. Penutup**

Python adalah bahasa pemrograman yang sangat cocok untuk pemula karena sintaksnya yang sederhana dan kemampuannya yang fleksibel. Dalam pemrograman dasar Python, kita belajar tentang tipe data, variabel, operator, struktur kontrol, fungsi, dan cara menerima input dan memberikan output.