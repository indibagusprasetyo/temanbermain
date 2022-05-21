# Program Validasi Tanggal
# I.S : Pengguna Memasukan Tanggal
# F.S : Program Mengidentifikasi tanggal tersebut (valid/tidak)

#input
tanggal = int(input("Masukan Tanggal : "))
bulan = int(input("Masukan Bulan (Berdasarkan angka) :"))
tahun = int(input("Masukan Tahun : "))

#Process & output
if(tanggal <= 31) and (bulan == 1,3,5,7,8,10,12):
    print("Tanggal", tanggal ,"/", bulan ,"/", tahun, "adalah tanggal valid")
elif(tanggal <= 29) and (bulan == 2):
     print("Tanggal", tanggal ,"/", bulan ,"/", tahun, "adalah tanggal valid")
elif(tanggal <= 30) and (bulan == 4, 6, 9, 12):
    print("Tanggal", tanggal ,"/", bulan ,"/", tahun, "adalah tanggal valid")
else:
     print("Tanggal", tanggal ,"/", bulan ,"/", tahun, "bukan tanggal valid")
