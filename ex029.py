import random

guess = int(input("Chute um número: "))
luck_number = random.randint(0, 5)

if guess == luck_number:
    print("Você acertou!")
else:
    print("Você errou! O computador venceu")