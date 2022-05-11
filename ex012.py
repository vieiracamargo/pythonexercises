"""
Faça um programa que leia a largura e altura de uma parede
em metros, calcule a sua área e a quantidade de tinta necessária
para pintá-la, sabendo que cada litro de tinta, pinta um área de 2m quadrados.
"""

width = float(input("Qual é a largura da parade(metros)?"))
height = float(input("Qual é a altura da parade(metros)??"))
area = width * height

paint = 2
paint_needed = area / 2

print(f"A parede tem {area} metros quadrados, e serão necessários {paint_needed} litros de tinta para pinta-la")