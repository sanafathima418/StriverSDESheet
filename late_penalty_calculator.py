subject = 1 #input()
assignment_no = 6 #input()
student_lost_marks = 30 #input()
late_days = 3 #input()

# 1 - Deep Learning
# 2 - Relational Database Design
# 3 - Advanced Topics

assignment_grade = {1: {1:65, 2:70, 3:125, 4:125, 5:125, 6:126},
                    2: {1:10, 2:10, 3:10, 4:10, 5:50},
                    3: {1:10, 2:15, 3:15, 4:10, 5:9}
                    }
late_day_check = {1:0.9, 2:0.8, 3:0.7}

total_grade = assignment_grade[subject][assignment_no]
student_score = total_grade - student_lost_marks


final_marks = student_score * late_day_check[late_days]
actual_percentage = (student_score/total_grade) * 100  
final_percentage = (final_marks/total_grade) * 100

print("Act Percentage: ", round(actual_percentage, 3))
print("New Percentage: ", round(final_percentage, 3))
print("\nNew Marks: ", round(final_marks, 3))

