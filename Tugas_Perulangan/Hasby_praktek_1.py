# Nama     : Ahmad Hasby Maulana
# Kelas    : XI TKJ 1
# No Absen : 02
# Soal     : Program yang menghitung berapa bulan yang dibutuhkan agar jumlah ayam melebihi 200 ekor.

bulanKe = 0
jumlahAyam = 100

while jumlahAyam <= 200:
    jumlahAyam += jumlahAyam * 0.05
    bulanKe += 1
    
print(f"Dalam {bulanKe} bulan peternak ayam memiliki {int(jumlahAyam)} ekor ayam")