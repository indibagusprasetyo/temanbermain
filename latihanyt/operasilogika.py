#operasilogika atau boolean

#not, or, and, xor

#NOT
print('=====NOT=====')
a = True
c = not a
print('data boolean =',a)
print('----------- NOT -----------')
print('data c =',c)

print('=====NOT=====')
a = False
c = not a
print('data boolean =',a)
print('----------- NOT -----------')
print('data c =',c)



#OR (seperti sistem penjumlahan, jika salah satu true, maka akan true)
print('=====OR=====')
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)

#Value
a = False
b = True
c = a or b
print(a,'OR',b,'=',c)

#Value
a = True
b = False
c = a or b
print(a,'OR',b,'=',c)

#Value
a = True
b = True
c = a or b
print(a,'OR',b,'=',c)

#AND (seperti sistem perkalian x, jika dua buah nilai true, maka akan true)
print('=====AND=====')
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)

#Value
a = False
b = True
c = a and b
print(a,'AND',b,'=',c)

#Value
a = True
b = False
c = a and b
print(a,'AND',b,'=',c)

#Value
a = True
b = True
c = a and b
print(a,'AND',b,'=',c)



#XOR (akan true jika salah satu true)
print('=====XOR=====')
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

#Value
a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)

#Value
a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

#Value
a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)