### Materi: **Penggunaan List (Array) dalam Pemrograman Python**

---

#### 1. **Apa itu List (Array)?**
Dalam pemrograman Python, **list** adalah tipe data yang digunakan untuk menyimpan kumpulan data yang bisa diubah (mutable) dan berurutan. List bisa menyimpan berbagai tipe data, baik itu integer, string, float, atau bahkan list lainnya.

Sementara itu, dalam bahasa pemrograman lain seperti C atau Java, kita sering menggunakan istilah "array". Namun, di Python, kita menggunakan list sebagai struktur data serupa, meskipun Python juga memiliki modul `array` untuk keperluan tertentu.

##### Contoh List di Python:
```python
# Membuat list kosong
my_list = []

# Membuat list dengan elemen
my_list = [1, 2, 3, 4, 5]

# List dengan berbagai tipe data
mixed_list = [1, "Hello", 3.14, True]
```

---

#### 2. **Operasi Dasar pada List**

##### a. **Mengakses Elemen dalam List**
Setiap elemen dalam list memiliki indeks, dimulai dari 0 untuk elemen pertama. Kita bisa mengakses elemen dengan menggunakan indeks tersebut.
```python
my_list = [10, 20, 30, 40, 50]

# Mengakses elemen pertama
print(my_list[0])  # Output: 10

# Mengakses elemen terakhir
print(my_list[-1])  # Output: 50
```

##### b. **Menambahkan Elemen ke List**
Kita bisa menambahkan elemen baru ke dalam list menggunakan metode `append()` atau `insert()`.
```python
my_list = [1, 2, 3]

# Menambahkan elemen di akhir list
my_list.append(4)  # my_list menjadi [1, 2, 3, 4]

# Menambahkan elemen di posisi tertentu
my_list.insert(1, 10)  # my_list menjadi [1, 10, 2, 3, 4]
```

##### c. **Menghapus Elemen dari List**
Elemen bisa dihapus menggunakan `remove()` atau `pop()`.
```python
my_list = [1, 2, 3, 4]

# Menghapus elemen tertentu
my_list.remove(3)  # Menghapus elemen pertama yang nilainya 3, my_list menjadi [1, 2, 4]

# Menghapus elemen berdasarkan indeks
my_list.pop(1)  # Menghapus elemen kedua, my_list menjadi [1, 4]
```

##### d. **Mengubah Elemen dalam List**
Elemen list dapat diubah dengan langsung menetapkan nilai baru berdasarkan indeks.
```python
my_list = [10, 20, 30]

# Mengubah elemen pertama
my_list[0] = 100  # my_list menjadi [100, 20, 30]
```

---

#### 3. **Looping Melalui List**
Python menyediakan cara mudah untuk melakukan iterasi melalui setiap elemen dalam list menggunakan loop `for`.
```python
my_list = [1, 2, 3, 4, 5]

# Loop melalui setiap elemen dalam list
for item in my_list:
    print(item)
```

---

#### 4. **List Comprehension**
**List comprehension** adalah cara singkat untuk membuat list baru dengan mendasarkan pada list lain, seringkali dengan kondisi atau operasi tertentu.
```python
# Membuat list baru dari list lama dengan list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]  # [1, 4, 9, 16, 25]
```

---

#### 5. **Studi Kasus: Manajemen Data Mahasiswa**

Misalnya, kita memiliki data mahasiswa yang terdiri dari nama, NIM, dan nilai. Kita akan menyimpan data ini dalam list dan melakukan beberapa operasi.

##### Langkah-langkah:

1. **Membuat List Mahasiswa**: Setiap mahasiswa adalah list yang terdiri dari nama, NIM, dan nilai.
2. **Menambah Data Mahasiswa**: Tambahkan beberapa data mahasiswa ke dalam list utama.
3. **Menghitung Nilai Rata-rata**: Hitung rata-rata nilai mahasiswa.
4. **Mencari Mahasiswa dengan Nilai Tertinggi**: Temukan mahasiswa dengan nilai tertinggi.

##### Kode Python:
```python
# List mahasiswa [Nama, NIM, Nilai]
mahasiswa = [
    ["Andi", "A001", 85],
    ["Budi", "A002", 90],
    ["Cici", "A003", 78],
    ["Doni", "A004", 88]
]

# 1. Menambahkan data mahasiswa baru
mahasiswa.append(["Eka", "A005", 92])

# 2. Menghitung rata-rata nilai mahasiswa
total_nilai = sum([mhs[2] for mhs in mahasiswa])  # Mengambil nilai dari setiap mahasiswa
rata_rata = total_nilai / len(mahasiswa)
print("Rata-rata nilai mahasiswa:", rata_rata)

# 3. Mencari mahasiswa dengan nilai tertinggi
nilai_tertinggi = max(mahasiswa, key=lambda x: x[2])  # Berdasarkan nilai (elemen ketiga)
print("Mahasiswa dengan nilai tertinggi:", nilai_tertinggi[0], "dengan nilai", nilai_tertinggi[2])
```

##### Penjelasan:
- Data mahasiswa disimpan dalam bentuk list, di mana setiap mahasiswa adalah list yang terdiri dari nama, NIM, dan nilai.
- **List comprehension** digunakan untuk menghitung total nilai mahasiswa dengan mengakses elemen ketiga (nilai) dari setiap mahasiswa.
- **Fungsi `max()`** dengan kunci (key) `lambda` digunakan untuk mencari mahasiswa dengan nilai tertinggi.

---

#### 6. **Kesimpulan**
Penggunaan list di Python sangat fleksibel dan dapat digunakan untuk berbagai kebutuhan, mulai dari menyimpan data sederhana hingga kompleks seperti dalam studi kasus manajemen data mahasiswa. Dengan berbagai operasi yang bisa dilakukan pada list, termasuk penambahan, penghapusan, dan manipulasi elemen, Python memberikan kemudahan dalam memanipulasi data.

