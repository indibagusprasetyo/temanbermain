#Program Matriks Nilai
#I.S. Pengguna memasukkan nim, matakuliah, nilai per matakuliah per mahasiswa
#F.S. Program Menampilkan nilai dan indeks prestasi / IP

#Array nim, matkul, sks, ip
nim_mhs = []
matkul = []
sks = []

#array 2 dimensi nilai dan indeks
matriks_nilai = []

#nim, matkul, sks
byk_mhs = int(input("Masukkan Banyak Mahasiswa  : "))
byk_matkul = int(input("Masukkan Banyak Mata Kuliah : "))

def IsiArray(byk_mhs,byk_matkul,nim_mhs,matkul,sks,matriks_nilai) :
    for i in range(byk_matkul) :
        print("Masukkan Nama Matakuliah Ke-",i+1,':',end=' ')
        nama_matkul = str(input(" "))
        print("Masukkan Banyak SKS untuk Matkul",nama_matkul,':',end=' ')
        banyak_sks = int(input(' '))
        matkul.append(nama_matkul)
        sks.append(banyak_sks)
    
    for i in range(byk_mhs) :
        print('Masukkan NIM Mahasiswa Ke-',i+1,':',end=' ')
        nim = str(input(' '))

nim_mhs.append(nim)
        sementara=[]
for j in range(byk_matkul) :
            print('Masukkan Nilai',matkul[j],':',end=' ')
            nilai = int(input(' '))
            sementara.append(nilai)
        print()
        matriks_nilai.append(sementara)  

IsiArray(byk_mhs,byk_matkul,nim_mhs,matkul,sks,matriks_nilai)
