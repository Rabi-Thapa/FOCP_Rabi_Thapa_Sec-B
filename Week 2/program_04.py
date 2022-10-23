total_no_of_sweets= int(input("Total no of sweets? "))
total_no_of_students= int(input("Total no of students? "))

each_student_get= total_no_of_sweets // total_no_of_students
left_over= total_no_of_sweets- (each_student_get* total_no_of_students)

print("Each Student will get {} and the {} sweets will be left.".format(each_student_get,left_over))
