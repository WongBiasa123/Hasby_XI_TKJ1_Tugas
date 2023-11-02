# Nama      : Ahmad Hasby Maulana
# Kelas     : XI TKJ 1
# No Absen  : 02
# Soal      : Fungsi yang menghitung bilangan Fibonacci ke-n.

def bilangan_fibonacci(h):
    if h == 1:
        return 0
    elif h == 2:
        return 1
    else:
        return bilangan_fibonacci(h - 1) + bilangan_fibonacci(h - 2)
    
input = int(input("Masukkan angka ke-n : "))
print(f"Bilangan Fibonacci ke-{input} adalah: " , bilangan_fibonacci(input))
