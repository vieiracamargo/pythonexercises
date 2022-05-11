"""
Faça um algoritmo que leia o preço de um produto e mostre seu
novo preço, com 5% de desconto.
"""

price = float(input("Digite o valor do produto: "))
new_price = price - (price * 0.05)

print(f"O novo preço é : {new_price:.2f}")