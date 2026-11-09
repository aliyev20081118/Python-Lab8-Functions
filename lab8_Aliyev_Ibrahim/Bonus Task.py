# bonus_journal.py

# utils.py-dən make_student funksiyasını import edirik
from utils import make_student

def add_student(students, name, score):
    """Tələbəni listə əlavə edir."""
    student_info = make_student(name, score)
    students.append(student_info)

def average_score(students):
    """Orta balı qaytarır, list boşdursa 0 qaytarır."""
    if not students:
        return 0
    total = sum(student['score'] for student in students)
    return total / len(students)

def top_student(students):
    """Ən yüksək ballı tələbənin dictionary-sini qaytarır, list boşdursa None qaytarır."""
    if not students:
        return None
    # 'score' açarına əsasən ən yüksək ballı tələbəni tapır
    best = students[0]
    for student in students:
        if student['score'] > best['score']:
            best = student
    return best

def print_report(students):
    """Hər tələbənin adını və balını, orta balı və ən yaxşı tələbəni çap edir."""
    if not students:
        print("Journal is empty.")
        return
    
    for student in students:
        print(f"{student['name']}: {student['score']}")
    
    avg = average_score(students)
    print(f"Average: {avg:.1f}")
    
    best = top_student(students)
    print(f"Top student: {best['name']} ({best['score']})")

# Əsas proqram (Menyu)
students_list = []

while True:
    print("\n--- Menu ---")
    print("1 Add student")
    print("2 Report")
    print("3 Quit")
    
    choice = input("Choice: ")
    
    if choice == '1':
        name = input("Name: ")
        score = int(input("Score: "))
        add_student(students_list, name, score)
    elif choice == '2':
        print_report(students_list)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
