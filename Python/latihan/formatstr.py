#format string

#contoh generic

from typing import BinaryIO


nama = "gaga"
format_str = f"hello {nama}" 

print(format_str)

#boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

#angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

#bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

#bilangan ribuan
angka = 2000
format_str = f"ribuan = {angka:,}"
print(format_str)

#bilangan desimal
angka = 2005.523231
format_str = f"desimal = {angka:.4f}"
print(format_str)

#menampilkan leading zero
angka = 2005.52422
format_str = f"desimal = {angka:9.3f}"
print(format_str)

#menampilkan tanda +-
angka_minus = -10
angka_plus = 10
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+d}"
print(format_minus)
print(format_plus)

#memformat persen
persen = 0.045
format_persen = f"persen = {persen:.1%}"
print(format_persen)

#melakukan operasi aritmatika didalam placeholder
harga = 10000
jumlah = 5
format_str = f"harga total = Rp.{harga * jumlah}"
print(format_str)

#format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hexadecimal = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)
