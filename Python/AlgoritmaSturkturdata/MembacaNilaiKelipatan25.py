#Menghitung Jarak Tanggal
#I.S : Pengguna Memasukan Nominal Uang dalam Bentuk Pecahan
#F.S : Program Menampilkan Banyaknya Pecahan dalam Nominal Tersebut

print('Konversi Pecahan Kelipatan 25')
nominal = int(input("Masukan Nominal Pecahan (Kelipatan 25) : Rp. "))
#P = Pecahan
#S = Sisa
P1000 = nominal // 1000
S1000 = nominal % 1000
P500 = S1000 // 500
S500 = S1000 % 500
P100 = S500 // 100
S100 = S500 % 100
P50 = S100 // 50
S50 = S100 % 50
P25 = S50 // 25
S25 = S50 % 25

print("Banyaknya Pecahan dalam Rp:",nominal,"Nilai 1000 :", P1000,"Nilai 500 :", P500,("Nilai 100 :"), P100,"Nilai 50 :", P50,"Nilai 25 :", P25)
