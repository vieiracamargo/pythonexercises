
year = int(input("Digite um ano: "))

if year % 4 == 0 and year % 100 != 0:
    print(f"O ano {year} é bissexto")
elif year % 400 != 0:
    print(f"O ano {year} não é bissexto")
else:
    print(f"O ano {year} é bissexto")