
travel_distance = float(input("Qual é a distância da sua viagem em km?: "))
price_index = 200
price_under_200 = 0.50
price_above_200 = 0.45

if travel_distance <= price_index:
    price = travel_distance * price_under_200
    print(f"O valor da passagem é R$ {price}")
else:
    price = travel_distance * price_above_200
    print(f"O valor da passagem é R$ {price}")
    