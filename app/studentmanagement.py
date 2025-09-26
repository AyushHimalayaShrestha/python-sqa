# Student Management (List of Dictionary)
students = []

def add_student(name, age, grade):
    student = {"name": name, "age": age, "grade": grade}
    students.append(student)

def show_students():
    for s in students:
        print(f"{s['name']} - Age: {s['age']} - Grade: {s['grade']}")

add_student("Ayush", 27, "A")
add_student("Sita", 21, "B")
show_students()
