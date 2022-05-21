# 1. Pendefinisian dari struktur data linked list
# Class untuk Node

from cmath import phase
# from time import pthread_getcpuclockid


class Node :
    def __init__(self, info) :
        self.info = info
        self.next = None
        self.prev = None

# Class untuk Linked List
class DoubleCircularLinkedList :
    def __init__(self):
        self.awal = None
        self.akhir = None

    def isEmpty(self):
        return self.awal is None

    def TampilData (self):
        print('Isi dari Linked List : ',end='')
        if self.isEmpty():
            print("Data itu kosong")
        else:
            bantu = self.awal
            while (bantu != self.akhir):
                print(bantu.info,'',end='')
                if bantu.next is not None:
                    print('->',end='')
                bantu = bantu.next
            print(bantu.info) #Menampilkan node yang diakhir
            print()

    def TampilData2 (self):
        print('Isi dari Linked List : ',end='')
        if self.isEmpty():
            print("Data itu kosong")
        else:
            bantu = self.akhir
            while (bantu != self.awal):
                print(bantu.info,'',end='')
                if bantu.prev is not None:
                    print('->',end='')
                bantu = bantu.prev
            print(bantu.info) #Menampilkan node awal
            print()

    def Penghancuran (self):
        phapus = self.awal
        while (phapus != self.akhir):
            self.awal = phapus.next
            self.awal.prev = self.akhir
            self.akhir.next = self.awal
            del phapus
            phapus = self.awal
        self.akhir = None
        self.awal = None
        del phapus

# Penambahan Di Depan
    def SisipDepanCircularDouble (self,dataBaru):
        baru = Node(dataBaru)
        if (self.isEmpty()):
            self.akhir = baru
        else:
            baru.next = self.awal
            self.awal.prev = baru
        self.awal = baru
        #Penambahan untuk circular
        self.awal.prev = self.akhir
        self.akhir.next = self.awal
# Penambahan Belakang
    def SisipBelakangCircularDouble(self,dataBaru):
        baru = Node(dataBaru)
        if (self.isEmpty()):
            self.awal = baru
        else:
            baru.prev = self.akhir
            self.akhir.next = baru
        self.akhir = baru
        #Penambahan untuk circular
        self.awal.prev = self.akhir
        self.akhir.next = self.awal
#Penambahan di tengah (sisip)
    def SisipTengahCircularDouble(self,dataBaru):
        sisipSetelah = int(input("Sisipkan Setelah : "))
        bantu = self.awal
        while (bantu.info != sisipSetelah) and (bantu != self.akhir):
            bantu = bantu.next

        if (bantu.info == sisipSetelah):
            if (bantu == self.akhir):
                self.SisipBelakangDouble(dataBaru)
            else:
                baru = Node(dataBaru)
                baru.next = bantu.next
                baru.prev = bantu
                bantu.next.prev = baru
                bantu.next = baru
        else:
            print("Data",sisipSetelah," Tidak Ditemukan")

# Oprasi Penghapusan
    def satuNode(self):
        if(self.awal == self.akhir):
            return True
        else:
            return False

# Oprasi Penghapusan Depan
    def hapusDepanCircularDouble(self):
        if(self.isEmpty()):
            print('Data Kosong')
        else:
            Phapus = self.awal
            elmen = Phapus.info
            if(self.satuNode()):
                self.awal = None
                self.akhir = None
            else:
                self.awal = Phapus.next
                self.awal.prev = self.akhir
                self.akhir.next = self.awal

            del Phapus
            print("Data yang dihapus adalah : ",elmen)
# Oprasi Penghapusan Belakang
    def hapusBelakangCircularDouble(self):
        if(self.isEmpty()):
            print("Data Kosong")
        else:
            Phapus = self.akhir
            elmen = Phapus.info
            if(self.satuNode()):
                self.awal = None
                self.akhir = None
            else:
                self.akhir = Phapus.prev
                self.akhir.next = self.awal
                self.awal.prev = self.akhir
            del Phapus
            print("Data yang dihapus adalah : ",elmen)
# Oprasi Penghapusan Tengah
    def hapusTertentuCircularDouble(self):
        if(self.isEmpty()):
            print('Data Kosong')
        else:
            dataHapus = int(input("Data yang ingin Dihapus : "))
            Phapus = self.awal
            while (Phapus.info != dataHapus) and (Phapus != self.akhir):
                Phapus = Phapus.next
            
            if(Phapus.onfo == dataHapus):
                elmen = Phapus.info
                if(Phapus == self.akhir):
                    self.hapusBelakangCircularDouble()
                elif(Phapus == self.awal):
                    self.hapusDepanCircularDouble()
                else:
                    Phapus.prev.next = Phapus.next
                    Phapus.next.prev = Phapus.prev
                    del Phapus
                    print("Data yang dihapus adalah : ",elmen)
            
            else:
                print("Data Hapus Tidak Ditemukan")

# Pengurutan Data secara Ascending menggunakan Selection Sort (Minimum Sort)
    def Urut(self):
        i = self.awal
        while (i.next != self.akhir):
            min = i
            j = i.next
            while (j != self.akhir):
                if(j.info < min.info):
                    min = j
                j = j.next

            if(j.info < min.info): #Membandingkan denngan node terakhir
                    min = j

            #Proses pertukaran
            temp = min.info
            min.info = i.info
            i.info = temp

            #Tempatkan i ke simpul selanjutnya
            i = i.next

            min = i
            j = i.next
            if(j.info < min.info): 
                    min = j

            #Proses pertukaran
            temp = min.info
            min.info = i.info
            i.info = temp

# 2. Inisialisasi Linked List
list1 = DoubleCircularLinkedList()
# print('Awal Linked List : ',list1.awal)

# 3. Memasukkan Data ke Linked List Secara Langsung
node1 = Node(5)
node2 = Node(7)
node3 = Node(2)
node4 = Node(10)

#Membuat Linked List
# list1.awal = node1
# node1.next = node2
# node2.next = node3
# node2.prev = node1
# node3.next = node4
# node3.prev = node2
# node4.prev = node3
# list1.akhir = node4

# print('Isi node 1 : ',node1.prev,'-',node1.info,'-',node1.next)
# print('Isi node 2 : ',node2.prev,'-',node2.info,'-',node2.next)
# print('Isi node 3 : ',node3.prev,'-',node3.info,'-',node3.next)
# print('Isi node 4 : ',node4.prev,'-',node4.info,'-',node4.next)

print('--- Menu ---')
print("1. Tambah Data")
print("2. Hapus Data")
print("3. Tampil Data")
print("4. Pengurutan Data")
print("0. Keluar")
menu = int(input('Masukkan Menu Pilihan Anda : '))

while (menu != 0):
    if (menu == 1):
        DataBaru = int(input("Masukkan Data Baru : "))
        if(list1.isEmpty()):
            list1.SisipDepanCircularDouble(DataBaru)
        else:
            print("1. Sisip Depan")
            print("2. Sisip Belakang")
            print("3. Sisip Tengah")
            menu2 = int(input("Masukkan Pilihan Tambah : "))
            if (menu2 == 1):
                list1.SisipDepanCircularDouble(DataBaru)
            elif (menu2 == 2):
                list1.SisipBelakangCircularDouble(DataBaru)
            elif (menu2 == 3):
                list1.SisipTengahCircularDouble(DataBaru)
            else:
                print("Menu Tambah Tidak Ada")
        list1.TampilData()
    elif (menu == 2):
        print("1. Hapus Depan")
        print("2. Hapus Belakang")
        print("3. Hapus Tengah")
        menu2 = int(input("Masukkan Pilihan Tambah : "))
        if (menu2 == 1):
            list1.hapusDepanCircularDouble()
        elif (menu2 == 2):
            list1.hapusBelakangCircularDouble()
        elif (menu2 == 3):
            list1.hapusTertentuCircularDouble()
        else:
            print("Menu Hapus Tidak Ada")
        list1.TampilData()
    elif (menu == 3):
        print("Tampil Data")
        list1.TampilData()
        print()
        print("Tampil Data Dari Belakang")
        list1.TampilData2()
        print()
    elif (menu == 4):
        print("Data sebelum diurutkan")
        list1.TampilData()
        print()
        list1.Urut()
        list1.TampilData()
        print("Data Setelah Diurutkan")
        
    else:
        print("Pilihan Menu Tidak Ada")
    
    print()
    print('--- Menu ---')
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampil Data")
    print("4. Pengurutan Data")
    print("0. Keluar")
    menu = int(input('Masukkan Menu Pilihan Anda : '))
else:
    print('Terima Kasih')
    list1.Penghancuran()