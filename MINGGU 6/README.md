## **Materi: Penggunaan Perulangan (Looping) dalam Pemrograman Python**

Perulangan (looping) adalah salah satu fitur penting dalam pemrograman yang memungkinkan kita menjalankan sekelompok perintah berulang kali hingga suatu kondisi tertentu terpenuhi. Di Python, ada dua jenis perulangan utama:

1. **`for` loop**: Digunakan untuk mengulang berdasarkan suatu iterable (seperti list, tuple, string, atau range).
2. **`while` loop**: Digunakan untuk mengulang selama kondisi tertentu masih benar (True).

---

### **1. `for` Loop**

`for` loop digunakan untuk iterasi (pengulangan) dalam suatu iterable, seperti list, tuple, string, atau objek yang mendukung iterasi lainnya. Misalnya, jika kita ingin mengulangi setiap elemen dalam list atau range angka, kita bisa menggunakan `for` loop.

**Sintaks**:
```python
for variable in iterable:
    # blok kode yang akan diulang
```

**Contoh**:
```python
# Mengulang setiap elemen dalam list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```
**Output**:
```
apple
banana
cherry
```

**`range()` Function dalam `for` loop**:
Fungsi `range()` digunakan untuk menghasilkan urutan angka. Ini sering digunakan dalam `for` loop ketika Anda ingin mengulang suatu kode dalam jumlah tertentu.

**Contoh**:
```python
# Mengulang dari 0 hingga 4
for i in range(5):
    print(i)
```
**Output**:
```
0
1
2
3
4
```

### **2. `while` Loop**

`while` loop akan menjalankan blok kode selama kondisinya adalah `True`. Ketika kondisi berubah menjadi `False`, loop akan berhenti.

**Sintaks**:
```python
while kondisi:
    # blok kode yang akan diulang
```

**Contoh**:
```python
# Mengulang hingga i tidak kurang dari 5
i = 0
while i < 5:
    print(i)
    i += 1  # Increment nilai i
```
**Output**:
```
0
1
2
3
4
```

---

### **Controlling Loop**: `break` dan `continue`

- **`break`**: Digunakan untuk menghentikan loop sepenuhnya, meskipun kondisi atau iterasi belum selesai.
- **`continue`**: Digunakan untuk melewati iterasi saat ini dan melanjutkan ke iterasi berikutnya.

**Contoh penggunaan `break`**:
```python
for i in range(5):
    if i == 3:
        break  # Loop berhenti ketika i == 3
    print(i)
```
**Output**:
```
0
1
2
```

**Contoh penggunaan `continue`**:
```python
for i in range(5):
    if i == 3:
        continue  # Melewati iterasi ketika i == 3
    print(i)
```
**Output**:
```
0
1
2
4
```

---

### **Studi Kasus Penggunaan Looping dalam Python**

#### **Studi Kasus 1: Mencari Nilai Terbesar dalam List**

Kita dapat menggunakan `for` loop untuk mencari nilai terbesar dalam sebuah list tanpa menggunakan fungsi built-in Python.

**Contoh**:
```python
numbers = [10, 25, 18, 7, 33, 15]

# Mencari nilai terbesar
max_value = numbers[0]
for number in numbers:
    if number > max_value:
        max_value = number

print("Nilai terbesar:", max_value)
```
**Output**:
```
Nilai terbesar: 33
```

#### **Studi Kasus 2: Mencetak Angka Genap dalam Rentang Tertentu**

Menggunakan `while` loop, kita bisa mencetak semua angka genap dari 1 hingga 20.

**Contoh**:
```python
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1
```
**Output**:
```
2
4
6
8
10
12
14
16
18
20
```

#### **Studi Kasus 3: Program Hitung Mundur dengan `while` Loop**

Buat program yang mencetak hitung mundur dari 10 hingga 0 menggunakan `while` loop.

**Contoh**:
```python
countdown = 10
while countdown >= 0:
    print("Countdown:", countdown)
    countdown -= 1
```
**Output**:
```
Countdown: 10
Countdown: 9
Countdown: 8
Countdown: 7
Countdown: 6
Countdown: 5
Countdown: 4
Countdown: 3
Countdown: 2
Countdown: 1
Countdown: 0
```

---

### **Kesimpulan**

- **`for` loop** digunakan untuk mengulang elemen dari iterable seperti list, tuple, string, atau range.
- **`while` loop** digunakan untuk mengulangi blok kode selama suatu kondisi benar (True).
- **`break`** menghentikan seluruh loop, dan **`continue`** melewati iterasi saat ini dan lanjut ke iterasi berikutnya.

Dengan menggunakan looping, Anda bisa menulis program yang efisien, karena Anda dapat mengotomatisasi tugas yang memerlukan pengulangan.

### **Latihan Soal**

1. Buat program menggunakan `for` loop untuk menjumlahkan semua angka dari 1 hingga 100.
2. Tulis program menggunakan `while` loop yang menghentikan perulangan jika ditemukan angka lebih dari 50 dalam list `[10, 20, 30, 40, 60, 70]`.