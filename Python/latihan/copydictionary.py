# copy dictionary

teman_teman = {
    "indi":"Indi Bagus Prasetyo",
    "asep":"Asep Rozali",
    "indra":"Indra Bagus Senjaya",
    "agus":"Agustinus",
    "alfan":"Alfan Nasrullah"
}

friends = teman_teman

print(f"teman_teman: {teman_teman}\n")
print(f"friends: {friends}\n")

teman_teman["indi"]="Indi Bagus Pranata"
print(f"teman_teman: {teman_teman}\n")
print(f"friends: {friends}\n")

# ini adalah pop dictionary (berdasarkan key)
dataIndi = friends.pop("indi")
print(f"data indi = {dataIndi}\n")
print(f"friends = {friends}")

# pop items dictionary (hanya yang terakhir)
dataTerakhir = friends.popitem()
print(f"data terakhir = {dataTerakhir}\n")
print(f"friends = {friends}")