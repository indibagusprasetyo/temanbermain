#Menghitung Jarak Tempuh
#I.S : Pengguna Memasukan Jarak Dalam (CM)
#F.S : Program Menampilkan Total Jarak Dalam (CM/M/KM)

print('Konversi Jarak')
sentimeter = int(input("Masukan Jarak dalam CM : "))

meter = sentimeter // 100
kilometer = sentimeter // 1000

print("Hasil Konversi" ,sentimeter,"cm :", meter,"m :", kilometer,"km :")

