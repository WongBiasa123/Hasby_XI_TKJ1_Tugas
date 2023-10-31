# Nama     : Ahmad Hasby Maulana
# Kelas    : XI TKJ 1
# No Absen : 02
# Soal     : Program yang menghitung berapa hari yang dibutuhkan agar sisa apel kurang dari 20 buah.

sisaApel = 100
hari = 0

while sisaApel >= 20 :
    sisaApel -= sisaApel * 0.10
    hari +=1
    
print(f"Butuh {hari} hari agar apel kurang dari 20")