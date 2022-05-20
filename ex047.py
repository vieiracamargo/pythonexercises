import time

print("Iniciando contagem regressiva para os fogos de artifícios")
print("Carregando", end=" ")

for i in range(0, 3):
    print(".", end="")
    time.sleep(1)

print()

for i in range(10, -1, -1):
    if i >= 7:
        print(f"\033[1:32m...{i}")
        time.sleep(1)
    elif i >= 3:
        print(f"\033[1:33m...{i}")
        time.sleep(1)
    else:
        print(f"\033[1:31m...{i}")
        time.sleep(1)

print("\U0001F386" * 10)