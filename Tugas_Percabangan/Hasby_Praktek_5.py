# Nama : Ahmad Hasby Maulana
# Kelas : XI TKJ 1
# Absen : 02
# Soal : Seorang guru menentukan nilai akhir siswa berdasarkan nilai tugas dan ujian.

nilai_tugas = int(input("Silahkan masukkan nilai tugas siswa!! (skala 0-100) \n  Nilai Tugas: "))
nilai_ujian = int(input("Silahkan Masukkan nilai ujian siswa!! (skala 0-100) \n  Nilai Ujian: "))


if (nilai_tugas > 70 and nilai_ujian > 60) :
    print("Lulus")
else :
    print("Gagal")