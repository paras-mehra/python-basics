# name = "Paras"
# number = "11"
# print(name)
# print(number)

# print(name[0:3]) # 3 is Exclusive
# print(name[1:4]) # 3 is Exclusive

# <======= Strings Method ======>
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.count("a"))
# print(name.isalnum())

a1 = "Paras"
a2 = 'Paras'
a3 = '''Paras Mehra is a Good Boy
He can play Guitar 
& He is Dance Teacher Too.''' # use tripple quotes for multiline strings
print(a1,a2,a3)

a1[0] = "k" # Strings are immutable and hence this line throws an error 
print(a1)