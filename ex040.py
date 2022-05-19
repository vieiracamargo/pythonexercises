import datetime

today_datetime = datetime.datetime.now()
current_year = today_datetime.year
birth_year = int(input("Digite o ano do seu nascimento: "))
age = current_year - birth_year

if age < 18:
    print(f"Você tem {age}  anos, e deverá se alistar em breve")
elif age == 18:
    print(f"Você tem {age}  anos, está na hora de você se alistar!")
else:
    print(f"Você tem {age}  anos, o tempo para o seu alistamento já se esgotou!")

