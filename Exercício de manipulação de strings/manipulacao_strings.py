string = "LABORATORIO"

print(string.lower())
print(string.capitalize())
print(list(string.capitalize()))
print(tuple(string.capitalize()))

mini_count = {}

for caracter in string.capitalize():
    if caracter in mini_count:
        mini_count[caracter] += 1
    else:
        mini_count[caracter] = 1
    print(mini_count)
