#Menghitung Jarak Tanggal
#I.S : Pengguna Memasukan Tanggal,Bulan,Tahun Pertama dan Kedua
#F.S : Program Menampilkan Sisa Bulan serta Jarak Antara Tahun dan Bulan

YEAR = 365
MONTH = 30
Tanggal1 = int(input("Masukan Tanggal Pertama: "))
Bulan1 = int(input("Masukan Bulan Pertama: "))
Tahun1 = int(input("Masukan Tahun Pertama: "))
Tanggal2 = int(input("Masukan Tanggal Kedua: "))
Bulan2 = int(input("Masukan Bulan Kedua: "))
Tahun2 = int(input("Masukan Tahun Kedua: "))


TotalHari = (Tanggal2 + Bulan2*MONTH + Tahun2*YEAR) - (Tanggal1 + Bulan1*MONTH + Tahun1*YEAR)

Tahun = TotalHari // YEAR
SisaTahun = TotalHari % YEAR

Bulan = SisaTahun // MONTH
SisaBulan = SisaTahun % MONTH

print(Tahun, Bulan, SisaBulan)