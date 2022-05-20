#Program Menghitung Gaji Bersih Karyawan 1 dan 2 kasus
#I.S : Pengguna Memasukan Nomor Induk, Nama, Golongan, Jumlah jam kerja pada per-bulan setiap karyawannya
#F.S : Program menampilkan Nomor Induk, Nama, Golongan, Jam Kerja/Bulan. Gaji Pokok, Tunjangan, Gaji Lembur, Potongan, dan Gaji Bersih

BULAN = 208
HARI = 8
GAJILEMBUR = 25000
POTHARI = 50000
POTJAM = 10000

#input
nik = str(input("Masukan Nomor Induk Karyawan : "))
nama = str(input("Masukan Nama Karyawan : "))
golongan = str(input("Masukan Golongan Karyawan : "))
jumlah_jamkerja = int(input("Masukan Jumlah Jam Kerja/Bulan : "))

#proses
if (golongan == "1"):
    gajipokok = 1750000
    tunjangan = 0.125

elif(golongan == "2"):
    gajipokok = 2300000
    tunjangan = 0.15

else:
    print("Golongan Karyawan Tidak Sah")
    exit()

if(BULAN <= jumlah_jamkerja):
    jamlembur= jumlah_jamkerja % BULAN
    total_jambolos = 0

elif(BULAN >= jumlah_jamkerja):
    jamlembur = 0
    total_jambolos = BULAN % jumlah_jamkerja

haribolos = total_jambolos // HARI
jambolos = total_jambolos % HARI
potong_haribolos= haribolos * POTHARI
potong_jam_bolos= jambolos * POTJAM
total_potongan= potong_haribolos + potong_jam_bolos
upahlembur = jamlembur * GAJILEMBUR
tunjangan_karyawan= tunjangan * gajipokok
gajibersih = (gajipokok + upahlembur + tunjangan_karyawan) - total_potongan


#Output
print("Nomor Induk Karyawan :", nik)
print("Nama Karyawan :", nama)
print("Golongan :", golongan)
print("Jumlah Jam Kerja/bulan:", jumlah_jamkerja,"Jam")
print("Gaji Pokok : Rp.", gajipokok)
print("Tunjangan",tunjangan," : Rp.", tunjangan_karyawan)
if(BULAN <= jumlah_jamkerja):
    print("Lembur :", jamlembur,"Jam")
    print(" : Rp.", upahlembur)
    print("Potongan : Rp. 0")
else:
    print("Lembur : Rp.0")
    print("Potongan : -", total_jambolos,"Jam")
    print(" :",haribolos, "Hari",jambolos,"Jam")
    print(" : Rp.", total_potongan)

print("Gaji Bersih : Rp.", gajibersih)
