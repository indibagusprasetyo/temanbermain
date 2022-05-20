# string
# operator dalam bentuk methods
# merubah case dari string
# merubah semua ke uppercase

salam = "Assalamu'alaikum"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)


# merubah semua ke lowercase
salam = salam.lower()
print("lower = " + salam)

# pengecekan dengan isX method

# contoh pengecekan lowercase
salam = "hola!"
apakah_lower = salam.islower() #Hasilnya Bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() #Hasilnya Bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semua huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab \t, newline \n atau \r
# istitle() <-- semua kata dimulai dengan huruf besar

judul = "Squid Game"
cek_judul = judul.istitle() #hasilnya bool

print(judul + " is title = " + str(cek_judul))


#ngecek komponen startswith() endswith()
cek_start = "Cyka Blyat".startswith("Cyka")
print("start = " + str(cek_start))
cek_start = "Cyka Blyat".startswith("Blyat")
print("start = " + str(cek_start))

cek_ends = "Cyka Blyat".endswith("Blyat")
print("ends = " + str(cek_ends))
cek_ends = "Cyka Blyat".endswith("Cyka")
print("ends = " + str(cek_ends))

#Penggabungan Komponen join() split()
#.join
pisah = ['aku','sayang','kamu']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

pisah = ['aku','sayang','kamu']
gabung = ' '.join(pisah)
print(pisah)
print(gabung)

#.split
gabung = "aku,sayang,kamu"
print(gabung.split(','))

# alokasi karakter rjust() ljust() center()
print(5*"=" + "data" + "="*5)

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(10)
print("'"+tengah+"'")

tengah = "tengah".center(20,"~")
print("'"+tengah+"'")

# kebalikannya --> strip()

tengah = tengah.strip("~")
print("'"+tengah+"'")