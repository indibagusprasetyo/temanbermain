x = float(input("X : "))
y = float(input("Y : "))
print(f"koordinat ({x}.{y}) berada di ", end="")

if(x > 0) and (y > 0):
    print("Kuadran I")
elif(x < 0) and (y > 0):
    print("Kuadran II")
elif(x < 0) and (x < y):
    print("Kuadran III")
elif(x > 0) and (y < 0):
    print("Kuadran IV")
elif(x == 0) and (y == 0):
    print("Titik Pusat")
elif(x == 0) and (y != 0):
    print("Sumbu X")
elif(x != 0) and (y == 0):
    print("Sumbu Y")

