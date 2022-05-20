#input
jmlkry = int(input("Jumlah karyawan : "))
gajipokok = int(input("Gaji Pokok : "))

#Process
pajak = 0.1 * gajipokok
tunjangan = 0.2 * gajipokok
gaji = gajipokok + tunjangan - pajak
jmlgji = gaji * jmlkry

#output
print("Gaji Perorangan : ", gaji)
print("Pajak Perorangan : ", pajak)
print("Tunjangan Perorangan : ", tunjangan)
print("Rp. ", jmlgji)