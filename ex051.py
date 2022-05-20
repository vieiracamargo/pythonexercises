
even_sum = 0

for i in range(1, 7):
    number = int(input(f"Digite o {i} número inteiro: "))
    if number % 2 == 0:
        even_sum += number

print(f"A soma dos números pares é: {even_sum}")