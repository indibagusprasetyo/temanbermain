# operasi yang dapat dilakukan dengan penyingkatan
#operasi ditambah assignment

#operator aritmatika (Penjumlahan, Pengurangan, Perkalian, dan Pembagian)
a = 5 # adalah assigment 
print('nilai a =', a)

a += 1 # artinya adalah a = a + 1
print('nilai += 1, nilai a menjadi',a)

a -= 2 # artinya adalah a = a - 1
print('nilai -= 1, nilai a menjadi',a)

a *= 5 # artinya adalah a = a * 1
print('nilai *= 1, nilai a menjadi',a)

a /= 2 # artinya adalah a = a / 2
print('nilai /= 1, nilai a menjadi',a)

b = 10 # adalah assignment
print('\nnilai b =',b)

b %= 3
print("nilai b %= 3, nilai b menjadi",b)

b = 10 # adalah assignment
print('\nnilai b =',b)

b //= 3
print("nilai b //= 3, nilai b menjadi",b)

#Eksponen atau Pangkat
a = 5
print('nilai a =', a)
a **= 3
print("nilai b **= 3, nilai b menjadi",a)

print("\n")

#operator bitwise
#OR
c = True
print("\nnilai c =",c)
c |= False
print("nilai c |= False, nilai  c menjadi", c)
c  = False
print("\nnilai c=", c)
c |= False
print("nilai c |= False, nilai  c menjadi", c)
c  = False

#AND
c = True
print("\nnilai c =",c)
c &= False
print("nilai c &= False, nilai  c menjadi", c)
c  = True
print("\nnilai c=", c)
c &= True
print("nilai c &= True, nilai c menjadi", c)

#XOR
c = True
print("\nnilai c =",c)
c ^= False
print("nilai c ^= False, nilai  c menjadi", c)
c  = True
print("\nnilai c=", c)
c ^= True
print("nilai c ^= True, nilai c menjadi", c)

#Shift (RIGHT and LEFT)
d = 0b0100
print("\nnilai d=",format(d,'04b'))
d >>= 2
print("nilai d >>= 2, nilai d menjadi",format(d,'04b'))
d <<= 2
print("nilai d <<= 1, nilai d menjadi",format(d,'04b'))