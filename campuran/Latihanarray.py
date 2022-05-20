#Program Array / Larik
Nmaks = 5
A = []

def TambahArray (A,n) :
    banyak_data = len(A)
    if (banyak_data < Nmaks) and (n<=(Nmaks-banyak_data)):
    for i in range (n) :
        data_baru = int(input('Masukan Data Elemen Larik : '))
        A.append(data_baru)

def CetakArray (A) :
    for Larik in A :
        print(Larik)

def SisipArray (A, Posisi, Sisip) :
    banyak_data = len(A)
    if (banyak_data < Nmaks):
        A.insert(Posisi,Sisip)
    
    

print('Menu Array')
print('1. Menambahkan Elemen Array')
print('2. Menampilkan Elemen Array')
print('3. Menyisipkan Elemen Array')
print('4. Menampilkan Nilai Terbesar dan Terkecil')
print('5. Nilai Rata-Rata')
print('0. Keluar')

 
menu = int(input('Masukan Pilihan : '))


while (menu!=0) :
    if (menu==1) :
        n = int(input('Masukan Jumlah Elemen Yang Diinginkan : '))
        TambahArray(A,n)
    elif (menu==2) :
        print(A)
        print('-'*20)
        CetakArray(A)
    elif (menu==3) :
        posisi = int(input('Masukan Posisi Sisip : '))
        data_sisip = int(input('Masukan Data Yang Akan Disisipkan : '))
        #A.insert(posisi,data,sisip)
        SisipArray(A,posisi,data_sisip)


    print('-'*30)
    menu = int(input('Masukan Pilihan : '))

