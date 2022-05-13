import random

students = []

for i in range(1, 5):
    student = input(f"Digite o nome do {i} aluno: ")
    students.append(student)

choice = random.choice(students)

print(students)

print(choice)