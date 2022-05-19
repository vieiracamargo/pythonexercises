

house = float(input("Qual é o valor da casa?"))
wage = float(input("Qual é o seu salário? "))
time = int(input("Em quantos anos você irá realizar o pagamento?"))
time_in_months = time * 12
installment_limit = wage * 30/100
installment_value = house / time_in_months

if installment_value <= installment_limit:
    print(f"Parabéns! Empréstimo concedido!")
else:
    print(f"Empréstimo Negado!")

print(f"Valor da parcela : {installment_value}")
print(f"Tempo: {time_in_months} meses")