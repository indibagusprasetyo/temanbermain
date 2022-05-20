#membuat gabungan area rentang dari sebuah angka

# ++++++3---------------10++++++
# + adalah nilai TRUE, - adalah nilai FALSE
inputUser = float(input("Masukan angka yang bernilai\nkurang dari 3\natau \nlebih dari 10\n:"))

# ++++++3---------------
# Memeriksa angka kurang dari 3
isKurangdari = (inputUser < 3)
print("Kurang dari 3 = ", isKurangdari)

# ---------------10++++++
# Memeriksa angka lebih dari 10
isLebihdari = (inputUser > 10)
print("Lebih dari 10 = ", isLebihdari)


isCorrect = isKurangdari or isLebihdari
print("Angka yang anda masukan : ", isCorrect)

print("\n",15*"=","\n")

 # -----3+++++++++++++++10----- (irisan)
 # + adalah nilai TRUE, - adalah nilai FALSE

inputUser = float(input("Masukan angka yang bernilai\nlebih dari 3\ndan \nkurang dari 10\n:"))

 # ------3+++++++++++++++
# Memeriksa angka lebih dari 3
isLebihdari = (inputUser > 3)
print("Lebih dari 3 = ", isLebihdari)

# +++++++++++++++10------
# Memeriksa angka lebih dari 10
isKurangdari = (inputUser < 10)
print("Kurang dari 10 = ", isKurangdari)


isCorrect = isLebihdari and isKurangdari
print("Angka yang anda masukan : ", isCorrect)