#I.S : PENGGUNA MEMASUKAN GAJI POKOK, TUNJANGAN, DAN JUMLAH KARYAWAN
#F.S : PROGRAM MENAMPILKAN GAJI PER-ORANG, PAJAK, TUNJANGAN, DAN PREMI

#Algoritma
#Header
print("PROGRAM STAFF/HRD UNTUK GAJI KARYAWAN")
print("Pt.X-Industri(PERSERO)")
print("\n\n")
print("Data ini akan disimpan di " r'C:\niles\X\prototype\line2\karyawan\192.168.100.1')

#Input
jml_karyawan = int(input("Jumlah karyawan : "))
gajipokok = int(input("Gaji Karyawan Tersebut : Rp."))

#Proses_dan_variabelnilai
pajak = 0.1 * gajipokok
premi = 0.2 * gajipokok
gaji  = gajipokok +premi - pajak
valuasigaji = gaji *  jml_karyawan

#Output
print("Gaji Perorang = Rp.", gaji)
print("pajak Perorang = Rp.", pajak)
print("Premi Perorang = Rp.", premi)
print("Gaji", jml_karyawan," Karyawan di PT.X-Industri(PERSERO) senilai Rp.", valuasigaji)