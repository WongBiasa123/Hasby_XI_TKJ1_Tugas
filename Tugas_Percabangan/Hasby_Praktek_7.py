# Nama : Ahmad Hasby Maulana
# Kelas : XI TKJ 1
# Absen : 02
# Soal : Seorang administrasi sistem memutuskan apakah suatu sistem perlu di-restart setelah pembaruan perangkat lunak.

informasi_pembaruan = input("Apakah pembaruan memerlukan restart? (ya/tidak) : ")

if informasi_pembaruan.lower() == "ya" :
    print("Sistem perlu di-restart")
elif informasi_pembaruan.lower() == "tidak" :
    print("Sistem tidak perlu di-restart")