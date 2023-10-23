# Nama : Ahmad Hasby Maulana
# Kelas : XI TKJ 1
# Absen : 02
# Soal : Seorang pengembang perangkat lunak membuat program sederhana yang menghitung bonus tahunan karyawan berdasarkan performa mereka.

performa_karyawan = int(input("Masukkan performa karyawan (1-5) : "))

print("Bonus 20% dari gaji tahunan") if (performa_karyawan == 5 ) else print("Bonus 10% dari gaji tahunan")  if (performa_karyawan == 4) else print("Bonus 5% dari gaji tahunan") if (performa_karyawan == 3) else print("Bonus 2% dari gaji tahunan") if (performa_karyawan == 2) else print("Tidak ada bonus") 