#Program Perhitungan Luas dan Keliling Persegi Panjang
#I.S. :
#F.S. :

P = float(input("Masukan Panjang : "))
L = float(input("Masukan Luas : "))

def LuasPersegiPanjang (P,L) :
    Luas = P * L
    print('Luas Persegi Panjang = {:.2f}'.format(Luas))

def KelilingPersegiPanjang (P,L) :
    Keliling = 2 * (P + L)
    print('Keliling Persegi Panjang = {:.2f}'.format(Keliling))
    return Keliling


LuasPersegiPanjang(P,L)
KelilingPersegiPanjang(P,L)