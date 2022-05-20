#Program Aritmatika
#I.S. : Pengguna memasukan angka dan memilih operasi aritmatika yang di inginkan
#F.S. : Program menampilkan hasil dari operasi

#variabel
angka1 = int(input("Masukan Angka : "))

#tabinformasi
print("Pilihlah operasi aritmatika")
print("+ = 1")
print("- = 2")
print("* = 3")
print("/ = 4")
operasi = int(input("Masukan Operasi berdasarkan angka berikut: "))
angka2 = int(input("Masukan Angka ke-2 : "))
if (operasi==1):
    print(angka1 + angka2)
elif (operasi==2):
    print(angka1 - angka2)
elif (operasi==3):
    print(angka1 * angka2)
elif (operasi==4):
    print(angka1 / angka2)
else:
    print("Operasi tidak diketahui")
