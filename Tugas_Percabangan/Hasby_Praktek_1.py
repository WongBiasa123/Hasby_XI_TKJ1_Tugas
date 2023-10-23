# Nama : Ahmad Hasby Maulana
# Kelas : XI TKJ 1
# Absen : 02
# Soal : menghitung diskon berdasarkan jumlah total belanjaan pelanggan di toko online.

total_belanjaan = float(input("Total Belanjaan Anda : "))

if total_belanjaan > 500000 :
    diskon = total_belanjaan * 0.10
elif total_belanjaan >= 300000 :
    diskon = total_belanjaan * 0.05
else:
    diskon = 0
    
total_pembayaran = total_belanjaan - diskon
print(f"Total pembayaran setelah diskon : {total_pembayaran}")