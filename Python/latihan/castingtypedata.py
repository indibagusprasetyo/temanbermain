#Casting = merubah suatu tipe ke tipe lain (data)
#int, float, str, bool


##INTEGER
print("=====Integer=====")
data_int = 9;
print("data = ", data_int, ", tipe = ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)

print("data = ", data_float, ", tipe = ", type(data_float))
print("data = ", data_str, ", tipe = ", type(data_str))
print("data = ", data_bool, ", tipe = ", type(data_bool))


##FLOAT
print("=====Float=====")
data_float = 9.3;
print("data = ", data_float, ", tipe = ", type(data_float))


data_float = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)

print("data = ", data_int, ", tipe = ", type(data_float))
print("data = ", data_str, ", tipe = ", type(data_str))
print("data = ", data_bool, ", tipe = ", type(data_bool))


##BOOLEAN
print("=====Boolean=====")
data_bool = True;
print("data = ", data_bool, ", tipe = ", type(data_bool))


data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)

print("data = ", data_int, ", tipe = ", type(data_float))
print("data = ", data_str, ", tipe = ", type(data_str))
print("data = ", data_float, ", tipe = ", type(data_float))


##STRING
print("=====String=====")
data_str = "1000"; #harus angka jika ingin casting ke int atau float
#bernilai TRUE jika ada nilai , dan sebaliknya
print("data = ", data_str, ", tipe = ", type(data_str))

data_int = int(data_str)
data_float = float(data_str)
data_bool = bool(data_str)

print("data = ", data_int, ", tipe = ", type(data_int))
print("data = ", data_float, ", tipe = ", type(data_float))
print("data = ", data_bool, ", tipe = ", type(data_bool))