age1 = 39
age2 = 30
age3 = 27

print(age1)
print(age2)
print(age3)

ages = [39, 30, 27, 18]  # list

if 18 in ages:
    ages.remove(18)

print(ages)
ages.append(19)
ages.insert(1, 20)

# "array"
ages_in_next_year = []
for age in ages:
    ages_in_next_year.append(age + 1)
print(ages_in_next_year)

# same ^
ages_in_next_year = [(age + 1) for age in ages]
print(ages_in_next_year)

# with validation
ages_in_next_year = [(age + 1) for age in ages if age > 21]
print(ages_in_next_year)


# validation simplified
def next_year(next_ages):
    return next_ages + 1


ages_in_next_year = [next_year(age) for age in ages if age > 21]
print(ages_in_next_year)


def visualization_process(lista=None):
    if lista is None:
        lista = list()
    print(len(lista))
    print(lista)
    lista.append(13)
