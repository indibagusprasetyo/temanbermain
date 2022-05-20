# Operasi

# index  0/-3    1/-2    2/-1
data = ["Asep", "Andri", "Tono"]

# mengambil data dari list ini
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_2 = data[-1]
print(f"data pertama (index 0) = {data_2}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# manipulasi data list

#menambahkan item data pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

# index.insert(posisi,item)
data.insert(1,"Agus")
print(f"data sesudah ditambah = \n{data}")

#menambah diakhir list
data.append("Juju")
print(f"data ditambah lagi = \n{data}")

# menambahkan list dengan list
data_baru = ["Ujang","Deden","Asrap"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

#merubah data
data[2] = "Gilbert"
print(f"data rubah = \n{data}")

#menghapus data
data.remove("Ujang")
print(f"data remove = \n{data}")

#meremove data paling belakang
data_akhir = data.pop()
print(f"data akhir = \n{data}")
print(data_akhir)