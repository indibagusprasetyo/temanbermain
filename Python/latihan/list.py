# LIST

# kumpulan data numbers
data_angka = [1,2,3]
print(data_angka)

# kumpulan data string
data_string = ["asep", "asro", "uro", "kuproy"]
print(data_string)

# kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# kumpulan data campuran
data_campuran = [1,"bala-bala",2,"cireng",3,"Balahu","didit",True,"Agung",False]
print(data_campuran)

# alternatif membuat list
data_range = range(0,10,2) #range (start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

#membuat list dengan for loop, list comprehension
list_ufor = [i for i in range(0,10)]
print(list_ufor)

#membuat list menggunakan for dan if
list_ufor_if = [i for i in range(0,10) if i != 5]
print(list_ufor_if)

list_ufor_if = [i for i in range(0,10) if i % 2 == 0]
print(list_ufor_if)

list_ufor_if = [i for i in range(0,10) if i % 2 != 0]
print(list_ufor_if)