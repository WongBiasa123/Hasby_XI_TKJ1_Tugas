# Nama : Ahmad Hasby Maulana
# Kelas : XI TKJ 1
# Absen : 02
# Soal : Kasir toko menghitung jumlah diskon berdasarkan total belanjaan pelanggan dan jenis anggota (anggota biasa atau anggota premium).

total_belanja = float(input("Masukkan total belanjaan : "))
status_anggota = input("Apa status anggota anda ? \n (Biasa atau Premium) : ")

if (status_anggota.lower() == "premium") :
    if (total_belanja > 500000) :
        diskon = total_belanja * 0.15
    else :
        diskon = total_belanja * 0.10
elif (status_anggota.lower() == "biasa") :
    if (total_belanja > 300000) :
        diskon = total_belanja * 0.07
    else :
        diskon = 0
        
pembayaran = total_belanja - diskon
print(f"Total belanja : {int(total_belanja)} \n Total diskon : {int(diskon)} \n Total Pembayaran setelah diskon : {int(pembayaran)}")