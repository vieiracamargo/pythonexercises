
weight = float(input("Digite o seu peso: "))
hight = float(input("Digite sua altura: "))
imc = weight / (hight * hight)

if imc < 18.5:
    print(f"Seu IMC é: {imc:.2f}")
    print("Abaixo do peso!")
elif imc < 25:
    print(f"Seu IMC é: {imc:.2f}")
    print("Peso ideal")
elif imc < 30:
    print(f"Seu IMC é: {imc:.2f}")
    print("Sobrepeso")
elif imc <= 40:
    print(f"Seu IMC é: {imc:.2f}")
    print("Obesidade")
else:
    print(f"Seu IMC é: {imc:.2f}")
    print("Obesidade mórbida")