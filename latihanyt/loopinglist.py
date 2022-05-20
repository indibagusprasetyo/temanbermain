#looping dari list
#for loop
print("for loop")
angka_angka = [4,5,3,8,3,2,9,1]

for angka in angka_angka:
    print(f"angka = {angka}")

peserta = ["agus","acep","indah","reni","elsy"]

for nama in peserta:
    print(f"nama = {nama}")

# for loop dan range
print("\nfor dan range")
kumpulan_angka = [1,2,3,4,5,6,7]

panjang = len(kumpulan_angka)

for i in range (panjang):
    print(f"angka = {kumpulan_angka[i]}")

# while 
print("\nwhile")
kumpulan_angka = [1,2,3,4,5,6,7]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

# list comprehension
print("\nList comprehension")
data = ["alex","ade","andini",2,3,6,1,"lion"]

[print(f"data={i}")for i in data]

print("\nData Kuadrat")

angka = [1,2,3,4,5,6,7]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)



#enumerate
print("\nEnumerate")
data_list = ["alex","ade","andini",2,3,6,1,"lion"]

for index,data in enumerate(data_list):
    print(f"index = {index}, data = {data}")