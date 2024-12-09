def hitung_total_penjualan(daftar_penjualan):
    total = 0
    
    for barang in daftar_penjualan:
        nama, jumlah, harga = barang
        total += jumlah * harga
    
    if total > 1000000:
        total *= 0.9  
        print("Diskon 10% diterapkan!")
    return total

daftar_penjualan = [
    ("Buku", 10, 20000),
    ("Pensil", 50, 5000),
    ("Penghapus", 30, 3000),
    ("Tas", 5, 250000)
]

total_harian = hitung_total_penjualan(daftar_penjualan)
print(f"Total penjualan hari ini: Rp{total_harian:,.2f}")