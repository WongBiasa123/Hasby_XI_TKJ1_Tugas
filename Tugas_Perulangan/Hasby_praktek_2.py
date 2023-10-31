# Nama     : Ahmad Hasby Maulana
# Kelas    : XI TKJ 1
# No Absen : 02
# Soal     : Program yang menghitung berapa minggu yang dibutuhkan agar pelari itu dapat berlari lebih dari 10 kilometer.

jarakTempuh = 5
mingguKe = 0

while jarakTempuh <= 10:
    jarakTempuh += jarakTempuh * 0.10
    mingguKe += 1
    
print(f"Pelari butuh {mingguKe} minggu untuk dapat berlari {int(jarakTempuh)} Km")