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
class DoubleLinkedList :
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
            while bantu is not None:
                print(bantu.info,'',end='')
                if bantu.next is not None:
                    print('->',end='')
                bantu = bantu.next
            print()

    def Penghancuran (self):
        phapus = self.awal
        while phapus is not None:
            self.awal = phapus.next
            del phapus
            phapus = self.awal
        self.akhir = None

# Penambahan Di Depan
    def SisipDepanDouble (self,dataBaru):
        baru = Node(dataBaru)
        if (self.isEmpty()):
            self.akhir = baru
        else:
            baru.next = self.awal
            self.awal.prev = baru
        self.awal = baru
# Penambahan Belakang
    def SisipBelakangDouble(self,dataBaru):
        baru = Node(dataBaru)
        if (self.isEmpty()):
            self.awal = baru
        else:
            baru.prev = self.akhir
            self.akhir.next = baru
        self.akhir = baru
#Penambahan di tengah (sisip)
    def SisipTengahDouble(self,dataBaru):
        sisipSetelah = int(input("Sisipkan Setelah : "))
        bantu = self.awal
        ketemu = False
        posisi = 1
        while (not ketemu) and (bantu is not None):
            if (bantu.info == sisipSetelah):
                ketemu = True
            else:
                bantu = bantu.next

        if (ketemu):
            baru = Node(dataBaru)
            if (bantu == self.akhir):
                self.SisipBelakangDouble(dataBaru)
            else:
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
    def hapusDepanDouble(self):
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
                self.awal.prev = None
            del Phapus
            print("Data yang dihapus adalah : ",elmen)
# Oprasi Penghapusan Belakang
    def hapusBelakangDouble(self):
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
                self.akhir.next = None
            del Phapus
            print("Data yang dihapus adalah : ",elmen)
# Oprasi Penghapusan Tengah
    def hapusTertentuDouble(self):
        if(self.isEmpty()):
            print('Data Kosong')
        else:
            dataHapus = int(input("Data yang ingin Dihapus : "))
            Phapus = self.awal
            ketemu = False
            while (not ketemu) and (Phapus is not None):
                if (Phapus.info == dataHapus):
                    ketemu = True
                else:
                    Phapus = Phapus.next
            
            if(ketemu):
                elmen = Phapus.info
                if(Phapus == self.akhir):
                    self.hapusBelakangDouble()
                elif(Phapus == self.awal):
                    self.hapusDepanDouble()
                else:
                    Phapus.prev.next = Phapus.next
                    Phapus.next.prev = Phapus.prev
                    del Phapus
                    print("Data yang dihapus adalah : ",elmen)
            
            else:
                print("Data Hapus Tidak Ditemukan")

# 2. Inisialisasi Linked List
list1 = DoubleLinkedList()
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
print("0. Keluar")
menu = int(input('Masukkan Menu Pilihan Anda : '))

while (menu != 0):
    if (menu == 1):
        DataBaru = int(input("Masukkan Data Baru : "))
        if(list1.isEmpty()):
            list1.SisipDepanDouble(DataBaru)
        else:
            print("1. Sisip Depan")
            print("2. Sisip Belakang")
            print("3. Sisip Tengah")
            menu2 = int(input("Masukkan Pilihan Tambah : "))
            if (menu2 == 1):
                list1.SisipDepanDouble(DataBaru)
            elif (menu2 == 2):
                list1.SisipBelakangDouble(DataBaru)
            elif (menu2 == 3):
                list1.SisipTengahDouble(DataBaru)
            else:
                print("Menu Tambah Tidak Ada")
        list1.TampilData()
    elif (menu == 2):
        print("1. Hapus Depan")
        print("2. Hapus Belakang")
        print("3. Hapus Tengah")
        menu2 = int(input("Masukkan Pilihan Tambah : "))
        if (menu2 == 1):
            list1.hapusDepanDouble()
        elif (menu2 == 2):
            list1.hapusBelakangDouble()
        elif (menu2 == 3):
            list1.hapusTertentuDouble()
        else:
            print("Menu Hapus Tidak Ada")
        list1.TampilData()
    elif (menu == 3):
        print("Tampil Data")
        list1.TampilData()
        print()
        print("Tampil Data Dari Belakang")
        list1.TampilData()
        print()
    else:
        print("Pilihan Menu Tidak Ada")
    
    print()
    print('--- Menu ---')
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampil Data")
    print("0. Keluar")
    menu = int(input('Masukkan Menu Pilihan Anda : '))
else:
    print('Terima Kasih')
    list1.Penghancuran()