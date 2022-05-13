import math

angle = float(input("Digite um angulo: "))
seno = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))
tan = math.tan(math.radians(angle))

print(f"O cosseno do angulo é: {cos:.2f}")
print(f"O seno do angulo é: {seno:.2f}")
print(f"A tangente do angulo é: {tan:.2f}")

