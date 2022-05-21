#Program Penyortir Total Harga Paling Murah
#I.S. : Pengguna Memiliki Data Orang, Bahan Baku, Toko
#F.S. : Program Mensortir Total Harga Paling Murah

Kebutuhan = [[10,6,8,12,4],[8,9,6,4,8],[6,9,4,7,7],[9,4,9,8,7],[12,6,11,8,8],[7,3,5,9,5]]
Harga = [[2500,2350,2600],[1750,1650,1650],[3150,3250,3225],[2800,2650,2750],[4100,4150,4100]]
temp2 = [0]

def Tampil(Array):
    for i in range(0,len(Array)):
        print(Array[i],end=' ')
        print()
    
def HargaMurah(Kebutuhan,Harga,Orang,Bahan,TotalHarga):
    Toko = [0,0,0]
    Toko[0] = (Kebutuhan[Orang][Bahan]) * (Harga[Bahan][0])
    Toko[1] = (Kebutuhan[Orang][Bahan]) * (Harga[Bahan][1])
    Toko[2] = (Kebutuhan[Orang][Bahan]) * (Harga[Bahan][2])
    temp = toko[0]
    j = 0
    for i in range(len(Toko)):
        if Toko[i] <= temp :
            temp = Toko [i]
            j = i
        TotalHarga[0] = temp
        return j

print()
print("TABEL KEBUTUHAN (BARIS=P)(KOLOM=B")
Tampil(Kebutuhan)
print()
print("TABEL HARGA JUAL UNIT (BARIS=B)(KOLOM=T)")
Tampil(Harga)

print()
print("Toko mana yang harus dipilih oleh tiap orang (P)")
for i in range(len(Kebutuhan)):
    print("----Kebutuhan P",i+1,"----")
    for j in range(len(Harga)):
        temp = HargaMurah(Kebutuhan,Harga,i,j,temp2)
        print("Toko yang harus dipilih untuk bahan B",j+1,)
    print()