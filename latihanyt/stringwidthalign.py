#Width and Multiline

#Data
data_nama = "Indi Bagus Prasss"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

#string multiline
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

#string multiline
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

#string multiline (kutip triple)
data_string = f"""
nama = {data_nama} , umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""

print(5*"="+"Data String"+5*"=")
print(data_string)

#mengatur lebar
data_string = f"""
nama    = {data_nama:>}
umur    = {data_umur:>}
tinggi  = {data_tinggi:>}
sepatu  = {data_nomor_sepatu:>}
"""

print(5*"="+"Data String"+5*"=")
print(data_string)
