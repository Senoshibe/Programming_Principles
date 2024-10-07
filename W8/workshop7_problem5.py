all_students_marks = []

for x in range(0,5):
    student_marks = input (f"Student {x + 1} (course 1 - 4): ")
    student_split = student_marks.split()

    while len(student_split) != 4:
        student_marks = input (f"Student {x + 1} (course 1 - 4): ")
        student_split = student_marks.split()

    

