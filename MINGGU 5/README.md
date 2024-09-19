### Materi dan Penjelasan: Penggunaan Kondisi `IF ELSE` dalam Pemrograman Python

**1. Pengenalan `IF ELSE`:**

Dalam pemrograman Python, struktur kondisi `IF ELSE` digunakan untuk mengambil keputusan berdasarkan suatu kondisi tertentu. Struktur ini memungkinkan program untuk menjalankan blok kode yang berbeda, tergantung apakah suatu kondisi bernilai **True** atau **False**.

#### Sintaks Dasar `IF ELSE` dalam Python:

```python
if kondisi:
    # blok kode jika kondisi bernilai True
else:
    # blok kode jika kondisi bernilai False
```

- **`if`**: Memeriksa apakah kondisi bernilai benar (`True`).
- **`else`**: Menangani kasus ketika kondisi bernilai salah (`False`).
  
#### Contoh Sederhana:

```python
nilai = 75

if nilai >= 70:
    print("Selamat, Anda lulus!")
else:
    print("Maaf, Anda belum lulus.")
```

Penjelasan:
- Program memeriksa apakah variabel `nilai` lebih besar atau sama dengan 70.
- Jika benar, program akan mencetak "Selamat, Anda lulus!".
- Jika salah, program mencetak "Maaf, Anda belum lulus."

---

**2. Struktur Kondisi `IF ELIF ELSE`:**

Untuk menangani lebih dari dua kemungkinan, Python menyediakan perintah tambahan, yaitu **`elif`** (singkatan dari *else if*). Dengan **`elif`**, kita dapat memeriksa lebih banyak kondisi tanpa menulis banyak pernyataan `if`.

#### Sintaks `IF ELIF ELSE`:

```python
if kondisi_1:
    # blok kode jika kondisi_1 True
elif kondisi_2:
    # blok kode jika kondisi_2 True
else:
    # blok kode jika semua kondisi False
```

#### Contoh:

```python
nilai = 85

if nilai >= 90:
    print("Grade A")
elif nilai >= 80:
    print("Grade B")
elif nilai >= 70:
    print("Grade C")
else:
    print("Grade D")
```

Penjelasan:
- Jika nilai >= 90, program mencetak "Grade A".
- Jika nilai >= 80, tapi kurang dari 90, program mencetak "Grade B".
- Jika nilai >= 70, tapi kurang dari 80, program mencetak "Grade C".
- Jika semua kondisi salah, maka program mencetak "Grade D".

---

**3. Penggunaan Kondisi `IF ELSE` dengan Operator Logika:**

Kita juga dapat menggunakan operator logika seperti **`and`**, **`or`**, dan **`not`** untuk menggabungkan beberapa kondisi dalam pernyataan `if`.

#### Contoh:

```python
nilai = 75
kehadiran = 85

if nilai >= 70 and kehadiran >= 80:
    print("Anda lulus dengan baik!")
else:
    print("Anda belum memenuhi syarat kelulusan.")
```

Penjelasan:
- Program mengecek dua syarat: `nilai >= 70` dan `kehadiran >= 80`.
- Jika kedua syarat terpenuhi, maka program akan mencetak "Anda lulus dengan baik!".
- Jika salah satu atau keduanya tidak terpenuhi, maka akan mencetak "Anda belum memenuhi syarat kelulusan."

---

### Studi Kasus: Penentuan Diskon Berdasarkan Jumlah Pembelian

Misalkan kita memiliki sebuah program yang menentukan diskon untuk pelanggan berdasarkan total jumlah pembelian mereka. Diskon ini bervariasi tergantung pada total belanja, sebagai berikut:
- Jika total belanja lebih dari atau sama dengan 500 ribu, maka diskon 20%.
- Jika total belanja lebih dari atau sama dengan 300 ribu, diskon 10%.
- Jika total belanja lebih dari atau sama dengan 100 ribu, diskon 5%.
- Jika kurang dari 100 ribu, tidak ada diskon.

#### Studi Kasus dalam Python:

```python
# Input jumlah belanja
total_belanja = float(input("Masukkan total belanja: Rp "))

# Kondisi diskon berdasarkan jumlah belanja
if total_belanja >= 500000:
    diskon = 0.2
    print("Anda mendapatkan diskon 20%.")
elif total_belanja >= 300000:
    diskon = 0.1
    print("Anda mendapatkan diskon 10%.")
elif total_belanja >= 100000:
    diskon = 0.05
    print("Anda mendapatkan diskon 5%.")
else:
    diskon = 0
    print("Anda tidak mendapatkan diskon.")

# Hitung total bayar setelah diskon
total_diskon = total_belanja * diskon
total_bayar = total_belanja - total_diskon

# Output total bayar
print(f"Total yang harus Anda bayar setelah diskon: Rp {total_bayar}")
```

#### Penjelasan:
- Program meminta input total belanja.
- Berdasarkan total belanja, program memeriksa kondisi untuk menentukan diskon.
- Jika total belanja >= 500 ribu, diskon 20%. Jika >= 300 ribu, diskon 10%, dan seterusnya.
- Total bayar dihitung dengan mengurangi total belanja dengan jumlah diskon.
  
---

Dengan kondisi `IF ELSE`, program Python dapat mengambil keputusan secara dinamis berdasarkan input atau kondisi tertentu, memungkinkan kita untuk membuat aplikasi yang interaktif dan responsif.