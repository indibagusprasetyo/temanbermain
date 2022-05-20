#Latihan

#Kalkulator Sederhana
print(20*"=")
print("KALKULATOR SEDERHANA")
print(20*"=" + "\n")

angka1 = float(input("masukan angka pertama = "))
operator = input("operator (+, -, x, /) = ")
angka2 = float(input("masukan angka kedua = "))

#percabangan
if operator == "+":
    hasil = angka1 + angka2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka1- angka2
    print(f"hasilnya adalah {hasil}")
elif operator == "x":
    hasil = angka1 * angka2
    print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka1 / angka2
    print(f"hasilnya adalah {hasil}")
else:
    print("Anda salah dalam memasukan Operator")

print("Akhir dari Kalkulator")