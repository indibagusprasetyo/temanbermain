# Algoritma pendataan nasabah bank (Nomer Rekening, nama, Jumlah saldo)
# Urutan berdasarkan nama nasabah
# Cari nasabah berdasarkan nomer rekening
# I.S. Pengguna memasukkan, nomer rekening, nama, jumlah saldo
# F.S. Program menampilkan 

from ast import Index
from operator import index


norek = []
nama = []
saldo = []
alamat = []

def TambahData(a_norek,a_nama,a_saldo,a_alamat,n):
    for i in range(n):
        print('Masukkan Nomer Rekening ke ',i+1,' : ',end='')
        norek = int(input(''))
        print('Masukkan Nama Nasabah : ',end='')
        nama = str(input(''))
        print('Masukkan Jumlah uang yang akan disetor : ',end='')
        saldo = int(input(''))
        print('Masukkan Alamat Nasabah : ',end='')
        alamat = str(input(''))

        a_norek.append(norek)
        a_nama.append(nama)
        a_saldo.append(saldo)
        a_alamat.append(alamat)


def TampilData(a_norek,a_nama,a_saldo):
    print('----- Daftar Nasabah ------')
    print('----------------------------')
    for i in range(len(a_norek)):
        print('No :', i+1,end='|')
        print('No.Rekening : ',a_norek[i],end='|')
        print('Nama : ',a_nama[i],end='|')
        print('Jumlah Setoran : ',a_saldo[i],end='|')
        print()

def UrutData (a_norek,a_nama,a_alamat,a_saldo):
    n = len(a_nama)
    for i in range(n):
        for j in range (n-i-1):
            if a_nama[j] > a_nama[j+1]:
                #Pengurutan berdasarkan nama
                temp = a_nama[j]
                a_nama[j] = a_nama[j+1]
                a_nama[j+1] = temp

                #Pengurutan berdasarkan norek
                temp = a_norek[j]
                a_norek[j] = a_norek[j+1]
                a_norek[j+1] = temp

                #Pengurutan berdasarkan alamat
                temp = a_alamat[j]
                a_alamat[j] = a_alamat[j+1]
                a_alamat[j+1] = temp

                #Pengurutan berdasarkan saldo
                temp = a_saldo[j]
                a_saldo[j] = a_saldo[j+1]
                a_saldo[j+1] = temp

def CekSaldo (a_norek,x):
    i = 0
    ketemu = False
    n = len(a_norek)

    while(i < n) and (not ketemu):
        if a_norek[i] == x:
            ketemu = True
        else:
            i += 1

    if ketemu:
        index = i
    else:
        index = -1
    return index

def TambahSaldo (a_saldo,x,tambah_setor):
    total = a_saldo[x] + tambah_setor
    return total

def AmbilSaldo (a_saldo,x,tarik_saldo):
    total = a_saldo[x] - tarik_saldo
    return total

def GantiSaldo (saldo_lama, posisi, saldo_baru):
    saldo_lama[posisi] = saldo_baru

def UrutNorek (a_norek,a_nama,a_saldo,a_alamat):
    n = len(a_norek)
    for i in range (n):
        for j in range(n-i-1):
            if a_norek[j] > a_norek[j+1]:
                #Pengurutan Nomer Rekening
                temp = a_norek[j]
                a_norek[j] = a_norek[j+1]
                a_norek[j+1] = temp

                #Pengurutan Nama
                temp = a_nama[j]
                a_nama[j] = a_nama[j+1]
                a_nama[j+1] = temp

                #Pengurutan Saldo
                temp = a_saldo[j]
                a_saldo[j] = a_saldo[j+1]
                a_saldo[j+1] = temp

                #Pengurutan Alamat
                temp = a_alamat[j]
                a_alamat[j] = a_alamat[j+1]
                a_alamat[j+1] = temp

def UrutNama (a_norek,a_nama,a_saldo,a_alamat):
    n = len(a_nama)
    for i in range (n):
        for j in range(n-i-1):
            if a_nama[j] > a_nama[j+1]:
                #Pengurutan Nama
                temp = a_nama[j]
                a_nama[j] = a_nama[j+1]
                a_nama[j+1] = temp

                #Pengurutan Nomer Rekening
                temp = a_norek[j]
                a_norek[j] = a_norek[j+1]
                a_norek[j+1] = temp

                #Pengurutan Saldo
                temp = a_saldo[j]
                a_saldo[j] = a_saldo[j+1]
                a_saldo[j+1] = temp

                #Pengurutan Alamat
                temp = a_alamat[j]
                a_alamat[j] = a_alamat[j+1]
                a_alamat[j+1] = temp

# def SaldoTinggi (a_saldo):
#     i = 0
#     maxSaldo = 0
#     ketemu = False
#     n = len(a_saldo)

#     while(i < n) and (not ketemu):
#         if a_saldo[i] > maxSaldo:
#             maxSaldo = a_saldo [i]
#         else:
#             i += 1

#     if maxSaldo:
#         index = i
#     else:
#         index = -1
#     return index

def SaldoTinggi(a_saldo):
    total_max = a_saldo[0]
    for i in (a_saldo):
        if i > total_max:
            total_max = i
    return total_max

def PemilikSaldo(a_saldo,x):
    i = 0
    ketemu = False
    n = len(a_saldo)

    while(i < n) and (not ketemu):
        if a_saldo[i] == x:
            ketemu = True
        else:
            i += 1

    if ketemu:
        index = i
    else:
        index = -1
    return index

def TampilData(a_norek, a_nama, a_saldo,a_alamat):
    print('------ Daftar Nasabah ------')
    print('----------------------------')
    for i in range(len(a_norek)):
        print('No :', i+1,end='|')
        print('No.Rekening : ',a_norek[i],end='|')
        print('Nama : ',a_nama[i],end='|')
        print('Saldo : ',a_saldo[i],end='|')
        print('Alamat : ',a_alamat[i],end='|')
        print()

def menucs():
    print('----- Menu -----')
    print('1. Menambahkan Data Nasabah Bank')
    print('11. Tampilan ')
    print('2. Memasukkan setoran Nasabah')
    print('3. Cek Saldo Nasabah')
    print('4. Mengurutkan Data Nasabah berdasarkan Nama')
    print('5. Mengurutkan Data Nasabah berdasarkan Nomor Rekening')
    print('6. Saldo Tertinggi')
    print('7. Tarik Tunai')
    print('8. Transfer Saldo Antar Nasabah')
    print('0. Keluar')
    print('---------------')
    menu=int(input('Masukkan menu yang dipilih : '))
    return menu

menu = menucs
while (menu != 0):
    if (menu == 1):
        print('Silahkan Masukkan data Nasabah (Nomer Rekening, Nama, dan Jumlah setoran)')
        n = int(input('Jumlah nasabah yang ingin diinputkan : '))
        TambahData(norek,nama,saldo,alamat,n)
    elif (menu == 11):
        TampilData(norek,nama,saldo,alamat)
    elif (menu == 2):
        print('Silahkan Masukkan Nomer Rekening dan jumlah Setoran')
        print(norek)
        x = int(input('Masukkan Nomer Rekening Nasabah : '))
        index = CekSaldo(norek,x)
        setor = int(input('Masukkan Jumlah Uang yang akan disetor Rp. '))
        setor_baru = TambahSaldo(saldo,index,setor)
        GantiSaldo(saldo,index,setor_baru)
        if index >= 0:
            print('Setoran berhasil masuk, Terima Kasih')
        else:
            print('Gagal Memasukkan Setoran')
    elif (menu == 3):
        print('Silahkan masukan nomer rekening untuk cek saldo')
        print(norek)
        y = int(input('Nomer Rekening : '))
        index = CekSaldo(norek,y)

        if index >= 0:
            print('No.Rekening : ',norek[index],end='|')
            print('Nama : ',nama[index],end='|')
            print('Saldo : Rp.',saldo[index],end='|')
            print('Alamat: ',alamat[index],end='|')
            print()
        else:
            print('Data Tidak DItemukan')
    elif (menu == 4):
        print('Daftar Data Nasabah Berdasarkan Urutan Nama')
        UrutNama(nama)
        TampilData(norek,nama,saldo,alamat)
    elif (menu == 5):
        print('Daftar Data Nasabah Berdasarkan Urutan Nomer Rekening')
        UrutNorek(norek)
        TampilData(norek,nama,saldo,alamat)
    elif(menu == 6):
        saldo_tinggi = SaldoTinggi(saldo)
        print('Slado Tertinggi adalah')
        index = PemilikSaldo(saldo,saldo_tinggi)
        if index >= 0:
            print('No.Rekening : ',norek[index],end='|')
            print('Nama : ',nama[index],end='|')
            print('Saldo : Rp.',saldo[index],end='|')
            print('Alamat: ',alamat[index],end='|')
            print()
        else:
            print('Data Tidak DItemukan')
    elif(menu == 7):
        print('Silahkan Masukkan Nomer Rekening dan jumlah Penarikan')
        print(norek)
        x = int(input('Masukkan Nomer Rekening Nasabah : '))
        index = CekSaldo(norek,x)
        tarik = int(input('Masukkan Jumlah Uang yang akan diambil Rp.'))
        ambil_saldo = AmbilSaldo(saldo,index,tarik)
        GantiSaldo(saldo,index,ambil_saldo)
        if index >= 0:
            print('Setoran berhasil masuk, Terima Kasih')
        else:
            print('Gagal Memasukkan Setoran')
    elif(menu == 8):
        print('Silahkan Masukkan Nomer Rekening pengirim dan jumlah uang yang akan ditransfer')
        print(norek)
        x = int(input('Nomer Rekening Pengirim : '))
        index = CekSaldo(norek,x)
        tarik = int(input('Masukkan Jumlah Uang Yang akan Ditransfer Rp.'))
        ambil_saldo = AmbilSaldo(saldo,index,tarik)
        GantiSaldo(saldo,index,ambil_saldo)
        if index >= 0:
            print('Saldo berhasil ditransfer, Terima Kasih')
        else:
            print('Gagal Transfer')
        y = int(input('Masukkan Rekening Penerima : '))
        index = CekSaldo(norek,y)
        setor = tarik
        setor_baru = TambahSaldo(saldo,index,setor)
        GantiSaldo(saldo,index,setor_baru)
        if index >= 0:
            print('Transfer Masuk, Terima Kasih')
        else:
            print('Transfer Gagal Masuk')
    else:
        print('Pilihan tidak tersedia')
    print('*'*10)
    menu = menucs()