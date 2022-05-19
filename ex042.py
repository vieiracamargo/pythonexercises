import datetime

today = datetime.datetime.now()
current_year = today.year
birth_year = int(input("Qual é o ano do seu nascimento?"))
age = current_year - birth_year

if age <= 9:
    print(f"Você tem {age} anos e pertence a categoria MIRIM")
elif age <= 14:
    print(f"Você tem {age} anos e pertence a categoria INFANTIL")
elif age <= 19:
    print(f"Você tem {age} anos e pertence a categoria JUNIOR")
elif age <= 25:
    print(f"Você tem {age} anos e pertence a categoria SÊNIOR")
else:
    print(f"Você tem {age} anos e pertence a categoria MASTER")