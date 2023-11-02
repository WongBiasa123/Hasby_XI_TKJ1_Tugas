# Nama      : Ahmad Hasby Maulana
# Kelas     : XI TKJ 1
# No Absen  : 02
# Soal      : Fungsi untuk menghitung faktorial dari suatu bilangan.

def faktorial(bilangan) :
    if bilangan == 0 or bilangan == 1 :
        return 1
    else :
        return bilangan * faktorial(bilangan-1)
    
angka = int(input("Masukkan angka : "))
print(f"Hasil faktorial dari {angka} adalah : ", faktorial(angka))