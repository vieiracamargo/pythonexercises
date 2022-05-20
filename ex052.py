
first_number = int(input("Digite o primeiro termo: "))
ratio = int(input("Digite a razão: "))
tenth = first_number + (10-1) * ratio
for i in range(first_number, tenth+ratio, ratio):
    print(i)
