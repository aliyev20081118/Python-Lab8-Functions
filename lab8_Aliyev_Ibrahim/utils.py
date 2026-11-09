# Tapşırıq 2
def add_vat(price, vat_percent=18):
    return price + (price * vat_percent / 100)
# Tapşırıq 3
def build_username(first, last, year=""):
    username = first.lower() + "." + last.lower()
    if year:
        username += str(year)
    return username

# Tapşırıq 5
def add_bonus(scores, bonus):
    for i in range(len(scores)):
        scores[i] = min(scores[i] + bonus, 100)
        
def with_bonus(scores, bonus):
    new_scores = []
    for score in scores:
        new_scores.append(min(score + bonus, 100))
    return new_scores

# Tapşırıq 6
def average(*numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def make_course(code, **details):
    course_dict = {"code": code}
    for key, value in details.items():
        course_dict[key] = value
    return course_dict
# Bonus task
def make_student(name, score, group=""):
    student_dict = {"name": name, "score": score}
    if group:
        student_dict["group"] = group
    return student_dict
