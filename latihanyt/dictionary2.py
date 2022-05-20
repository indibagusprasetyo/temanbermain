# operator untuk dictionary

data_dict = {
    'ind':'indonesia',
    'ger':'germany',
    'sgr':'singapore',
    'dnk':'denmark'
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary : {LENDICT}")

#mengecek key exist atau tidak
KEY = 'ind'
CHEKCKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict : {CHEKCKEY}")

#mengakses value (read) dengan get
print(data_dict['ind'])
print(data_dict.get("ind"))
print(data_dict.get("isd","KEY TIDAK DITEMUKAN")) # cek key dengan message

# mengupdate data
data_dict["ind"] = "Indonesian Republic"
print(data_dict)
data_dict["sgr"] = "singaporean Food"
print(data_dict)

data_dict.update({"ind":"Indonesian"})
print(data_dict)
data_dict.update({"jwd":"Jeweled"})
print(data_dict)

#menghapus data
del data_dict["jwd"]
print(data_dict)