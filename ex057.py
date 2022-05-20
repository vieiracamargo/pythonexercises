
total_ages = 0
older_man_age = 0
older_man_name = ""
under_twenty_women = 0

for i in range(0, 4):
    name = input("Digite seu nome: ")
    age = int(input("Digite sua idade: "))
    print("""Qual é o seu sexo ?
    1 - Masculino
    2 - Feminino   """)
    gender = int(input("Esolha sua opção: "))

    if gender == 1:
        if age > older_man_age:
            older_man_age = age
            older_man_name = name

    elif gender == 2:
        if age < 20:
            under_twenty_women += 1

    total_ages += age

age_average = total_ages / 4
print(f"A média de idade é: {age_average:.2f}")
print(f"A quantidade de mulheres abaixo de 20 anos é: {under_twenty_women}")
if older_man_age > 0:
    print(f"{older_man_name} tem {older_man_age} anos, e é o homem mais velho.")




