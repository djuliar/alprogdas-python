### Materi dan Penjelasan tentang **Nested IF** dalam Pemrograman Python

### 1. **Pengertian Nested IF**
**Nested IF** atau **IF bersarang** adalah struktur kontrol di mana satu blok **IF** ditempatkan di dalam blok **IF** lainnya. Dengan kata lain, kita dapat menempatkan satu atau lebih pernyataan **IF ELSE** di dalam pernyataan **IF** utama. Kondisi ini digunakan untuk menguji beberapa kondisi lebih spesifik setelah suatu kondisi terpenuhi.

### 2. **Sintaks Nested IF di Python**

Struktur **Nested IF** di Python bisa terlihat seperti ini:

```python
if kondisi_1:
    # Blok kode jika kondisi_1 True
    if kondisi_2:
        # Blok kode jika kondisi_2 True
    else:
        # Blok kode jika kondisi_2 False
else:
    # Blok kode jika kondisi_1 False
```

Dalam hal ini, **kondisi_2** akan dicek hanya jika **kondisi_1** bernilai **True**. **Nested IF** berguna jika kita ingin memeriksa beberapa syarat yang saling bergantung.

### 3. **Contoh Sederhana Nested IF**

```python
umur = 20
kartu_pelajar = True

if umur >= 18:
    print("Kamu sudah dewasa.")
    if kartu_pelajar:
        print("Kamu juga memiliki kartu pelajar.")
    else:
        print("Kamu tidak memiliki kartu pelajar.")
else:
    print("Kamu belum dewasa.")
```

Pada contoh di atas:
- Jika usia seseorang lebih dari atau sama dengan 18, maka akan dicek apakah dia memiliki kartu pelajar atau tidak.
- Jika usia kurang dari 18, maka hanya pesan "Kamu belum dewasa" yang akan muncul, tanpa mengecek kartu pelajar.

### 4. **Studi Kasus: Penentuan Status Kelulusan dengan Nilai Tambahan**

#### Deskripsi Masalah:
Seorang siswa dianggap **lulus** jika:
- Nilai ujian teori >= 70.
- Jika nilai teori >= 70, harus dicek nilai ujian praktek. Nilai praktek harus >= 60 agar siswa benar-benar dinyatakan lulus.

Jika salah satu syarat tidak terpenuhi, siswa dinyatakan **tidak lulus**.

#### Solusi:

```python
nilai_teori = float(input("Masukkan nilai ujian teori: "))
nilai_praktek = float(input("Masukkan nilai ujian praktek: "))

if nilai_teori >= 70:
    if nilai_praktek >= 60:
        print("Selamat, Anda lulus!")
    else:
        print("Maaf, Anda tidak lulus. Nilai praktek Anda kurang.")
else:
    print("Maaf, Anda tidak lulus. Nilai teori Anda kurang.")
```

#### Penjelasan:
- Jika nilai teori siswa >= 70, baru kita cek nilai ujian praktek.
- Jika nilai teori >= 70 **dan** nilai praktek >= 60, siswa dinyatakan lulus.
- Jika salah satu syarat tidak terpenuhi, maka siswa dinyatakan tidak lulus.

### 5. **Keuntungan Menggunakan Nested IF**
- **Kontrol yang Lebih Terperinci**: Dengan menggunakan **Nested IF**, kita dapat lebih mudah mengontrol alur program saat ada beberapa kondisi yang terkait atau bergantung satu sama lain.
- **Logika Multi-Level**: Digunakan saat kondisi tambahan hanya perlu diperiksa setelah kondisi utama terpenuhi.

### 6. **Contoh Nested IF dengan Kondisi Lebih Kompleks**

Misalkan kita membuat program untuk menentukan kategori usia seseorang dan apakah mereka bisa mendapatkan akses ke fasilitas tertentu:

```python
umur = int(input("Masukkan umur: "))
kartu_anggota = input("Apakah Anda memiliki kartu anggota? (ya/tidak): ").lower()

if umur >= 18:
    if kartu_anggota == "ya":
        print("Anda bisa mendapatkan akses penuh ke fasilitas.")
    else:
        print("Anda perlu kartu anggota untuk akses penuh.")
else:
    if umur >= 12:
        print("Anda hanya bisa mendapatkan akses terbatas.")
    else:
        print("Maaf, Anda tidak bisa mendapatkan akses.")
```

#### Penjelasan:
- Jika usia seseorang >= 18, maka akan dicek apakah dia memiliki kartu anggota.
- Jika memiliki kartu anggota, dia akan mendapatkan akses penuh; jika tidak, dia butuh kartu anggota untuk akses penuh.
- Jika usianya antara 12 dan 17, dia hanya mendapatkan akses terbatas.
- Jika usia kurang dari 12, tidak akan mendapatkan akses sama sekali.

### 7. **Tips Penggunaan Nested IF**
- **Hindari terlalu dalam bersarang**: Meskipun **Nested IF** bisa diterapkan untuk memeriksa banyak kondisi, terlalu banyak bersarang bisa membuat kode sulit dibaca. Pertimbangkan penggunaan **logical operators** seperti `and` atau `or` untuk mempermudah logika.
- **Gunakan dengan bijak**: Pastikan bahwa kondisi bersarang memang relevan dan memperjelas logika program.
  
#### Contoh: Penggunaan Logical Operator untuk Menghindari Nested IF
Kode berikut adalah cara alternatif untuk kasus kelulusan menggunakan **logical operators** sehingga mengurangi kedalaman **Nested IF**:

```python
nilai_teori = float(input("Masukkan nilai ujian teori: "))
nilai_praktek = float(input("Masukkan nilai ujian praktek: "))

if nilai_teori >= 70 and nilai_praktek >= 60:
    print("Selamat, Anda lulus!")
else:
    print("Maaf, Anda tidak lulus.")
```

### 8. **Penutup**
**Nested IF** adalah cara yang sangat berguna untuk mengelola logika yang lebih kompleks, terutama jika kondisi tersebut saling bergantung. Namun, penting untuk menjaga kode tetap rapi dan mudah dipahami dengan tidak terlalu banyak menggunakan **Nested IF** jika bisa dihindari.

Itulah penjelasan tentang **Nested IF** dalam Python. Jika ada yang ingin ditanyakan atau dijelaskan lebih lanjut, silakan tanyakan!