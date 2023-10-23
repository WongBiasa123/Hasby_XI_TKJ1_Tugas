# Nama : Ahmad Hasby Maulana
# Kelas : XI TKJ 1
# Absen : 02
# Soal : Seorang analisis data mengkategorikan produk berdasarkan penjualan bulanan.

penjualan_bulanan = int(input("Masukkan data penjualan produk selama satu bulan : "))

if (penjualan_bulanan > 1000) :
    print("Produk Terlaris")
elif (penjualan_bulanan >= 500) :
    print("Produk Populer")
elif (penjualan_bulanan < 500) :
    print("Produk Biasa")