#Program Penjumlahan Matriks
#I.S : Pengguna memasukan jumlah kolom dan baris
#F.S : Program menampilkan hasil penambahan 2 matriks

A = []
B = []
C = []


# Memasukan Elemen Larik
def bacaLarik(A, NBaris, NKolom) :
    for i in range(NBaris) :
        A_Sementara = []
        for j in range(NKolom) :
            print("Masukan data [",i, ", ", j, "] :", end='')
            nilai = int(input(''))
            A_Sementara.append(nilai)
        A.append(A_Sementara)

def tampilMatriks(A) :
    for i in range(0, len(A)) :
        for j in range(0, len(A[0])) :
            print(A[i][j], end=" ")
        print()

# Tambah
def tambahLarik(A, B, NBaris, NKolom, C) :
    A_Sementara = []
    for i in range(NBaris) :

        for j in range(NKolom) :
            A_Sementara.append(A[i][j] + B[i][j])

    C.append(A_Sementara)

print("Memasukkan Element Matriks A")
NBaris = int(input("Masukan jumlah baris : "))
NKolom = int(input("Masukan jumlah Kolom : "))

bacaLarik(A, NBaris, NKolom)

# print(A, end=' ')
tampilMatriks(A)
print()

print("Memasukkan Element Matriks B")
NBaris = int(input("Masukan jumlah baris : "))
NKolom = int(input("Masukan jumlah Kolom : "))

bacaLarik(B, NBaris, NKolom)

# print(A, end=' ')
tampilMatriks(B)
print()

tambahLarik(A, B, NBaris, NKolom, C)
tampilMatriks(C)