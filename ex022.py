
name = input("Digite o seu nome completo: ").strip()

name_to_upper = name.upper()
name_to_lower = name.lower()
name_no_space = name.replace(" ", "")
name_split = name.split()
first_name = name_split[0]

print(name_to_upper)
print(name_to_lower)
print(len(name_no_space))
print(len(first_name))


