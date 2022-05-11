"""
Escreva um programa que leia um valor em metros e o exiba convertido
em centímetros e milimetros.
"""

meters = float(input("Digite um valor em metros que deseja converter: "))

centimeters = meters * 100
millimeters = meters * 1000

print(f"{meters:.2f} metro(s) é igual a {centimeters:.2f} centimetros")
print(f"{meters:.2f} metro(s) é igaul a {millimeters:.2f} milimetros")