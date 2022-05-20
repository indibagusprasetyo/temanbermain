# Program Menghitung gaji karyawan
# I.S : Pengguna memasukan nama, jabatan, status, dan banyak anak
# F.S : Program menampilkan nama,jabatan, status, banyak anak, gaji pokok, tunjungan keluarga & anak, gaji kotor, pajak pph21, dan gaji bersih

#konstan
DIREKTUR = 5000000
MANAGER = 3000000
STAFF = 2000000

#input
nama = str(input("Masukan Nama Anda : "))

print("Jabatan :")
print("Direktur == 1")
print("Manager == 2")
print("Staff == 3")
jabatan = int(input("Pilihlah Jabatan sesuai nomor diatas : "))
status = str(input("Menikah (Y/T) : "))

