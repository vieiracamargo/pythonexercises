
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))

if number1 > number2 and number1 > number3:
    print(f"{number1} é o maior número")
elif number2 > number1 and number2 > number3:
    print(f"{number2} é o maior número")
else:
    print(f"{number3} é o maior número")

if number1 < number2 and number1 < number3:
    print(f"{number1} é o menor número")
elif number2 < number1 and number2 < number3:
    print(f"{number2} é o menor número")
else:
    print(f"{number3} é o menor número")
