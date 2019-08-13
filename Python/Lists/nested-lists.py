#Problem: Given the names and grades for each student in a Physics class of  students, #store them in a nested list and print the name(s) of any student(s) having the second #lowest grade.

#URL Link: https://www.hackerrank.com/challenges/nested-list/problem

students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    student = []
    student.append(name)
    student.append(score)
    students.append(student)
scores = sorted(set([student[1] for student in students])) #filter out duplicates
second_lowest_score = scores[1] #get the second highest score
#List comprehension with the predicate second highest score
second_lowest_students = sorted([student for student in students if student[1] == second_lowest_score])
result = [student[0] for student in second_lowest_students]
print(*result, sep='\n')
