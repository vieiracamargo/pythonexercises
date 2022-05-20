import time

print("Processando", end=" ")
for i in range(0, 3):
    print(".", end="")
    time.sleep(1)

print()

odd_sum = 0
for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        odd_sum += i
print(f"A soma dos números impares no intervalo de 1 a 500 é: \033[1:32m{odd_sum}")
