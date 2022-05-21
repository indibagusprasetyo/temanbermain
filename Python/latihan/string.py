### 1. cara membuat string

data = "ini adalah string"
print(data)
print(type(data))

'''
    1. membuat string dengan menggunakan single quote '...'
    2. membuat string dengan menggunakan double quote "..."
'''

data = 'ini adalah menggunakan single quote'
print(data)

data = "ini menggunakan double quote / kutip"
print(data)
print('"Halo, apa kabar"') #kutip dua didalam
print("'Halo, apa kabar'") #kutip satu didalam
print("Ini adalah hari jum'at")

### 2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, ins\'t it?')

# backslash
print("C:\\user\\bagus")

# tab
print("bagus\tprasss, gokil")
print("bagus\t\t\t\t\tprasss, gokil euy")

# backspace
print("lebar \bterakhir,jadi so close")

# newline
print("baris pertama,\nbaris kedua") #LF - Line Feed = macOS, linux, Unix.
print("baris pertama,\rbaris kedua") #CR - Carriage Return = commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua") #CRLF - Line Feed Carriage Return = dipakai di Windows


### 3. Sting Literal atau Raw

#hati-hati
print('C:\new folder')

#menggunakan raw string
print(r'C:\new folder') #menghilangkan funcsting

#multiline litteral string
print("""
Nama : Indi
Kelas : IF-9K/S1/SMS1
""")

#multiline literal string dan raw
print(r"""
Nama : Bagus
Kelas : IF-9K/S1/SMS5
Website : bagusxpro.id\tescomp
""")