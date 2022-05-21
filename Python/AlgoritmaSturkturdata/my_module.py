#pendefinisian objek
pi = 22/7

#pendefinisian function
def luasLingkaran(radius):
    return pi * radius ** 2

def kelilingLingkaran(radius):
    return 2 * pi * radius

def kabisat(tahun):
    return (tahun % 100 == 0) and (tahun % 400 == 0) or (tahun % 100 !=0) and (tahun % 4 == 0)