# Nama      : Ahmad Hasby Maulana
# Kelas     : XI TKJ 1
# No Absen  : 02
# Soal      : Fungsi untuk menghitung jumlah digit dari suatu bilangan.

def jumlahDigit (bilangan):
    return len(str(bilangan))

bilangan = input("Masukkan angka : ")
print(f"Jumlah digit dari bilangan {bilangan} adalah : ", jumlahDigit(bilangan))