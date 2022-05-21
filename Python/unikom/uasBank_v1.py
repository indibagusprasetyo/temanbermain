from re import I
from turtle import setworldcoordinates


norek = []
nama = []
saldo = []
alamat = []

def Menu() :
    print('----- Menu -----')
    print('1. Menambahkan Data Nasabah Bank')
    print('2. Memasukkan setoran Nasabah')
    print('3. Cek Saldo Nasabah')
    print('4. Mengurutkan Data Nasabah berdasarkan Nama')
    print('5. Mengurutkan Data Nasabah berdasarkan Nomor Rekening')
    print('6. Cek Saldo Tertinggi')
    print('7. Tarik Tunai')
    print('8. Transfer Saldo ANtar Nasabah')
    print('0. Keluar')
    print('---------------')
    menu=int(input('Masukkan menu yang dipilih : '))
    return menu

def CekUserBesar (_norek) :
    if len(_norek) > 0 :
        maks = _norek[0]
        for i in _norek :
            if i > maks :
                maks = i
        print('No. rekening Nasabah terakhir adalah',"{:04d}".format(maks))
    else :
        print('Belum ada Nasabah Yang Terdaftar')
        maks = 0
    return maks

def InputUser (_norek,_nama,_saldo,_alamat,n,_userbesar) :
    for j in range (n) :
        print('-'*20)
        norek = int(_userbesar+(j+1))
        print('REKENING',"{:04d}".format(norek))
        print('Masukkan Nama :',end=' ')
        nama = str(input(' '))
        print('Masukkan Saldo : Rp',end=' ')
        saldo = int(input(' '))
        print('Masukkan Alamat :',end=' ')
        alamat = str(input(' '))

        _norek.append(norek)
        _nama.append(nama)
        _alamat.append(alamat)
        _saldo.append(saldo)

def SearchSaldo (_norek,x):
    i = 0
    j = len(_norek)-1
    ketemu = False
    while(i <= j) and (not ketemu):
        if _norek[j] == x :
            ketemu = True
        else:
            j -= 1
    if ketemu :
        index = j
    else:
        index = -1
    return index

def TambahSaldo(_saldo,_index,_setor):
    total = _saldo[_index] + _setor
    return total

def KurangSaldo(_saldo,_index,_setor):
    total = _saldo[_index] - _setor
    return total

def GantiSaldo(_saldolama,_posisi,_saldobaru):
    _saldolama[_posisi] = _saldobaru

def TampilData(_norek,_nama,_saldo,_alamat) :
    print('----Daftar Nasabah----')
    for i in range(len(_norek)) :
        print('No.Rek :',"{:04d}".format(_norek[i]),end='|')
        print('Nama :',_nama[i],end='|')
        print('Saldo : Rp',_saldo[i],end='|')
        print('Alamat :',_alamat[i],end='|')
        print()

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

def CekMaks (_saldo):
    maks = _saldo[0]
    for i in _saldo :
        if i > maks :
            maks = i
    return maks

def Urut (A,B,C,D):
    n = len(A)
    for i in range (n):
        for j in range(n-i-1):
            if A[j] > A[j+1]:

                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp

                temp = B[j]
                B[j] = B[j+1]
                B[j+1] = temp

                temp = C[j]
                C[j] = C[j+1]
                C[j+1] = temp

                temp = C[j]
                C[j] = C[j+1]
                C[j+1] = temp

menu = Menu()
while (menu!=0) :
    if(menu==1) :
        print('-'*30)
        userbesar=CekUserBesar(norek)
        print('Memasukkan Data Nasabah')
        n = int(input('Masukkan Jumlah User Nasabah : '))
        InputUser(norek,nama,saldo,alamat,n,userbesar)
    elif(menu==2) :
        print('Data nasabah sebelum setoran')
        TampilData(norek,nama,saldo,alamat)
        print('-'*30)
        print('Silahkan Masukkan Nomer Rekening dan jumlah Setoran')
        xnorek = int(input('Masukkan Nomer Rekening Nasabah : '))
        index = SearchSaldo(norek,xnorek)
        setor = int(input('Masukkan Jumlah Uang yang akan disetor Rp. '))
        setor_baru=TambahSaldo(saldo,index,setor)
        GantiSaldo(saldo,index,setor_baru)
        print('Data nasabah sesudah setoran')
        TampilData(norek,nama,saldo,alamat)
        if index >= 0:
            print('Setoran berhasil masuk, Terima Kasih')
        else:
            print('Gagal Memasukkan Setoran')
    elif(menu==3):
        for i in range(len(norek)) :
            print('No.Rek :',"{:04d}".format(norek[i]),end='|')
            print()
        print('Silahkan masukkan nomor rekening untuk cek saldo')
        print('-'*30)
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
    elif(menu==4):
        print('Daftar Data Nasabah Berdasarkan Urutan Nama')
        Urut(nama,norek,saldo,alamat)
        TampilData(norek,nama,saldo,alamat)
        print('-'*30)
    elif(menu==5):
        print('Daftar Data Nasabah Berdasarkan Urutan Nomer Rekening')
        Urut(norek,nama,saldo,alamat)
        TampilData(norek,nama,saldo,alamat)
        print('-'*30)
    elif(menu==6):
        print('Nasabah Dengan Saldo Tertinggi Adalah')
        SaldoTinggi = CekMaks(saldo)
        index = SearchSaldo(saldo,SaldoTinggi)
        if index >= 0:
            print('No.Rekening : ',norek[index],end='|')
            print('Nama : ',nama[index],end='|')
            print('Saldo : Rp.',saldo[index],end='|')
            print('Alamat: ',alamat[index],end='|')
            print()
        else:
            print('Data Tidak DItemukan')
    elif(menu==7):
        print('Data nasabah sebelum setoran')
        TampilData(norek,nama,saldo,alamat)
        print('-'*30)
        print('Silahkan Masukkan Nomer Rekening dan jumlah Penarikan')
        xnorek = int(input('Masukkan Nomer Rekening Nasabah : '))
        index = SearchSaldo(norek,xnorek)
        tarik = int(input('Masukkan Jumlah Uang yang akan ditarik Rp. '))
        tarik_baru=KurangSaldo(saldo,index,tarik)
        GantiSaldo(saldo,index,tarik_baru)
        print('Data nasabah sesudah penarikan')
        TampilData(norek,nama,saldo,alamat)
        if index >= 0:
            print('Penarikan berhasil, Terima Kasih')
        else:
            print('Gagal Penarikan')
    elif(menu==8):
        print('Data nasabah sebelum transaksi')
        TampilData(norek,nama,saldo,alamat)
        print('-'*30)
        print('Silahkan masukkan nomor rekening dan saldo yang akan di transfer')
        xnorek = int(input('Masukkan Nomer Rekening Nasabah : '))
        index = SearchSaldo(norek,xnorek)
        transfer = int(input('Masukkan Jumlah Uang yang akan ditransfer Rp. '))
        transfer_baru=KurangSaldo(saldo,index,transfer)
        GantiSaldo(saldo,index,transfer_baru)
        xnorek = int(input('Masukkan Nomer Rekening Nasabah Yang Akan ditrasnfer : '))
        index = SearchSaldo(norek,xnorek)
        transfer_baru=TambahSaldo(saldo,index,transfer)
        GantiSaldo(saldo,index,transfer_baru)
        print('-'*30)
        print('Data nasabah sesudah transaksi')
        TampilData(norek,nama,saldo,alamat)
    else :
        print('Pilihan Menu Tidak Tersedia')

    print('-'*30)
    menu = Menu()