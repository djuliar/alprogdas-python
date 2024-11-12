Berikut adalah materi tentang penggunaan fungsi dalam pemrograman Python beserta penjelasan dan contoh studi kasus.

---

### **1. Pengertian Fungsi dalam Python**

Fungsi adalah blok kode yang dirancang untuk melakukan tugas tertentu dan dapat dipanggil berkali-kali dalam program. Fungsi memudahkan pengelolaan kode, mengurangi duplikasi, dan meningkatkan modularitas program. 

Dalam Python, fungsi didefinisikan menggunakan kata kunci `def` diikuti dengan nama fungsi dan tanda kurung `()`. Di dalam tanda kurung, kita dapat menentukan parameter yang digunakan oleh fungsi tersebut.

### **2. Struktur Dasar Fungsi di Python**

Struktur umum dari fungsi di Python adalah sebagai berikut:

```python
def nama_fungsi(parameter1, parameter2, ...):
    """
    Dokumentasi atau deskripsi singkat fungsi ini
    """
    # Blok kode fungsi
    hasil = parameter1 + parameter2  # Contoh operasi dalam fungsi
    return hasil
```

- `def`: Kata kunci untuk mendefinisikan fungsi.
- `nama_fungsi`: Nama fungsi yang bisa dipilih sesuai kebutuhan.
- `parameter`: Nilai input yang diterima fungsi saat dipanggil.
- `return`: Nilai yang dikembalikan fungsi (opsional).

### **3. Keuntungan Menggunakan Fungsi**

- **Mengurangi Duplikasi Kode**: Kita dapat memanggil fungsi yang sama di beberapa tempat tanpa menulis ulang kodenya.
- **Modularitas**: Program lebih modular sehingga mudah dibaca, dikelola, dan diuji.
- **Reusabilitas**: Fungsi dapat digunakan kembali di berbagai bagian program atau di proyek lain.

### **4. Jenis Fungsi dalam Python**

1. **Fungsi Built-in**: Fungsi yang sudah disediakan oleh Python, seperti `print()`, `len()`, `max()`, dll.
2. **Fungsi Pengguna (User-defined Function)**: Fungsi yang dibuat oleh pengguna sesuai kebutuhan spesifik.

---

### **5. Studi Kasus Penggunaan Fungsi**

**Studi Kasus: Sistem Pemesanan Restoran**

Bayangkan kita sedang membuat program sederhana untuk sistem pemesanan makanan di restoran. Program ini menerima daftar pesanan makanan, menghitung total harga, dan menampilkan pesan jika diskon tertentu berlaku.

#### Langkah 1: Definisikan Fungsi

1. **Fungsi `tampilkan_menu`** - Menampilkan menu dan harga makanan.
2. **Fungsi `hitung_total`** - Menghitung total harga pesanan.
3. **Fungsi `diskon`** - Memberikan diskon jika total harga mencapai batas tertentu.

Berikut adalah implementasi dari setiap fungsi tersebut:

```python
# Fungsi untuk menampilkan menu
def tampilkan_menu(menu):
    print("Menu Restoran:")
    for item, harga in menu.items():
        print(f"{item}: Rp{harga}")

# Fungsi untuk menghitung total harga pesanan
def hitung_total(pesanan, menu):
    total = 0
    for item in pesanan:
        total += menu.get(item, 0)  # Ambil harga item atau 0 jika tidak ada
    return total

# Fungsi untuk menghitung diskon jika total memenuhi syarat
def diskon(total, minimum_pembelian=100000, diskon_persen=10):
    if total >= minimum_pembelian:
        return total * (1 - diskon_persen / 100)
    return total
```

#### Langkah 2: Menggunakan Fungsi dalam Program

Sekarang kita dapat memanggil fungsi-fungsi ini untuk mengatur alur program.

```python
# Menu makanan di restoran
menu = {
    "Nasi Goreng": 20000,
    "Ayam Bakar": 25000,
    "Mie Goreng": 15000,
    "Es Teh": 5000,
}

# Pesanan pelanggan
pesanan = ["Nasi Goreng", "Ayam Bakar", "Es Teh"]

# Menampilkan menu
tampilkan_menu(menu)

# Menghitung total harga pesanan
total_harga = hitung_total(pesanan, menu)
print(f"Total harga sebelum diskon: Rp{total_harga}")

# Menghitung harga setelah diskon jika memenuhi syarat
total_setelah_diskon = diskon(total_harga)
print(f"Total harga setelah diskon: Rp{total_setelah_diskon}")
```

#### Penjelasan Program

1. **tampilkan_menu(menu)**: Fungsi ini menerima `menu` sebagai parameter dan menampilkan daftar item dan harganya.
2. **hitung_total(pesanan, menu)**: Fungsi ini menerima `pesanan` (daftar item yang dipesan) dan `menu`, kemudian mengembalikan total harga pesanan.
3. **diskon(total, minimum_pembelian, diskon_persen)**: Fungsi ini memberikan diskon jika `total` mencapai `minimum_pembelian`.

Jika pelanggan memesan lebih dari Rp100.000, maka mereka mendapatkan diskon sebesar 10%.

---

### **6. Kesimpulan**

Fungsi membantu kita untuk mengorganisir kode dan membuat program lebih terstruktur. Pada studi kasus di atas, fungsi membantu untuk memecah tugas-tugas spesifik, seperti menampilkan menu, menghitung total harga, dan menghitung diskon, sehingga kode lebih modular dan mudah dipahami. 

Contoh penggunaan fungsi ini dapat dikembangkan lebih lanjut untuk mencakup fungsi tambahan sesuai dengan kebutuhan, seperti fungsi untuk menambahkan pesanan baru atau menghitung pajak tambahan.
