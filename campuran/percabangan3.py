# Program Pengenal Tahun Kabisat
# I.S : Pengguna Memasukan Tahun
# F.S : Program menampilkan keterangan jenis tahun (Bukan / Kabisat)

#input
tahun = int(input("Masukan Tahun : "))

#process & output
if (tahun % 4 == 0) and (tahun % 100 != 0) or (tahun % 400 == 0):
    print("Tahun", tahun, "adalah tahun kabisat")
else:
    print("Tahun", tahun,"adalah bukan tahun kabisat")
