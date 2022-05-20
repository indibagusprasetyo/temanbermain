data_angka = [1,2,5,5,6,2,3,6,1,8]

print(f"data angka = \n{data_angka}")
#count data

jumlah_data_4= data_angka.count(4)
jumlah_data_3= data_angka.count(3)

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

#ambil posisi data
data = ["Ucup","Otong","Dudi","Agus"]

print(f"data = {data}")

index_Otong = data.index("Otong")
print(f"index si Otong = {index_Otong}")

# mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = {data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

#membalik list (descend)
data_angka.reverse()
data.reverse()
print(f"data diReverse = \n{data_angka} \n{data}")