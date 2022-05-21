#program list buku


list_buku = []
while True:
    print("\nMasukan Data Buku")

    judul = input("Masukan judul buku\t : ")
    penulis = input("Masukan Nama penulis\t : ")

    buku_baru = [judul,penulis]
    print(buku_baru)
    list_buku.append(buku_baru)

    print("\n\n","="*10,"Data Buku","="*10)
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")

    print("\n\n","="*20)
    isLanjut = input("Apakah DiLanjutkan? (Y/N) : ")

    if isLanjut == "N":
        break

print("BOOKS PROGRAM HAS BEEN SHUTING DOWN")