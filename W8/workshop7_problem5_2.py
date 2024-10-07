all_students_marks = []

for x in range(0,5):
    student_marks = input(f"Student {x+1} (courses 1-4): ")
    student_marks_split = student_marks.split()
    all_students_marks.append(student_marks_split)

print(all_students_marks)
