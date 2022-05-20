data_0 = [0,1]
data_1 = [3,4]

data_list_biasa = [1,2,3,4]
print(f"list biasa = {data_list_biasa}")
list_2D = [data_0,data_1,6,7]
print(f"list 2D = {list_2D}")

#contoh penggunaan
peserta_0 = ["Ucup",26,"Laki-laki"]
peserta_1 = ["Otong",12,"Laki-laki"]
peserta_2 = ["Dedeh",52,"Perempuan"]

list_peserta = [peserta_0,peserta_1,peserta_2]

print(f"peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"nama\t: {peserta[0]}")
    print(f"umur\t: {peserta[1]}")
    print(f"gender\t: {peserta[2]}\n")

# dengan reference
list_copy = list_peserta.copy();
print(f"peserta = {list_copy}")
