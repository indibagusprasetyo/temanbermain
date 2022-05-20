#1. Pendefinisian Struktur Data Linked List
#Class untuk Node


class Node :
    def __init__(self, info) :
        self.info = info
        self.next = None

#Class untuk LinkedList
class LinkedList :
    def __init__(self) :
        self.awal = None

    def isEmpty(self):
        return self.awal is None

    def TampilData(self):
        print("Isi Linked List : ",end='')
        if self.isEmpty() :
            print("Data Kosong")
        else :
            bantu = self.awal
            while bantu is not None :
                print(bantu.info," ",end='')
                if bantu.next is not None :
                    print('->',end=' ')
                bantu = bantu.next
            print()

    def BanyakNode(self):
        if self.isEmpty() :
            byknode = 0
        else :
            bantu = self.awal
            byknode = 0
            while bantu is not None :
                #byknode += 1
                byknode = byknode + 1
                bantu = bantu.next
            return byknode
    def Penghancuran(self):
        Phapus = self.awal
        while Phapus is not None :
            self.awal = Phapus.next
            del Phapus
            Phapus = self.awal

#Operasi pencarian
#Pencarian data angka
    def PencarianAngka(self) :
        if (self.isEmpty()):
            print("Data Kosong")
        else :
            CariAngka = int(input("Masukan angka yang dicari : "))
            bantu = self.awal
            ketemu = False
            while (not ketemu) and (bantu is not None):
                if(bantu.info) == CariAngka :
                    ketemu = True
                else :
                    bantu = bantu.next
            
            if(ketemu) :
                print("Angka", CariAngka, "Ditemukan")
            else :
                print("Angka",CariAngka,"Tidak ditemukan")

#Pencarian node
    def PencarianNode(self) :
        if (self.isEmpty()):
            print("Data Kosong")
        else :
            CariNode = int(input("Masukan Node yang dicari : "))
            bantu = self.awal
            ketemu = False
            posisi = 1
            while (not ketemu) and (bantu is not None):
                if(bantu.info) == CariNode :
                    ketemu = True
                else :
                    bantu = bantu.next
            
            if(ketemu) :
                print("Node Ke-", CariNode, "Ditemukan")
            else :
                print("Node Ke-",CariNode,"Tidak ditemukan")

#Operasi penambahan
#Penambahan didepan
    def SisipDepan (self, DataBaru):
        Baru = Node(DataBaru)
        if(not self.isEmpty):
            Baru.next = self.awal

        self.awal = Baru
#Penambahan dibelakang
    def SisipBelakang(self, DataBaru):
        Baru = Node(DataBaru)
        if(self.isEmpty()):
            self.awal = Baru
        else :
            bantu = self.awal
            while (bantu.next is not None):
                bantu = bantu.next
            bantu.next = Baru
        
#Penambahan ditengah
    def SisipTengah(self , DataBaru) :
        SisipSetelah = int(input("Sisipkan Setelah"))
        bantu = self.awal
        ketemu = False
        while (not ketemu) and (bantu is not None):
            if(bantu.info) == CariAngka :
                ketemu = True
            else :
                bantu = bantu.next

        if(ketemu) :
            Baru = Node(DataBaru)
            if(bantu.next is None):
                self.SisipBelakang(DataBaru)
            else:
                Baru.next = bantu.next
                bantu.next = Baru
        else :
            print("Data",SisipSetelah,"Tidak Ditemukan")

#Operasi pengubahan data
    def UbahData(self):
        if(self.isEmpty()):
            print("Data Kosong")
        else:
            DataUbah = int(input("Sisipkan Setelah"))
            bantu = self.awal
            ketemu = False
            while (not ketemu) and (bantu is not None):
                if(bantu.info) == DataUbah :
                    ketemu = True
                else :
                    bantu = bantu.next

                if(ketemu):
                    DataBaru = int(input("Masukan Data Peubah : "))
                    bantu.info = DataBaru
                else :
                    print("Data", DataUbah,"Tidak Ditemukan")

#Operasi Penghapusan
    def SatuNode(self) :
        bantu = self.awal
        if(bantu.next is None) :
            return True
        else :
            return False

#Penghapusan didepan
    def HapusDepan (self) :
        if(self.isEmpty()) :
            print("Data Kosong")
        else :
            Phapus = self.awal
            Element = Phapus.info
            if(self.SatuNode()):
                self.awal = None
            else :
                self.awal = Phapus.next
            
            del Phapus
            print("Data yang dihapus adalah : ", Element)

#Penghapusan dibelakang
    def HapusBelakang (self) :
        if(self.isEmpty()) :
            print("Data Kosong")
        else :
            Phapus = self.awal
            if(self.SatuNode()) :
                self.awal = None
            else :
                #Mencari Node Terakhir
                while (Phapus.next is not None) :
                    Phapus = Phapus.next

                #Mencari Node Sebelum Node Terakhir
                bantu = self.awal
                while (bantu.next is not Phapus) :
                    bantu = bantu.next

                bantu.next = None

            Element = Phapus.info
            del Phapus
            print("Data yang dihapus adalah : ", Element)

#Penghapusan diTengah
    def HapusTengah(self):
        if(self.isEmpty()) :
            print("Data Kosong")
        else :
            DataHapus = int(input("Masukan data yang ingin dihapus :"))
            Phapus = self.awal
            ketemu = False
            while (not ketemu) and (Phapus is not None):
                if(Phapus.info) == DataHapus :
                    ketemu = True
                else :
                    Phapus = Phapus.next

            if(ketemu) :
                Element = Phapus.info
                if(Phapus == self.awal) :
                    self.HapusDepan()
                elif (Phapus.next is None):
                    self.HapusBelakang()
                else:
                    #Mencari Node sebelum Node yang ingin dihapus
                    bantu = self.awal
                    while(bantu.next is not Phapus) :
                        bantu = bantu.next
                    bantu.next = Phapus.next

                    del Phapus
                    print("Data yang dihapus adalah : ", Element)
            else :
                print("Data",DataHapus,"Tidak Ditemukan")

#Pengurutan data secara Ascending menggunakan selection sort (minimum sort)
    def urutData(self):
        i = self.awal
        while (i.next is not None) :
            min = i
            j = i.next
            while(j is not None):
                if(j.info < min.info) :
                    min = j
                j = j.next

            #Proses Pertukaran
            temp = min.info
            min.info = i.info
            i.info = temp

            #Tempatkan i ke simpul berikutnya
            i = i.next


#2. Inisialiasai Linked List
list1 = LinkedList()
# print("Awal Linked List :", list1.awal)

#3. Memasukan data ke Linked List Secara langsung
node1 = Node(5)
node2 = Node(12)
node3 = Node(19)
node4 = Node(7)

# print("Isi dari node1 adalah : ", node1.info,'-', node1.next)
# print("Isi dari node2 adalah : ", node2.info,'-', node2.next)
# print("Isi dari node3 adalah : ", node3.info,'-', node3.next)
# print("Isi dari node4 adalah : ", node4.info,'-', node4.next)

# print("\n\n\n")

#4. Membuat Linked List
list1.awal = node1
node1.next = node2
node2.next = node3
node3.next = node4

# print("Isi dari node1 adalah : ", node1.info,'-', node1.next)
# print("Isi dari node2 adalah : ", node2.info,'-', node2.next)
# print("Isi dari node3 adalah : ", node3.info,'-', node3.next)
# print("Isi dari node4 adalah : ", node4.info,'-', node4.next)

# #4.2 Transversal untuk menampilkan Data Linked List
# list1.TampilData()

# #5. Transversal untuk menghitung banyak data
# print("Banyak data : ",list1.BanyakNode())

#7.Pencarian Data angka Linked List

#Pencarian angka
#list1.PencarianAngka()

#pencarianNode
# list1.PencarianNode()

#8. Penambahan data linkedList
# DataBaru = int(input("Masukan Data Baru : "))

#9. Pengubahan data linked list
# list1.UbahData()

#10. Penghapusan data linked list
#Penghapusan didepan
list1.HapusDepan()
#Penghapusan dibelakang
# list1.HapusBelakang()
#Penghapusan ditengah
# list1.HapusTengah()


#11. Pengurutan data linked list
# if (list1.isEmpty()) :
#     print("Data Kosong")
# else :
#     list1.urutData()

#Penambahan didepan
# list1.SisipDepan(DataBaru)
# list1.TampilData()

# #Penambahan dibelakang
# list1.SisipBelakang(DataBaru)
# list1.TampilData()

#Penambahan ditengah
# list1.SisipTengah(DataBaru)
# list1.TampilData()

#9. Perubahan Data
# list1.UbahData(DataBaru)
# list1.TampilData()

#6. Penghancuran Linked List
list1.Penghancuran()
# list1.TampilData()