#Input
nama = str(input("Nama Mahasiswa : "))
nilaiuts = int(input("Masukan Nilai UTS : "))
nilaiharian = int(input("Masukan Nilai Harian : "))

#Process
nilaiakhir = (nilaiuts + nilaiharian) * 0.30

#output
print(nama)
print("Nilai Akhir : ",nilaiakhir,nama) 