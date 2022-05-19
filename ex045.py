
value = float(input("Digite o valor do produto: "))
print("""Escolha a condição de pagamento: 
1 - Á vista(dinheiro) ou cheque: 10% de desconto
2 - Á vista no cartão: 5% de desconto
3 - Em até 2x no cartão: preço normal
4 - 3x ou mais no cartão: 20% de juros: \n""")
options = int(input("Qual é a opçao: "))

if options == 1:
    new_value = value - (value * 10/100)
elif options == 2:
    new_value = value - (value * 5/100)
elif options == 3:
    new_value = value
elif options == 4:
    new_value = value + (value * 20/100)
else:
    print("Digite valores válidos!")

print(f"O valor do produto é: {new_value:.2f}")