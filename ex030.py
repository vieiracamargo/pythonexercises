

speed = int(input("Digite a velocidade do carro: "))
speed_limit = 80
ticket_value = (speed - speed_limit) * 7

if speed > speed_limit:
    print("Você ultrapassou o limite permitido!")
    print(f"Multado! O valor da multa é  R$ {ticket_value:.2f}")
