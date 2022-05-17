frase = "Curso em video Python"

print(frase[15:])

print(len(frase))

print(frase.count("v"))

#O ultimo valor é ignorado, ou seja, a contagem  irá até a 12 casa
print(frase.count("o", 0,13))

print(frase[0:2])

print(frase[2:])

#retorna a posição onde começa do termo pesquisado
print(frase.find("deo"))

#quando o valor não existe o valor retornado será -1
print(frase.find("Android"))

#retorna um valor lógico  TRUE ou FALSE
print("Curso" in frase)

#procura uma termo e substiui por outro
print(frase.replace("Python", "Android"))

#coloca todas as letras em maiusculo
print(frase.upper())

#coloca toadas as letras em minusculo
print(frase.lower())

#coloca a primeira letra em maiusc
print(frase.capitalize())

#Capitalize palavra por palavra
print(frase.title())

frase2 ="   Aprenda Python   "
print(frase2)
#Remove os espaços em branco
print(frase2.strip())

#remove os espaços apenas do lado direito
print(frase2.rstrip())

#remove os espaços apenas do lado esquerdo
print(frase2.lstrip())

#divide a string e a coloca em uma nova lista
split = frase.split()
print(split)

#Junta as palavras  que estao em uma lista
join ="-".join(split)
print(join)