value = input("Digite algo: ")
print(f"O Tipo primitivo desse valor é {type(value)}")

#USANDO F- STRIGNS
print(f"Só tem espaços? {value.isspace()}")
print(f"É um número? {value.isnumeric()}")
print(f"É alfabético? {value.isalpha()}")
print(f"É alfanumérico? {value.isalnum()}")
print(f"Está em maiúsculas? {value.isupper()}")
print(f"Está em minusculas? {value.islower()}")
print(f"Está capitalizada? {value.istitle()}")
print()

#USANDO .FORMAT
print("Só tem espaços? {}" .format(value.isspace()))
print("É um número? {}" .format(value.isnumeric()))
print("É alfabético? {}" .format(value.isalpha()))
print("É alfanúmerico? {}" .format(value.isalnum()))
print("Éstá em maiúsculas? {}" .format(value.isupper()))
print("Está em minusculas? {}" .format(value.islower()))
print("Está capitalizada? {}" .format(value.istitle()))