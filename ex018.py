import random

students = []

for i in range(1, 5):
    student = input(f"Digite o nome do {i} aluno: ")
    students.append(student)

print(students)

random.shuffle(students)

print(students)