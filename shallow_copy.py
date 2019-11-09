import copy
# SC = Shallow copy actually creates a new object which stores reference of original object,

original_list = [[1,2,3,],[4,5,6],[7,8,9]]
copy_list = copy.copy(original_list)

# creating new object with 3 nested objects
print("Original List : ",original_list)		# Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Copied List : ",copy_list)		# Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# result/output of below 2 lines will not be same as it is creating new object but nested objects will
# will not be created, it will share reference of original nested objects
print("Id of Original List : ",id(original_list))
print("Id of Copied List : ",id(copy_list))

# result/output of below 2 lines will be same as it is sharing the reference of nested elements of original object
# output of nested 3 elements will be same as when this step "copy.copy(original_list)" executed ,
# it was having 3 nested elements
print("Id of Original List 0th element : ",id(original_list[0]))
print("Id of Copied List 0th element  : ",id(copy_list[0]))

original_list.append(["a","b","c"])
print("Original List after append in original_list : ",original_list)		#Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print("Copied List after append in original_list : ",copy_list)		#Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

copy_list.append(["p","q","r"])
print("Original List after append in copy_list : ",original_list)		#Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
print("Copied List after append in copy_list : ",copy_list)		#Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

# result/output of below 2 lines will not be same as it is not sharing the reference of nested elements of
# original object, So output of only nested 3 elements will be same as when this step "copy.copy(original_list)" executed ,
# it was having 3 nested elements, after 3rd nested elements every newly created nested element will
# have different reference.
print("Id of Original List 3th element : ",id(original_list[3]))
print("Id of Copied List 3th element  : ",id(copy_list[3]))

# Value of "D" will be copied to both Original & Copied List, because of above reason : line 30 to 33
copy_list[1][1]="D"
# Value of "X" will not be copied to both Original & Copied List, because of above reason : line 30 to 33
copy_list[3][1]="X"

# Value of "M" will be copied to both Original & Copied List, because of above reason : line 30 to 33
original_list[1][2]="M"
# Value of "N" will not be copied to both Original & Copied List, because of above reason : line 30 to 33
original_list[3][2]="N"

print("Original List after append in copy_list : ",original_list)		#Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
print("Copied List after append in copy_list : ",copy_list)		#Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
