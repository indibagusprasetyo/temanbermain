#Program Validasi Tanggal
#I.S : Pengguna memasukan tanggal, bulan, tahun
#F.S :

input(tanggal,bulan,tahun)

if (bulan=1) or (bulan=3) or (bulan=5) or (bulan=7) or (bulan=8) or (bulan=10) or (bulan=12) then
jumlah hari <- 31
elif(bulan=4) or (bulan=6) or (bulan=6) or (bulan=11) then
jumlah hari <- 30
elif(bulan=2) then
    if(tahun mod 4 = 0) and (tahun mod 100 != 0) or (tahun mod 400 = 0) then
    jumlah_hari = 29
    else
    jumlah_hari = 28
    endif
else
validitas <- false
endif

if (tanggal < jumlah_hari) :
    validitas <- true
else
     validitas <- false
endif

if (validitas = true)
    output("tanggal valid")
else
    output("tanggal tidak valid")
endif
