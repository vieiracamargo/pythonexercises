
grade1 = float(input("Digite a primeira nota: "))
grade2 = float(input("Digite a segunda nota: "))
average = (grade1 + grade2) / 2
cut_off_score = 5
if average < cut_off_score:
    print(f"REPROVADO! Sua média foi: {average:.2f}")
elif average <= 6.9:
    print(f"RECUPERAÇÃO! Sua média foi: {average:.2f}")
else:
    print(f"APROVADO! Sua média foi: {average:.2f}")