# looping dictionary

from re import L


teman_teman = {
    "indi":"Indi Bagus Prasetyo",
    "asep":"Asep Rozali",
    "indra":"Indra Bagus Senjaya",
    "agus":"Agustinus",
    "alfan":"Alfan Nasrullah"
}

#looping first try ( yang keluar adalah key)
for teman in teman_teman:
    print(teman)

# operator untuk mengambil item / iterables
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))

values = teman_teman.values()
print(values)

for value in teman_teman.values():
    print(value)

items = teman_teman.items()
print(items)

for item in teman_teman.items():
    print(item)

for key,value in teman_teman.items():
    print(f"key = {key}, value = {value}")