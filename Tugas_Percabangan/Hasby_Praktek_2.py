# Nama : Ahmad Hasby Maulana
# Kelas : XI TKJ 1
# Absen : 02
# Soal : Manajer proyek menentukan apakah suatu proyek akan selesai tepat waktu atau terlambat.

from datetime import datetime

estimasi = input("Masukkan estimasi waktu selesai (format: DD-MM-YYYY) : ")
target = input("Masukkan tanggal target selesai (format: DD-MM-YYYY) : ")

estimasi_selesai = datetime.strptime(estimasi, '%d-%m-%Y')
target_selesai = datetime.strptime(target, '%d-%m-%Y')

if (estimasi_selesai <= target_selesai) :
    print("Tepat waktu!!")
else :
    print("Terlambat!!")
