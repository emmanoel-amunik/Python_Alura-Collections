ages = [15, 87, 32, 65, 56, 32, 49, 37]

for index in range(len(ages)):
    print(index, '-', ages[index])


for value in enumerate(ages):  # packed
    print(value)


for index, value in enumerate(ages):  # unpacking
    print(index, "x", value)


users = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]
for name, age, birth in users:  # unpacked
    print(name)


sorted(ages)
list(reversed(ages))
sorted(ages, reverse=True)
list(reversed(sorted(ages)))
ages.sort()
