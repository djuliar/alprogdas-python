**Materi: Penggunaan Fungsi dalam Pemrograman Python**

### Pengertian Fungsi
Fungsi adalah blok kode terpisah dalam sebuah program yang dirancang untuk melakukan tugas tertentu. Dalam Python, fungsi memungkinkan kita untuk membungkus logika yang berulang atau kompleks ke dalam satu entitas yang mudah dipanggil kapan saja dalam program. Fungsi membantu dalam mengorganisir kode sehingga lebih terstruktur, mudah dibaca, dan dipelihara.

### Manfaat Menggunakan Fungsi
1. **Reusability (Dapat digunakan kembali)**: Fungsi dapat dipanggil berkali-kali di berbagai tempat dalam program.
2. **Modularisasi**: Membagi kode ke dalam fungsi membuat program lebih modular sehingga lebih mudah dipahami dan di-debug.
3. **Efisiensi Kode**: Fungsi membantu mengurangi pengulangan kode, sehingga kode menjadi lebih ringkas.
4. **Meningkatkan Kolaborasi**: Dengan membagi kode ke dalam fungsi, lebih mudah bagi beberapa orang untuk bekerja pada bagian yang berbeda dari proyek besar.

### Cara Mendefinisikan Fungsi dalam Python
Untuk membuat fungsi di Python, gunakan kata kunci `def` diikuti oleh nama fungsi dan tanda kurung `()`. Berikut adalah format dasar pembuatan fungsi:

```python
def nama_fungsi(parameter1, parameter2, ...):
    # Blok kode
    return hasil
```

- **nama_fungsi** adalah nama yang digunakan untuk memanggil fungsi.
- **parameter** adalah variabel yang berfungsi sebagai input ke dalam fungsi.
- **return** mengembalikan nilai hasil dari fungsi, meskipun return opsional.

### Contoh Sederhana Fungsi
Berikut adalah contoh fungsi yang menerima dua angka dan mengembalikan hasil penjumlahan kedua angka tersebut:

```python
def tambah(a, b):
    hasil = a + b
    return hasil

# Menggunakan fungsi
print(tambah(3, 5))  # Output: 8
```

### Fungsi dengan Nilai Default Parameter
Parameter dalam fungsi bisa diberikan nilai default. Ini berguna jika kita ingin parameter memiliki nilai tertentu jika tidak ada input.

```python
def salam(nama="Teman"):
    return f"Halo, {nama}!"

print(salam())         # Output: Halo, Teman!
print(salam("Andi"))   # Output: Halo, Andi!
```

### Studi Kasus: Menggunakan Fungsi dalam Program Pengelolaan Data Siswa

Misalkan kita ingin membuat program sederhana untuk mengelola data siswa, termasuk menghitung nilai rata-rata, menampilkan status kelulusan, dan menambahkan data siswa baru. Kita bisa membuat beberapa fungsi terpisah untuk setiap tugas.

1. **Fungsi untuk Menghitung Rata-rata**
   Fungsi ini akan menerima daftar nilai sebagai input dan mengembalikan rata-rata nilai tersebut.

   ```python
   def hitung_rata_rata(nilai):
       return sum(nilai) / len(nilai)
   ```

2. **Fungsi untuk Menentukan Status Kelulusan**
   Berdasarkan rata-rata nilai, kita bisa menentukan apakah siswa lulus atau tidak.

   ```python
   def status_kelulusan(rata_rata):
       if rata_rata >= 70:
           return "Lulus"
       else:
           return "Tidak Lulus"
   ```

3. **Fungsi untuk Menambahkan Data Siswa**
   Fungsi ini akan menerima nama siswa dan daftar nilai, kemudian mengembalikan data siswa dengan status kelulusan.

   ```python
   def tambah_data_siswa(nama, nilai):
       rata_rata = hitung_rata_rata(nilai)
       status = status_kelulusan(rata_rata)
       return {
           "Nama": nama,
           "Nilai": nilai,
           "Rata-rata": rata_rata,
           "Status": status
       }
   ```

4. **Menggunakan Fungsi dalam Program**

   Sekarang, kita bisa menggunakan fungsi-fungsi di atas untuk membuat data siswa.

   ```python
   siswa1 = tambah_data_siswa("Budi", [80, 75, 85, 90])
   siswa2 = tambah_data_siswa("Ani", [60, 65, 70, 50])

   print(siswa1)
   print(siswa2)
   ```

   **Output:**
   ```python
   {'Nama': 'Budi', 'Nilai': [80, 75, 85, 90], 'Rata-rata': 82.5, 'Status': 'Lulus'}
   {'Nama': 'Ani', 'Nilai': [60, 65, 70, 50], 'Rata-rata': 61.25, 'Status': 'Tidak Lulus'}
   ```

### Penjelasan
Dalam contoh di atas:
- **Fungsi `hitung_rata_rata`** menghitung rata-rata nilai siswa.
- **Fungsi `status_kelulusan`** memeriksa apakah rata-rata nilai siswa memenuhi syarat kelulusan.
- **Fungsi `tambah_data_siswa`** adalah fungsi utama yang menggabungkan semua langkah dan mengembalikan informasi lengkap tentang siswa.

Dengan menggunakan fungsi, program menjadi lebih terstruktur dan mudah diperluas.
