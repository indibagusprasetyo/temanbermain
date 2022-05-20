def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else :
        return n * faktorial(n -1)

nilai = int(input("Masukan Nilai : "))
for i in range (nilai):
    print(i);
print("Faktorial dari : ", nilai, "adalah : ", faktorial(nilai))

