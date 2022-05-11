"""
Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira e mostre quantos Dólares ela pode comprar.

Considere U$$ 1.00 = R$ 5.12
"""

reais = float(input("Quanto dinheiro você tem na carteira?"))
dolar = 5.12
conversion = reais / dolar

print(f"Você pode comprar {conversion:.2f} dolares")