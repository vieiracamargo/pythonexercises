reta1 = float(input("Digite o valor da primeira reta: "))
reta2 = float(input("Digite o valor da segunda reta: "))
reta3 = float(input("Digite o valor da terceira reta: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("É possivel criar um triângulo")

    if reta1 != reta2 != reta3 != reta1:
        print(f"O triângulo é ESCALENO!")
    elif reta1 == reta2 == reta3:
        print(f"O triângulo é EQUILÁTERO")
    else:
        print(f"O triângulo é ISÓCELES")
else:
    print("Não é possível criar um triângulo")

