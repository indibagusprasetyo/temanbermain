#tipedata: angka satuan (integer)
data_integer = 1

print("data : ", data_integer, ", bertipe : ", type(data_integer))

#tipedata: angka real (float)
data_float = 1.5

print("data : ", data_float, ", bertipe : ", type(data_float))

#tipedata: kumpulan karakter (string)
data_string = "im_on_you"

print("data : ", data_string, ", bertipe : ", type(data_string))

#tipedata: karakter (char)
data_char = "A"

print("data : ", data_char, ", bertipe : ", type(data_char))

#tipedata: logika TRUE/FALSE (boolean)
data_bool = True

print("data : ", data_bool, ", bertipe : ", type(data_bool))

#tipedata khusus
#bilangan kompleks (complex)
data_complex = complex(5,6)

print("data : ", data_complex, ", bertipe : ", type(data_complex))

#tipedata dari bahasa C
from ctypes import c_double, c_char
data_c_double = c_double(10.5)
print("data : ", data_c_double, ", bertipe : ", type(data_c_double))