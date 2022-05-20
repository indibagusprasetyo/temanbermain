#Program Konversian Waktu Ke detik
#I.S : Memasukan Waktu
#F.S : Menampilkan Hasil Konversi

jj = int(input("jam :"))
mm = int(input("menit :"))
dd = int(input("detik :"))

TotalDetik = (jj * 3600) + (mm * 60) + dd
print("jam : ",jj)
print("menit : ",mm)
print("detik : ",dd)
print("TotalDetik : ",TotalDetik)

