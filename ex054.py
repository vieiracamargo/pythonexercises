
phrase = input("Digite uma frase: ").upper().strip().replace(" ", "")
phrase2 = ""

for i in range(len(phrase)-1, 0-1, -1):
    phrase2 += phrase[i]

print(phrase)
print(phrase2)

if phrase == phrase2:
    print("A frase é um PALINDROMO")
else:
    print("A frase NÃO é um PALINDROMO")