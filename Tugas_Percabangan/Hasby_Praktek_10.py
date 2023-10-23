# Nama : Ahmad Hasby Maulana
# Kelas : XI TKJ 1
# Absen : 02
# Soal : Seorang pustakawan menentukan jenis pinjaman buku berdasarkan durasi peminjaman.

durasi_peminjaman = int(input("Durasi Peminjaman buku (hari) : "))

if (durasi_peminjaman <= 7 ) :
    print("Peminjaman Pendek")
elif (durasi_peminjaman > 7 and durasi_peminjaman <= 30) :
    print("Peminjaman Sedang")
elif (durasi_peminjaman > 30 ) :
    print("Peminjaman Panjang")