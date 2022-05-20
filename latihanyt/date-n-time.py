# Date and time (latihan)

import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)

tanggal = dt.date(2002,1,30)
print(tanggal)

#mulai
print('silahkan masukan tanggal, \nbulan lahir anda, dan tahun lahir anda')

tanggal = int(input("Tanggal \t:"))
bulan = int(input("Bulan \t\t:"))
tahun = int(input("Tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah = {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal = {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"Umur anda = {umur_hari}")
print(f"Harinya adalah = {tanggal_lahir:%A}")
print(f"Umur anda = {umur_tahun} tahun, {umur_bulan_sisa} bulan")