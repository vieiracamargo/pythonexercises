
number = int(input("Digite um número: "))
print("""Escolha qual sera a base de conversão:
1 - Binário
2 - Octal
3 - Hexadecimal
""")

options = int(input("Sua opção: "))

if options == 1:
    binary = bin(number)
    print(f"O número {number} convertido para binário é: {binary}")
elif options == 2:
    octal = oct(number)
    print(f"O número {number} convertido para octal é: {octal}")
elif options == 3:
    hexadecimal = hex(number)
    print(f"O número {number} convertido para hexadecimal é: {hexadecimal}")
else:
    print("Valor Inválido! \n"
          "Digite um valor disponível!")