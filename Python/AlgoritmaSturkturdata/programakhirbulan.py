# Program Akhir
# {I.S : Pengguna memasukan Tahun dan Bulan
# {F.S : Program menampilkan bulan dan Tahun}

bulan = int(input("Masukan bulan = "))
tahun = int(input("Masukan tahun = "))

def get_tanggal_terakhir(t,m):
    if(0 < bulan <= 12) :
        if(bulan in [1,3,5,7,8,10,12]) :
            TanggalBoke = 31


        elif (bulan in [4,6,9,11]) :
            TanggalBoke = 30


        elif (bulan == 2) :
            if ((tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)):
                TanggalBoke = 29

            else:
                TanggalBoke = 28

        return TanggalBoke

    else :
        print("Bulan",bulan, ' / ', tahun, ' bukan tanggal valid')

get_tanggal_terakhir(tahun,bulan)
print("tanggal Akhir Bulan", bulan, ',Tahun', tahun, 'Adalah', get_tanggal_terakhir(tahun,bulan))