# KM Programs
# https://km-programs.pl/

# Dictionary merge and update

# Sposob 1
d1 = {'name': 'JOHN', 'surname': 'BLACK', 'age': 30}
d2 = {'name': 'ANDY', 'gender': 'male'}

print('--------------------------------- 1 ----------------------------------------')
d31 = {**d1, **d2}
print(d31)  # {'name': 'ANDY', 'surname': 'BLACK', 'age': 30, 'gender': 'male'}

print('--------------------------------- 2 ----------------------------------------')
d1_copy = d1.copy()
d1_copy.update(d2)
print(d1_copy)  # {'name': 'ANDY', 'surname': 'BLACK', 'age': 30, 'gender': 'male'}

print('--------------------------------- 3 ----------------------------------------')
d4 = dict(d1, **d2)  # dziala jezeli w d2 kluczami sa tylko i wylacznie napisy
print(d4)


# Sposob 2

d11 = {'name': 'JOHN', 'surname': 'BLACK', 'age': 30}
d22 = {'name': 'ANDY', 'gender': 'male'}

print('--------------------------------- 4 ----------------------------------------')
d32 = d11 | d22
print(d32)  # {'name': 'ANDY', 'surname': 'BLACK', 'age': 30, 'gender': 'male'}

print('--------------------------------- 5 ----------------------------------------')
d11 |= d22
print(d11)  # {'name': 'ANDY', 'surname': 'BLACK', 'age': 30, 'gender': 'male'}
