import random as rd
import bubble_module as bm

students = []

for i in range(20):
    students.append(rd.randint(170,185))

print(students)

sortedStudents = bm.bubbleSort(students, deepCopy=False)

print(students)
print(sortedStudents)