#Program Pengolahan Data Mahasiswa
#I.S. : Pengguna Memasukan Data Mahasiswa (NIM,NAMA,ALAMAT)
#F.S. : Program Akan Menampilkan data mahasiswa secara terurut

nim =[]
nama=[]
alamat=[]

def MemasukanData(a_nim, a_nama, a_alamat, n):
  for i in range (n) :
    print("Masukan Nim Ke-,",i+1,':',end='')
    nim = str(input(''))
    print("Masukan Nama Ke-,",i+1,':',end='')
    nama = str(input(''))
    print("Masukan Alamat Ke-,",i+1,':',end='')
    alamat = str(input(''))

    a_nim.append(nim)
    a_nama.append(nama)
    a_alamat.append(alamat)

def Menu() :
  print('===========Menu==========')
  print('1. Memasukan Data')
  print('2. Mengurutkan Data')
  print('3. Pencarian Data')
  print('0. Keluar')
  menu = int(input("Masukan Pilihan : "))
  return menu

def TampilData(a_nim,a_nama,a_alamat):
  print('==========Daftar Mahasiswa==========')
  print('====================================')
  for i in range(len(a_nim)):
    print('No :',i+1,ends="|")
    print('NIM : ', a_nim[i],end="|")
    print('Nama : ', a_nama[i],end="|")
    print('Alamat : ', a_alamat[i],end="|")
    print()

def PengurutanData(a_nim,a_nama,a_alamat):
  n = len(a_nim)
  for i in range (n):
    for j in range (n-i-1):
      if a_nim[j] > a_nim[j+1] :
        #PertukaranNIM
        temp = a_nim[j]
        a_nim[j] = a_nim[j+1]
        a_nim[j+1] = temp

        #PertukaranNama
        temp = a_nama[j]
        a_nama[j] = a_nama[j+1]
        a_nama[j+1] = temp

        #PertukaranAlamat
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
while (menu!=0):
  if(menu==1):
    print('Memasukan Data Mahasiswa')
    n = int(input('Memasukan Jumlah Inputan : '))
    MemasukanData(nim,nama,alamat,n)
  elif(menu==2):
    print('Mengurutkan Data Mahasiswa')
    print("Data Belum Terurut")
    TampilData(nim,nama,alamat)
    PengurutanData(nim,nama,alamat)
    print()
    print('Data Sudah Terurut')
    TampilData(nim,nama,alamat)
    print()
  elif(menu==3):
    print('Pencarian Data Mahasiswa')
    x = str(input('Masukan NIM yang ingin dicari : '))
    PengurutanData(nim,nama,alamat)
    index = Binary_Search(nim,x)

    if index >= 0 :
      print("Data Ditemukan : ")
      print('NIM : ', a_nim[index],ends="|")
      print('Nama : ', a_nama[index],ends="|")
      print('Alamat : ', a_alamat[index],ends="|")
      print()
    else :
      print("Data Tidak Ditemukan!")
  else :
    print('Pilihan Menu Tidak Tersedia')

print('-'*30)
menu = Menu()
