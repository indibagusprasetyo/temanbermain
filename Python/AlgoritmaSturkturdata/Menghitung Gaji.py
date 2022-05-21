#Menghitung Gaji Bersih Karyawan UNIKOM
#I.S : Pengguna memasukan nama karyawan dan gaji pokok karyawan tersebut
#F.S : Program menampilkan gaji bersih dari karyawan tersebut

NamaKaryawan = str(input("Nama Karyawan :"))
GajiPokok = float(input("Gaji :"))
Tunjangan = 0.20 * GajiPokok
Pajak = (0.15 * GajiPokok) + Tunjangan

GajiBersih = GajiPokok + Tunjangan - Pajak

print("Nama Karyawan :",NamaKaryawan)
print("Tunjangan Karyawan :",Tunjangan)
print("Pajak :",Pajak)
print("Gaji Bersih :",GajiBersih)


