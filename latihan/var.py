#Program untuk menghitung biaya rental warnet
# I.S : Pengguna memasukan Jam Masuk, Menit Masuk, Jam Keluar, dan Menit Keluar
# F.S : Program menampilkan Lamanya rental dan Biaya rental

#Konstan
BIAYA = 5000
MENIT = 60

#input
jamMasuk = int(input("Jam Masuk : "))
menitMasuk = int(input("Menit Masuk : "))
jamKeluar = int(input("Jam Keluar : "))
menitKeluar = int(input("Menit Keluar : "))

#process
TotalJam = jamMasuk - jamKeluar
Durasi = TotalJam * MENIT
TotalMenit = menitMasuk - menitKeluar
TotalDurasi = TotalMenit + Durasi


#output