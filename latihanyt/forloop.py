#Perulangan (loop) FOR

#ini dengan list
angka = [0,1,2,3,4] #ini adalah list
print(angka)

for i in angka:
    print(f"i sekarang -> {i}")

print("akhir dari program 1\n")


#ini dengan range
angka2 = range(5)
for i in angka2:
    print(f"i sekarang -> {i}")

print("akhir dari program 2a\n")

angka2 = range(1,10)
for i in angka2:
    print(f"i sekarang -> {i}")

print("akhir dari program 2b\n")

#Menggunakan string
data_str = "saya pintar"

for i in data_str:
    print(data_str)

print("akhir dari program str\n")