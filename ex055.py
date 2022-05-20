import datetime

current_year = datetime.datetime.now().year
under_eighteen = 0
over_eighteen = 0

for i in range(0, 7):
    birth_year_str = input("Digite o seu ano de nascimento: ").replace(" ", "")
    if birth_year_str == "":
        print("O campo está vazio! Digite um valor válido!")
        break
    elif not birth_year_str.isnumeric():
        print("Erro! Digite apenas números!")
        break
    else:
        birth_year_int = int(birth_year_str)
        age = current_year - birth_year_int

        if age < 18:
            under_eighteen += 1
        else:
            over_eighteen += 1

if under_eighteen or over_eighteen > 0:
    print(f"Total de pessoas menores de 18 anos: {under_eighteen}")
    print(f"Total de pessoas maiores de 18 anos: {over_eighteen}")