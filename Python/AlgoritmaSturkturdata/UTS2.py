#Program Menghitung Tarif Biaya Telefon
#I.S : Pengguna memasukan Waktu awal, dan akhir, serta kode wiilayah (kodwil) tujuan.
#F.S : Program menampilkan kode wilayah (kodwil), durasi waktu, tujuan telefon (kota), dan biaya percakapan


#Algoritma

##input

jamawal     = int(input("Masukan Jam Awal :"))
menitawal   = int(input("Masukan Menit Awal :"))
detikawal   = int(input("Masukan detikawal :"))

jamakhir    = int(input("Masukan Jam Akhir :"))
menitakhir  = int(input("Masukan Menit Akhir :"))
detikakhir  = int(input("Masukan Detik Akhir :"))

##Process
detwal      = jamawal * 3600 + menitawal * 60 + detikawal
dethir      = jamakhir * 3600 + menitakhir * 60 + detikakhir
durasi      = dethir - detwal

durjam      = durasi // 3600
dursa       = durasi % 3600

durnit      = dursa // 60

durtik      = dursa % 60

##Output
print("-----Wilayah Telepon-----")
print("| Kode Wilayah | Wilayah Kota |")
print("|    021       | Jakarta      |")
print("|    0751      | Padang       |")
print("|    0737      | Medan        |")
print("|    0912      | Balikpapan   |")
print("|    0981      | Ternate      |")

##Inputkodwil
kodwil      = str(input("Masukan Kode Wilayah :"))

##Ouput durasi and process kodwil
print(durjam,":",durnit,":",durtik)

if (kodwil=="021"):
    print("Tujuan Telepon anda Ke Kota Jakarta")
    print("Biaya Percakapan Rp.",durasi / 60 * 150)
elif (kodwil=="0751"):
    print("Tujuan Telepon anda Ke Kota Padang")
    print("Biaya Percakapan Rp.",durasi / 30 * 250)
elif (kodwil=="0737"):
    print("Tujuan Telepon anda Ke Kota Medan")
    print("Biaya Percakapan Rp.",durasi / 25 * 375)
elif (kodwil=="0912"):
    print("Tujuan Telepon anda Ke Kota Balikpapan")
    print("Biaya Percakapan Rp.",durasi / 20 * 415)
elif (kodwil=="0981"):
    print("Tujuan Telepon anda Ke Kota Ternate")
    print("Biaya Percakapan Rp.",float((durasi / 17 ) * 510))
else : print("Tidak ada kode kota Tujuan")