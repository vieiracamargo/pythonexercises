
heavier_weight = 0
light_weight = 0

for i in range(0, 5):
    weight = input("Digite seu peso (KG): ").replace(" ", "").replace(",", ".")
    weight_clear = weight.replace(".", "")

    if weight_clear == "":
        print("O campo está vazio! Digite um valor válido!")
        break
    elif not weight_clear.isnumeric():
        print("Erro! Digite apenas números!")
        break
    else:
        float_weight = float(weight)

    if i == 0:
        heavier_weight = float_weight
        light_weight = float_weight
    else:
        if float_weight > heavier_weight:
            heavier_weight = float_weight

        if float_weight < light_weight:
            light_weight = float_weight


print(heavier_weight)
print(light_weight)