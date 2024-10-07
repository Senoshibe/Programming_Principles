all_students_marks = []

for x in range(0,5):
    student_marks = input (f"Student {x + 1} (course 1 - 4): ")
    student_split = student_marks.split()

    while len(student_split) != 4:
        student_marks = input (f"Student {x + 1} (course 1 - 4): ")
        student_split = student_marks.split()
    
    all_students_marks.append(student_split)

all_students_marks = [[int(value) for value in row] for row in all_students_marks]

def average_row(matrix, row_index):
    sum_of_row = sum(matrix[row_index])
    return sum_of_row/len(matrix[row_index])

def average_column(matrix, column_index):
    col_sum = 0
    row_count = len(matrix)
    for row in matrix:
        col_sum += row[column_index]
    return col_sum/row_count

highest_student_average = 0
for row_index in range(0,5): 
    average_row(all_students_marks, row_index)
    current_average_row = float(average_row(all_students_marks, row_index))
    if highest_student_average < current_average_row:
        highest_student_average = current_average_row

highest_course_average = 0    
for column_index in range(0,4):
    average_column (all_students_marks, column_index)
    current_average_column = float(average_column(all_students_marks, column_index))
    if highest_course_average < current_average_column:
        highest_course_average = current_average_column

print(f"The highest average mark of students: {highest_student_average}")
print(f"The highest average mark of course: {highest_course_average}")