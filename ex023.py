
number_str = input("Digite um número de 0 até 9999: ")

number_unity = number_str[-1]
number_ten = number_str[-2]
number_hundred = number_str[-3]
number_thousand = number_str[-4]

print(f"Unidade: {number_unity}")
print(f"Dezena: {number_ten }")
print(f"Centena: {number_hundred}")
print(f"Milhar {number_thousand}")