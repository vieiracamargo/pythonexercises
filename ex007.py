"""
Crie um algoritmo que leai um número e mostre o seu dobro,
triplo e raiz quadrada.
"""



number = int(input("Digite um número: "))

double = number * 2
triple = number * 3
square= pow(number, 0.5)

print(f"O dobro de {number} é : {double}")
print(f"O triplo de {number} é: {triple}")
print(f"A raiz quadrada de {number} é :{square}")
