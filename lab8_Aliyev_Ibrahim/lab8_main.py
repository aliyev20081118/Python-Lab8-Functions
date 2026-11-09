# lab8_main.py

# Tapşırıq 7
import utils
from utils import average
from utils import build_username as make_user
import utils as u

# Tapşırıq 1
print(" Tapşırıq 1")
def print_student_card(name, group, year):
    print("Name:", name)
    print("Group:", group)
    print("Year:", year)

print_student_card("Aysel Mammadova", "CE-101", 1)
print_student_card(year=2, name="Kamran Aliyev", group="CE-201")
# print_student_card("Həsən Həsənov", "CE-301") # Qəsdən xəta (şərhdə)

# Tapşırıq 7 2-ci versiya ( yoxlama)
print("\n Tapşırıq 7 yoxlama")
print(utils.add_vat(200))
print(average(60, 70))
print(make_user("Nigar", "Hasanova"))
print(u.with_bonus([50, 95], 10))

print("\n Tapşırıq 5 ")
scores = [70, 95, 88, 100]
print(u.with_bonus(scores, 10))
print(scores)
u.add_bonus(scores[:], 10)
print(scores)
u.add_bonus(scores, 10)
print(scores)

print("\n Tapşırıq 6 ")
print(average(70, 80, 90))
print(average(100))
print(average())
print(utils.make_course("CE101", title="Fundamentals of Programming", credits=6))

# Tapşırıq 4
print("\n Tapşırıq 4 ")
def make_student(name, score, group=""):
    student_dict = {"name": name, "score": score}
    if group:
        student_dict["group"] = group
    return student_dict

print(make_student("Kamran", 61, "CE-101"))

students = []
while True:
    entered_name = input("Name (quit to stop): ")
    if entered_name == 'quit':
        break
    entered_score = int(input("Score: "))
    new_student = make_student(entered_name, entered_score)
    students.append(new_student)

for student in students:
    print(student['name'] + ": " + str(student['score']))

# Tapşırıq 7 2-ci versiya ( yoxlama)
print("\n Tapşırıq 7 yoxlama")
print(utils.add_vat(200))
print(average(60, 70))
print(make_user("Nigar", "Hasanova"))
print(u.with_bonus([50, 95], 10))

print("\n Tapşırıq 5 ")
scores = [70, 95, 88, 100]
print(u.with_bonus(scores, 10))
print(scores)
u.add_bonus(scores[:], 10)
print(scores)
u.add_bonus(scores, 10)
print(scores)

print("\n Tapşırıq 6 ")
print(average(70, 80, 90))
print(average(100))
print(average())
print(utils.make_course("CE101", title="Fundamentals of Programming", credits=6))
