# latihan perulangan membuat segitiga

sisi = 12

# 1. menggunakan for

#dummy variable
print("Awal For")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

print("Akhir for")


# 2. menggunakan while
print("Awal while")

count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break
print("Akhir while")



# 3. hanya ganjil saja
print("Awal while")
count = 1
while True:
    if (count % 2):
        #print jika ganjil
        print("*"*count)
        count += 1
    else:
        #akan kembali jika ganjil
        count += 1
        continue

    #akan break bila melebihi sisi
    if count > sisi:
        break
print("Akhir while")

# 4. hanya ganjil saja
print("Awal while")
count = 1
spasi = int(sisi/2)
while True:
    if (count % 2):
        #print jika ganjil
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        #akan kembali jika ganjil
        count += 1
        continue

    #akan break bila melebihi sisi
    if count > sisi:
        break
print("Akhir while")