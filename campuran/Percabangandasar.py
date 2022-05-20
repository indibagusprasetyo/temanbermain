#Desc
print("Pemilihan TIKET KERETA API")
print("Kota Jakarta = Kode 1 = 150000")
print("Kota Yogyakarta = Kode 2 = 300000")
print("Kota Surabaya = Kode 3 = 400000")
print("Harap memilih tiket dengan kode tertentu")

#Input
kodekota = int(input("Kode Kota Tujuan (1/2/3): "))
banyaktiket = int(input("Jumlah Tiket Pembelian : "))

kode1 = 150000
kode2 = 300000
kode3 = 400000

#Process & Output
if (kodekota==1):
    print(kode1 * banyaktiket)
elif (kodekota==2):
    print(kode2 * banyaktiket)
elif (kodekota==3):
    print(kode3 * banyaktiket)
else: print("Tidak ada kode")