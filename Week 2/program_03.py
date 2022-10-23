total_no_of_stud= int(input("How many students?     "))
req_group_size= int(input("Required group size?    "))
full_group= total_no_of_stud// req_group_size
left_over= total_no_of_stud- (full_group * req_group_size)
print("There will be {} groups with {} students left over.".format(full_group,left_over))

