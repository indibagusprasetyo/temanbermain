#Program Pengurutan
#I.S. : Pengguna memasukan sembarang elemen array
#F.S. : Program menampilkan elemen array yang sudah terurut

unordered_array = []

def BacaArray (array,N):
    for i in range (N):
        print('Masukan array ke-', i+1,': ',end='')
        data_baru = int(input(' '))
        array.append(data_baru)
    return array

def CetakArray (array): 
    for Larik in (array):
        print(Larik)

def bubble_sort(array):
    n = len(array)
    for i in range (n):
        for j in range (n-i-1):
            #Pengurutan secara ascending
            if array[j] > array[j +1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array


print('----Menu Pengurutan----')
print('1. Masukan Array')
print('2. Bubble Sort')
print('0. Keluar')
print('-' * 20)
menu = int(input('Pilih Menu : '))

while (menu!=0):
    if (menu==1):
        print('Memasukan Element Array')
        panjang_element = int(input('Masukan Panjang Element Array : '))
        BacaArray(unordered_array,panjang_element)
    elif (menu==2):
        print('Pengurutan Bubble Sort')
        print('-' * 20)
        array_bubble = unordered_array
        print('Array Belum Terurut')
        print(unordered_array)
        print('Array Yang Sudah Terurut')
        print(bubble_sort(array_bubble))
    else :
        print('Pilihan Menu Tidak Ada')

    print()
    print('----Menu Pengurutan----')
    print('1. Masukan Array')
    print('2. Bubble Sort')
    print('0. Keluar')
    print('-' * 20)
    menu = int(input('Pilih Menu : '))
else:
    print('Terima Kasih Telah Menggunakan Aplikasi Ini.')