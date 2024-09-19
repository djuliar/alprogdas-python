## Materi: Penggunaan **List** atau **Array** dalam Pemrograman Python

### **Pengertian List dan Array**
Dalam pemrograman Python, **list** adalah salah satu tipe data yang digunakan untuk menyimpan kumpulan data secara terurut dan dapat diubah. List dapat berisi elemen dari berbagai tipe data, seperti integer, string, float, bahkan list lainnya. Sedangkan **array** dalam Python lebih sering diimplementasikan melalui library tambahan seperti `numpy`, terutama saat kita memerlukan operasi vektor atau matriks dengan performa tinggi.

### **List dalam Python**
List di Python adalah struktur data **dinamis**, yang berarti ukuran list dapat berubah (menambah atau mengurangi elemen). List dideklarasikan dengan menggunakan tanda kurung siku (`[]`).

#### **Ciri-ciri list:**
1. **Mutable**: Elemen-elemen dalam list bisa diubah setelah deklarasi.
2. **Beragam tipe data**: List dapat menampung berbagai tipe data di dalamnya.
3. **Indeks**: Elemen-elemen list diakses menggunakan indeks (dimulai dari 0).

### **Contoh List:**
```python
my_list = [1, "Python", 3.14, True]
```

### **Operasi Dasar pada List**
1. **Menambah elemen**: `append()`, `insert()`
   ```python
   my_list.append(100)    # Menambahkan di akhir list
   my_list.insert(1, "Data")  # Menyisipkan di indeks 1
   ```
2. **Menghapus elemen**: `remove()`, `pop()`, `clear()`
   ```python
   my_list.remove(3.14)  # Menghapus elemen dengan nilai tertentu
   my_list.pop()         # Menghapus elemen terakhir
   my_list.clear()       # Mengosongkan list
   ```
3. **Mengakses elemen**: melalui indeks
   ```python
   elemen_pertama = my_list[0]
   elemen_terakhir = my_list[-1]  # Mengakses elemen terakhir dengan indeks negatif
   ```

4. **Menggabungkan list**: `+` atau `extend()`
   ```python
   list1 = [1, 2, 3]
   list2 = [4, 5, 6]
   list_baru = list1 + list2  # Menggabungkan dua list
   ```

5. **Menghitung jumlah elemen**: `len()`
   ```python
   panjang_list = len(my_list)  # Menghitung jumlah elemen dalam list
   ```

### **Array dalam Python**
Untuk array, Python menyediakan **array** dalam library `numpy`. Array di sini biasanya digunakan untuk manipulasi data numerik dalam jumlah besar dan untuk operasi yang lebih efisien dibandingkan list.

```python
import numpy as np

my_array = np.array([1, 2, 3, 4, 5])
```

#### **Perbedaan List dan Array:**
1. **Ukuran**: List dapat menyimpan elemen dengan tipe data yang berbeda, sedangkan array harus menyimpan elemen dengan tipe data yang sama.
2. **Operasi**: Operasi matematika seperti penjumlahan atau perkalian pada array akan berlaku pada setiap elemen (vectorized operations), sementara list akan menambah/menggabungkan elemen secara langsung.

### **Studi Kasus Penggunaan List dalam Pemrograman**

#### **Kasus: Pengelolaan Data Mahasiswa**
Misalnya, kita ingin membuat program untuk mengelola data nilai mahasiswa. Kita akan menggunakan list untuk menyimpan nama-nama mahasiswa dan nilai mereka, serta melakukan berbagai operasi seperti menambah, menghapus, atau mencari mahasiswa tertentu.

#### **Langkah-Langkah:**
1. **Menyimpan Nama dan Nilai**: Menggunakan list untuk menyimpan nama mahasiswa dan nilai-nilainya.
2. **Menambah Mahasiswa Baru**: Menggunakan operasi `append()` untuk menambah mahasiswa baru ke dalam list.
3. **Menghitung Rata-Rata Nilai**: Menggunakan perulangan untuk menjumlahkan nilai dan menghitung rata-rata.

#### **Contoh Program:**
```python
# Daftar mahasiswa dan nilainya
mahasiswa = ["Alice", "Bob", "Charlie", "Diana"]
nilai = [85, 90, 78, 92]

# Menambah mahasiswa baru dan nilainya
mahasiswa.append("Eve")
nilai.append(88)

# Mencetak daftar mahasiswa dan nilai mereka
for i in range(len(mahasiswa)):
    print(f"Nama: {mahasiswa[i]}, Nilai: {nilai[i]}")

# Menghitung rata-rata nilai
rata_rata = sum(nilai) / len(nilai)
print(f"Rata-rata nilai: {rata_rata}")

# Mencari nilai seorang mahasiswa
nama_cari = "Charlie"
if nama_cari in mahasiswa:
    index = mahasiswa.index(nama_cari)
    print(f"Nilai {nama_cari} adalah {nilai[index]}")
else:
    print(f"{nama_cari} tidak ditemukan.")
```

#### **Output Program:**
```
Nama: Alice, Nilai: 85
Nama: Bob, Nilai: 90
Nama: Charlie, Nilai: 78
Nama: Diana, Nilai: 92
Nama: Eve, Nilai: 88
Rata-rata nilai: 86.6
Nilai Charlie adalah 78
```

### **Penjelasan Kasus:**
- **`append()`** digunakan untuk menambah mahasiswa baru beserta nilainya ke dalam list.
- Loop `for` digunakan untuk mencetak daftar nama dan nilai mahasiswa.
- **`sum()`** dan **`len()`** digunakan untuk menghitung rata-rata nilai.
- Fungsi **`index()`** digunakan untuk mencari posisi dari nama mahasiswa yang dicari di dalam list.

### **Kesimpulan**
List dalam Python sangat fleksibel dan dapat digunakan untuk menyimpan berbagai macam data serta melakukan berbagai operasi manipulasi data seperti menambah, menghapus, atau mengakses elemen-elemen di dalamnya. Sedangkan array, yang lebih sering digunakan dari library `numpy`, lebih cocok untuk manipulasi data numerik dalam jumlah besar dengan performa tinggi.

Apakah ada bagian yang ingin dijelaskan lebih lanjut atau dioptimalkan?