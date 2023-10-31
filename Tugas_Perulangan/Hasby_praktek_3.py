# Nama     : Ahmad Hasby Maulana
# Kelas    : XI TKJ 1
# No Absen : 02
# Soal     : Program yang menghitung berapa tahun yang dibutuhkan agar nilai investasi melebihi 20.000 dollar.

investasi = 10000
tahunKe = 0

while investasi <= 20000 :
    investasi += investasi * 0.06
    tahunKe += 1
    
print(f"Butuh {tahunKe} tahun agar nilai investasi {int(investasi)} dollar")