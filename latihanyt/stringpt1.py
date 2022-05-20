#operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = "Indi"
nama_tengah = "Bagus"
nama_akhir = "Prasetyo"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. operator untuk string

# mengecek apakah ada komponen char atau string di sebuah string

d = "d"
status = d in nama_lengkap
print( d + " ada di " + nama_lengkap + " = " + str(status))

D = "D"
status = D in nama_lengkap
print( D + " ada di " + nama_lengkap + " = " + str(status))

d = "d"
status = d not in nama_lengkap
print( d + " ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("xi"*12)
print(12*"xi")

#indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[1])
print("index ke-7 : " + nama_lengkap[7])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-8) : " + nama_lengkap[-8])
print("index ke-[0:4] : " + nama_lengkap[0:4])
print("index ke-[5:10] : " + nama_lengkap[5:10])
print("index ke-[0:2:4:6:8:10] : " + nama_lengkap[0:11:2])

#item paling kecil
print("paling kecil : " + min(nama_lengkap))

#item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# 4. operator dalam bentuk method

data = " Indi adalah seorang Mahasiswa"
jumlah = data.count("a")
print("jumlah a pada " + data + " = " + str(jumlah))