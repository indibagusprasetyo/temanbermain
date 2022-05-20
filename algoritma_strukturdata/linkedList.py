#1. Pendefinisian Struktur Data Linked List

#Class Untuk Node
class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

#Class Untuk Linked list
class LinkedList:
    def __init__(self):
        self.awal = None

    def isEmpty(self):
        return  self.awal is None

    def TampilData(self):
        print('Isi Linked List :',end='')
        if self.isEmpty():
            print('Data Kosong')
        else:
            bantu = self.awal
            while bantu is not None:
                print(bantu.info, "", end='')
                if bantu.next is not None:
                    print("-> ", end='')
                bantu = bantu.next
            print()

    def BanyakNode(self):
        if self.isEmpty():
            byknode = 0
        else:
            bantu = self.awal
            byknode = 0
            while bantu is not None:
                #byknode += 1
                byknode = byknode + 1
                bantu = bantu.next
        return  byknode

    def Penghancuran(self):
        Phapus = self.awal
        while Phapus is not None:
            self.awal = Phapus.next
            del Phapus
            Phapus = self.awal

#Operasi Pencarian
#Pencarian Data Angka
    def PencarianAngka(self):
        if (self.isEmpty()):
            print("Data Kosong")
        else :
            CariAngka = int(input("Masukan Angka Yang Dicari : "))
            bantu = self.awal
            ketemu = False
            while (not ketemu) and (bantu is not None):
                if (bantu.info == CariAngka):
                    ketemu = True
                else:
                    bantu = bantu.next

            if (ketemu):
                print('Angka',CariAngka,'Ditemukan')
            else :
                print('Angka',CariAngka,'Tidak Ditemukan')

#Pencarian Node
    def PencarianNode(self):
        if (self.isEmpty()):
            print("Data Kosong")
        else :
            CariNode = int(input("Masukan Node Yang Dicari : "))
            bantu = self.awal
            ketemu = False
            posisi = 1
            while (not ketemu) and (bantu is not None):
                if (posisi == CariNode):
                    ketemu = True
                else:
                    bantu = bantu.next
                    posisi += 1

            if (ketemu):
                print('Node Ke-',CariNode,'Ditemukan')
            else :
                print('Node Ke-',CariNode,'Tidak Ditemukan')

#Operasi Penambahan
#Penambahan Di Depan
    def SisipDepan(self,DataBaru):
        Baru = Node(DataBaru)
        if(not self.isEmpty()) :
            Baru.next = self.awal
        self.awal = Baru

#Penambahan Di Belakang
    def SisipBelakang(self,DataBaru):
        Baru = Node(DataBaru)
        if(self.isEmpty()):
            self.awal = Baru
        else:
            bantu = self.awal
            while(bantu.next is not  None):
                bantu = bantu.next
            bantu.next = Baru

#Penambahan Di Tengah (sisip)
    def SisipTengah(self, DataBaru):
        SisipSetelah = int(input("Sisip Setelah : "))
        bantu = self.awal
        ketemu = False
        while (not ketemu) and (bantu is not None):
            if (bantu.info == SisipSetelah):
                ketemu = True
            else:
                bantu = bantu.next

        if(ketemu):
            Baru = Node(DataBaru)
            if(bantu.next is None):
                self.SisipBelakang(DataBaru)
            else:
                Baru.next = bantu.next
                bantu.next = Baru
        else:
            print('Data',SisipSetelah,'Tidak Ditemukan')

#Operasi Pengubahan Data
    def UbahData(self):
        if(self.isEmpty()):
            print('Data Kosong')
        else:
            DataUbah = int(input("Masukan Data Yang Ingin Di Ubah : "))
            bantu = self.awal
            ketemu = False
            while (not ketemu) and (bantu is not None):
                if (bantu.info == DataUbah):
                    ketemu = True
                else:
                    bantu = bantu.next

            if(ketemu):
                DataBaru = int(input('Masukan Data Peubah :'))
                bantu.info = DataBaru
            else :
                print("Data Tidak Ditemukan")

#Operasi Penghapusan
    def SatuNode(self): #Pemerikasaan Node
        bantu = self.awal
        if(bantu.next is None):
            return True
        else:
            return False

# Hapus Didepan
    def HapusDepan(self):
        if(self.isEmpty()):
            print("Data Kosong")
        else:
            Phapus = self.awal
            elemen = Phapus.info
            if(self.SatuNode()):
                self.awal = None
            else:
                self.awal = Phapus.next

            del  Phapus
            print('Data Yang Dihapus Adalah : ', elemen)

# Hapus DiBelakang
    def HapusBelakang(self):
        if(self.isEmpty()):
            print('Data Kosong')
        else:
            Phapus = self.awal
            if(self.SatuNode()):
                self.awal = None
            else:
                # Mencari Node Terakhir
                while (Phapus.next is not None):
                    Phapus = Phapus.next
                # Mencari Node Sebeleum Node Terakhir
                bantu = self.awal
                while(bantu.next is not Phapus):
                    bantu = bantu.next

                bantu.next = None

            elemen = Phapus.info
            del Phapus
            print('Data Yang Dihapus Adalah : ', elemen)

# Hapus DiTengah
    def HapusTengah(self):
        if(self.isEmpty()):
            print('Data Kosong')
        else:
            DataHapus = int(input("Masukan Data Yang Ingin Di Hapus : "))
            Phapus = self.awal
            ketemu = False
            while (not ketemu) and (Phapus is not None):
                if (Phapus.info == DataHapus):
                    ketemu = True
                else:
                    Phapus = Phapus.next

            if(ketemu):
                elemen = Phapus.info
                if (Phapus == self.awal):
                    self.HapusDepan()
                elif(Phapus.next is None):
                    self.HapusBelakang()
                else:
                    # Mencari Node Sebelum Node Yang Akan Dihapus
                    bantu = self.awal
                    while(bantu.next is not Phapus):
                        bantu = bantu.next

                    bantu.next = Phapus.next

                    del Phapus
                    print('Data Yang Dihapus Adalah',elemen)
            else:
                print('Data',DataHapus,'Tidak Ditemukan')

#Pengurutan Data Secara Acsecding Menggunakan Selection Sort (Minimum Sort)
    def UrutData(self):
        i = self.awal
        while(i.next is not None):
            min = i
            j = i.next
            while(j is not None):
                if (j.info < min.info):
                    min = j
                j = j.next

            #Proses Pertukaran
            temp = min.info
            min.info = i.info
            i.info = temp

            #Tempatkan i Ke Simpul Berikutnya
            i = i.next


#2. Inisialisasi linked List
list1 = LinkedList()
print('Awal Linked List :',list1.awal)

#3. Memasukan Data Linked List Secara Langsung
node1 = Node(5)
node2 = Node(7)
node3 = Node(2)
node4 = Node(10)

#print('isi Node 1 : ',node1.info,'-',node1.next)
#print('isi Node 2 : ',node2.info,'-',node2.next)

#Membuat Linked List
list1.awal = node1
node1.next = node2
node2.next = node3
node3.next = node4

#print('isi Node 1 : ',node1.info,'-',node1.next)
#print('isi Node 2 : ',node2.info,'-',node2.next)

#4. Traversal Untuk Menampilkan Data
list1.TampilData()

#5 Traversal Untuk Mengghitung Banyak Data
#print('Banyak Data : ',list1.BanyakNode())

#7. Pencarian Data Linked List
#Pencarian Angka
#list1.PencarianAngka()
#Pencarian Node
#list1.PencarianNode()

#8. Penamabahan Data Linkk List
#DataBaru = int(input('Masukan Data Baru : '))
#penambahan Di Depan
#list1.SisipDepan(DataBaru)

#Penambahan Di Belakang
#list1.SisipBelakang(DataBaru)

#Penambahan Di Tengah
#list1.SisipTengah(DataBaru)

#9.Pengubahan Data
#list1.UbahData()

#10.Pengahpusan Data LinkedList
#Hapus Didepan
#list1.HapusDepan()

#Hapus Dibelakang
#list1.HapusBelakang()

#Hapus Ditengah
#list1.HapusTengah()

#11.Pengurutan Data Linked List
# if(list1.isEmpty()):
#     print("Data kosong")
# else:
#     list1.UrutData()
# print("Data Sudah Terurut")
# list1.TampilData()

# 6. Penghancuran Linked List
list1.Penghancuran()
#list1.TampilData()