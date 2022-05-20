#Program Pengolahan Data Mahasiswa
#I.S. : Pengguna Memasukan Data Mahasiswa (NIM,NAMA,ALAMAT)
#F.S. : Program Akan Menampilkan data mahasiswa secara terurut

nim = []
nama = []
alamat = []

def memasukkanData(a_nim, a_nama, a_alamat,n):
    for i in range (n):
        print('Masukkan NIM ke-',i+1,'  : ',end='')
        nim = str(input(' '))
        print('Masukkan Nama ke-',i+1,'  : ',end='')
        nama = str(input(' '))
        print('Masukkan Alamat ke-',i+1,'  : ',end='')
        alamat = str(input(' '))

        a_nim.append(nim)
        a_nama.append(nama)
        a_alamat.append(alamat)

def Menu():
    print('===== Menu =====')
    print('1. Masukkan Data')
    print('2. Mengurutkan Data')
    print('3. Pencarian Data')
    print('0. Keluar')
    menu = int(input('Masukkan Pilihan : '))
    return menu

def TampilData(a_nim, a_nama, a_alamat):
    print('----- Daftar Mahasiswa -----')
    print('----------------------------')
    for i in range(len(a_nim)):
        print('No :', i+1,end='|')
        print('NIM : ',a_nim[i],end='|')
        print('Nama : ',a_nama[i],end='|')
        print('Alamat : ',a_alamat[i],end='|')
        print()

def PengurutanData(a_nim, a_nama, a_alamat):
    n = len(a_nim)
    for i in range(n):
        for j in range(n-i-1):
            if a_nim[j] > a_nim[j+1] :
                #pertukaran nim
                temp = a_nim[j]
                a_nim[j] = a_nim[j+1]
                a_nim[j+1] = temp

                #pertukaran nama
                temp = a_nama[j]
                a_nama[j] = a_nama[j+1]
                a_nama[j+1] = temp

                #pertukaran alamat
                temp = a_alamat[j]
                a_alamat[j] = a_alamat[j+1]
                a_alamat[j+1] = temp

def Binary_search(a_nim,x):
    i = 0
    j = len(a_nim)-1
    ketemu = False
    while (i < j) and (not ketemu):
        k = (i+j)//2
        if (a_nim[k] == x) :
            ketemu = True
        else:
            if a_nim[k] > x :
                j = k - 1
            else:
                i = k + 1
    
    if ketemu:
        index = k
    else:
        index = - 1
    return index

menu = Menu()
while(menu != 0):
    if (menu == 1):
        print('1. Masukkan Data')
        n = int(input('Masukkan jumlah input Data : '))
        memasukkanData(nim,nama,alamat,n)
    elif (menu == 2):
        print('2. Mengurutkan Data')
        print('Data belum terurut')
        TampilData(nim,nama,alamat)
        PengurutanData(nim,nama,alamat)
        print()
        print('Data sudah Terurut')
        TampilData(nim,nama,alamat)
    elif (menu == 3):
        print('3. Pencarian Data Mahasisa')
        x = str(input('Masukkan NIM yang ingin dicari : '))
        PengurutanData(nim,nama,alamat)
        index = Binary_search(nim,x)

        if index >= 0:
            print('Data Ditemukan')
            print('NIM : ',nim[index],end='|')
            print('Nama : ',nama[index],end='|')
            print('Alamat : ',alamat[index],end='|')
            print()
        else:
            print('Data Tidak Ditemukan')

    else:
        print('Pilihan menu tidak tersedia')
    print('-'*10)
    menu = Menu()