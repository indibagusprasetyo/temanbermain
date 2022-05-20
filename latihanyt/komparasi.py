# operasi komparasi

#setiap hasil dari operasi komparasi adalah boolean

# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# besar dari (>)
print("========BESAR DARI========")
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > 2
print(b, '>', 2, '=', hasil)
hasil = b > 1.9
print(b, '>', 1.9, '=', hasil)

# kurang dari (<)
print("========KURANG DARI========")
hasil = a < 3
print(a, '<', 3, '=', hasil)
hasil = b < 3
print(b, '<', 3, '=', hasil)
hasil = b < 2
print(b, '<', 2, '=', hasil)
hasil = b < 5
print(b, '<', 5, '=', hasil)

# lebih kurang dari sama dengan(<=)
#2 == 2 sejajar dan dianggap TRUE
print("========KURANG DARI SAMA DENGAN========")
hasil = a <= 3
print(a, '<=', 3, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = b <= 2
print(b, '<=', 2, '=', hasil)
hasil = b <= 5
print(b, '<=', 5, '=', hasil)

# besar dari sama dengan(>)
#2 == 2 sejajar dan dianggap TRUE
print("========BESAR DARI SAMA DENGAN========")
hasil = a >= 3
print(a, '>=', 3, '=', hasil)
hasil = b >= 3
print(b, '>=', 3, '=', hasil)
hasil = b >= 2
print(b, '>=', 2, '=', hasil)
hasil = b >= 1.9
print(b, '>=', 1.9, '=', hasil)

#is dan is not
#a == (4) adalah literal

#is membandingkan abjad komparasi object identity
print('==========Object Identity (is)==========')
x = 4 #ini adalah assignment make object
y = 4
print('nilai x = ',x,hex(id(x)))
print('nilai y = ',y,hex(id(y)))
hasil = x is not y
print('x is y = ',hasil)

x = 4 #ini adalah assignment make object
y = 5
print('nilai x = ',x,hex(id(x)))
print('nilai y = ',y,hex(id(y)))
hasil = x is not y
print('x is y = ',hasil)


print('==========Object Identity (is not)==========')
x = 7 #ini adalah assignment make object
y = 7
print('nilai x = ',x,hex(id(x)))
print('nilai y = ',y,hex(id(y)))
hasil = x is not y
print('x is y = ',hasil)

x = 7 #ini adalah assignment make object
y = 8
print('nilai x = ',x,hex(id(x)))
print('nilai y = ',y,hex(id(y)))
hasil = x is not y
print('x is y = ',hasil)