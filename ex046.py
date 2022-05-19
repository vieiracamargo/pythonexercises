import random
import time

print("Olá! Eu sou o jogo de Jokenpoo! Que tal uma partida?")
user_choice =input("Escolha entre pedra, papel ou tesoura: ").upper().strip()

jokenpoo = ["PEDRA", "PAPEL", "TESOURA"]
ai_choice = random.choice(jokenpoo)

print("Calculando minha jogada...")
time.sleep(1)


if user_choice == "TESOURA":
    if ai_choice =="PAPEL":
        print(f"Você ganhou! {user_choice} corta {ai_choice}!")
    elif ai_choice =="PEDRA":
        print(f"Você perdeu! {ai_choice} quebra a  {user_choice}!")
    else:
        print("Empate! Tente novamente!")

if user_choice == "PAPEL":
    if ai_choice == "TESOURA":
        print(f"Você perdeu! {ai_choice} corta {user_choice}!")
    elif ai_choice == "PEDRA":
        print(f"Você ganhou! {user_choice} embrulha a {ai_choice}!")
    else:
        print("Empate! Tente novamente!")

if user_choice == "PEDRA":
    if ai_choice == "TESOURA":
        print(f"Você ganhou! {user_choice} amassa a  {ai_choice}!")
    elif ai_choice == "PAPEL":
        print(f"Você perdeu! {ai_choice} embrulha a {user_choice}!")
    else:
        print("Empate! Tente novamente!")
