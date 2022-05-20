#Program Penjumlahan Matriks
#I.S : Pengguna memasukan jumlah kolom dan baris
#F.S : Program menampilkan hasil penambahan 2 matriks

A=[]
B=[]
C=[]

def BacaLarik(A,NBaris,NKolom) :
    for i in range(NBaris):
        A_Sementara=[]
        for j in range(NKolom):
            print('Masukan Data [',i,',',j,'] : ',end='')
            nilai= int(input(' '))
            A_Sementara.append(nilai)
        A.append(A_Sementara)

def TampilMatriks(A) :
    for i in range(0,len(A)):
        for j in range(0,len(A[0])):
            print(A[i][j],end='')
        print()
        
NBaris = int(input("Masukan Jumlah Baris : "))
NKolom = int(input("Masukan Jumlah Kolom : "))

print("Memasukan Elemen Matriks A")
BacaLarik(A,NBaris,NKolom)
TampilMatriks(A)
print()

print("Memasukan Elemen Matriks B")
BacaLarik(B,NBaris,NKolom)
TampilMatriks(B)
print()