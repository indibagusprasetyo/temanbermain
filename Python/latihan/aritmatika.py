# operasi aritmatika

n = 10
x = 2

# operasi tambah (+)
hasil = n + x
print(n,'+',x,'=',hasil)


# operasi kurang (-)
hasil2 = n - x
print(n,'-',x,'=',hasil2)

# operasi perkalian (*)
hasil3 = n * x
print(n,'.',x,'=',hasil3)

# operasi pembagian (/)
hasil4 = n / x
print(n,'/',x,'=',hasil4)

# operasi eksponen (^) / pangkat
hasil5 = n ** x
print(n,'^',x,'=',hasil5)

# operasi modulous (mod), ESYD (%)
hasil6 = n % x
print(n,'%',x,'=',hasil6)

# operasi floor division (div), ESYD (//)
hasil = n // x
print(n,'//',x,'=',hasil)


#prioritas operasi, operational precendence

x = 3
y = 2
z = 4

hasil = x + y - z % x ** y
print(x, '+', y, '-', z, '%', x, '^', y, "hasil = ", hasil)

#diprioritaskan yang () dalam kurung (IMPORTAN!!!)
#lalu, pangkat/eksponen (^ / **)
#lalu, perkalian (*), pembagian (/), permodulous (%), perfloordiv (//)
#lalu, penjumlahan (+) dan pengurangan (-)