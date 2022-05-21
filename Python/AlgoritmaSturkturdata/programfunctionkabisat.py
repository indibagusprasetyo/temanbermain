# Program Kabisat
# {I.S : Pengguna memasukan sebuah Tahun}
# {F.S : Program menampilkan hasil tahun}

tahun = int(input("Masukan Tahun = "))
def kabisat(thun):
    if (tahun % 4 == 0) and (tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

result = kabisat(tahun)
print ("Tahun ",tahun,",Tahun Kabisat" if result else ",Bukan Kabisat")