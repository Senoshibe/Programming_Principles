all_students_marks = []

for x in range(0,5):
    student_marks = input(f"Student {x+1} (courses 1-4): ")
    student_marks_split = student_marks.split()
    all_students_marks.append(student_marks_split)

all_students_marks = [[float(value) for value in row] for row in all_students_marks]

def average_marks_student(matrix, row_index): 
    total_marks_student = sum(matrix[row_index])
    number_of_marks = len(matrix[row_index])
    return total_marks_student/number_of_marks

def average_marks_course(matrix, column_index):
    total_marks_course = 0
    number_of_courses = len(matrix)

    for row in matrix:
        total_marks_course += row[column_index]

    return total_marks_course/number_of_courses

highest_average_marks_student = 0

for i in range(0,5):
    row_index = i
    average_marks_student(all_students_marks, row_index)
    if highest_average_marks_student < float(average_marks_student(all_students_marks, row_index)):
        highest_average_marks_student = float(average_marks_student(all_students_marks, row_index))

print(f"The highest average mark of students: {highest_average_marks_student}")

highest_average_marks_course = 0

for j in range(0,4):
    column_index = j
    average_marks_course(all_students_marks, column_index)
    if highest_average_marks_course < float(average_marks_course(all_students_marks, column_index)):
        highest_average_marks_course = float(average_marks_course(all_students_marks, column_index))

print(f"The highest average mark of course: {highest_average_marks_course}")


