# Nama      : Ahmad Hasby Maulana
# Kelas     : XI TKJ 1
# No Absen  : 02
# Soal      : Fungsi yang menghitung nilai pangkat dari suatu bilangan dengan eksponen tertentu.

def pangkatBilangan(nilai,pangkat):
    return nilai ** pangkat

angka = int(input("Masukkan angka : "))
eksponen = int(input("Masukkan nilai eksponen : "))

print(f"Hasil dari {angka} pangkat {eksponen} adalah : ", pangkatBilangan(angka,eksponen))