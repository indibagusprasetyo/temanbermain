#latihan konversi satuan temperatur (suhu)

#program konversi celcius ke satuan (S.I / S.U) yang lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Masukan suhu dalam celcius : '))
print("Suhu adalah",celcius, "C")


# Reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah ", reamur, "Reamur")

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah ", fahrenheit, "Fahrenheit")

# Kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah ", kelvin, "Kelvin")

# Rankine
rankine = (celcius + 273.15) * 9/5
print("Suhu dalam rankine adalah", rankine, "Rankine")