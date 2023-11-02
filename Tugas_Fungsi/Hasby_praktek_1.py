# Nama      : Ahmad Hasby Maulana
# Kelas     : XI TKJ 1
# No Absen  : 02
# Soal      : Fungsi yang menghitung total dari deret bilangan ganjil hingga batas tertentu yang ditentukan pengguna.

def bilangan_ganjil (batas) :
    jumlah = 0
    for i in range(1, batas + 1, 2) :
       jumlah += i
    return jumlah

batas_akhir = int(input("Masukkan batas akhir bilangan ganjil :"))

total_bilangan = bilangan_ganjil(batas_akhir)
print(f"Total bilangan ganjil yang kurang dari {batas_akhir} adalah {total_bilangan}")
