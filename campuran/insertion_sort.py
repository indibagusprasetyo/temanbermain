#Program Pengurutan Sisip
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

def bubble_sort(array, desc=False):
    n = len(array)
    for i in range (n):
        for j in range (n-i-1):
            if desc==True :
                #Pengurutan secara descending
                if array[j] < array[j +1]:
                    array[j],array[j+1] = array[j+1],array[j]
            else:
            #Pengurutan secara ascending
                if array[j] > array[j +1]:
                    array[j],array[j+1] = array[j+1],array[j]
    return array

def selection_sort(array, desc=False):
    n = len(array)
    for i in range (n):
        #Mencari nilai terendah berada di indeks mana
        min_idx = i
        for j in range (i + 1, n):
            if desc :
                #Pengurutan Secara Ascending
                if array[min_idx] < array[j]:
                    min_idx = j
            else :
                #Pengurutan Secara Ascending
                if array[min_idx] > array[j]:
                    min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]
    return array

def insertion_sort(array,desc=False):
    n = len(array)
    for i in range (1,n):
        key_item = array[i]
        j = i -1
        #Menggeser Element
        if desc :
            #Pengurutan Descending
            while j >= 0 and array[j] < key_item :
                array[j+1] = array[j]
                j -= 1
        else :
            #Pengurutan Ascending
            while j >= 0 and array[j] > key_item :
                array[j+1] = array[j]
                j -= 1

        array[j+1] = key_item
    return array

print('----Menu Pengurutan----')
print('1. Masukan Array')
print('2. Bubble Sort')
print('3. Selection Sort')
print('4. Insertion Sort')
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
    elif (menu==3):
        print('Pengurutan Selection Sort')
        print('-' * 20)
        array_selection = unordered_array
        print('Array Belum Terurut')
        print(unordered_array)
        print('Array Yang Sudah Terurut')
        print(selection_sort(array_selection,desc=True))
    elif (menu==4):
        print('Pengurutan insertion Sort')
        print('-' * 20)
        array_insertion = unordered_array
        print('Array Belum Terurut')
        print(unordered_array)
        print('Array Yang Sudah Terurut')
        print(insertion_sort(array_insertion))
    else :
        print('Pilihan Menu Tidak Ada')

    print()
    print('----Menu Pengurutan----')
    print('1. Masukan Array')
    print('2. Bubble Sort')
    print('3. Selection Sort')
    print('4. Insertion Sort')
    print('0. Keluar')
    print('-' * 20)
    menu = int(input('Pilih Menu : '))
else:
    print('Terima Kasih Telah Menggunakan Aplikasi Ini.')