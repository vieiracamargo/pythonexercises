
phrase = input("Digite uma frase: ").lower().strip()

print(f"A letra A aparece um total de : {phrase.count('a')} vezes")
print(f"A letra A aparece  pela primeira vez na posição: {phrase.find('a')}")
print(f"A letra A aparece pela ultima vez na posição: {phrase.rfind('a')}")