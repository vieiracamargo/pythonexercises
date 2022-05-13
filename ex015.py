import math

cateto_oposto = float(input("Digite o comprimento do cateto opoosto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = math.hypot(cateto_adjacente, cateto_oposto)

print(f"O comprimento da hipotenusa é: {hipotenusa}")