#Program Menghitung Komisi_Salesman
#I.S : Pengguna memasukan nama salesman dan nilai penjualan
#F.S : Program menampilkan nama salesman dan juga komisi yang diterima

NamaSalesman = str(input("Masukan Nama Salesman : "))
NilaiPenjualan = float(input("Masukan Nilai Penjualan : "))

Komisi = 0.05 * NilaiPenjualan

print("Nama Salesman : ",NamaSalesman)
print("Besar Komisi : ",Komisi)