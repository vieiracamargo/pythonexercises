
wage = float(input("Digite o seu salário: "))
wage_increase_index = 1250

if wage <= wage_increase_index:
    new_wage = wage + wage * (15/100)
    print(f"O seu novo salário é: R$ {new_wage:.2f}")
else:
    new_wage = wage + wage * (10/100)
    print(f"O seu novo salário é: R$ {new_wage:.2f}")

