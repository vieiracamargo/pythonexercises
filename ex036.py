
reta1 = float(input("Digite o valor da primeira reta: "))
reta2 = float(input("Digite o valor da segunda reta: "))
reta3 = float(input("Digite o valor da terceira reta: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print(f"É possivel criar um triângulo")
else:
    print(f"Não é possivel criar um triângulo")