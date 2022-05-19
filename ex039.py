
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))

if number1 > number2:
    print(f"O primerio valor ({number1}) é maior")
elif number2 > number1:
    print(f"O segundo valor ({number2}) é maior")
else:
    print(f"Não existe valor maior, os dois são iguais")