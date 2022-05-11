"""
Faça um algoritmo que leia o salário e mostre seu novo salário,
com 15% de aumento.
"""

wage = float(input("Digite seu salário: "))
new_wage = wage + (wage * 0.15)

print(f"O seu novo salário  com o aumento de 15% é: {new_wage:.2f}")