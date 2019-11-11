import copy
# DC = Deep copy actually creates a new object also creates new references of nested object, This is not
# like Shallow Copy

original_list = [[1,2,3,],[4,5,6],[7,8,9]]
copy_list = copy.deepcopy(original_list)

# creating new object with 3 nested objects, both result will be same
print("Original List : ",original_list)		# Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Copied List : ",copy_list)		# Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# result/output of below 2 lines will not be same as it is creating new object with new nested objects
# it will not share reference of original nested objects.
# This is not like Shallow copy
print("Id of Original List : ",id(original_list))
print("Id of Copied List : ",id(copy_list))

# result/output of below 2 lines will not be same as it is not sharing the reference of nested elements of original object
# This is not like Shallow copy
print("Id of Original List 0th element : ",id(original_list[0]))
print("Id of Copied List 0th element  : ",id(copy_list[0]))

original_list.append(["a","b","c"])
print("Original List after append in original_list : ",original_list)		#Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['a', 'b', 'c']]
print("Copied List after append in original_list : ",copy_list)		#Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

copy_list.append(["p","q","r"])
print("Original List after append in copy_list : ",original_list)		#Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['a', 'b', 'c']]
print("Copied List after append in copy_list : ",copy_list)		#Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['p', 'q', 'r']]

# result/output of below 2 lines will not be same as it is not sharing the reference of nested elements of
# original object
print("Id of Original List 3th element : ",id(original_list[3]))
print("Id of Copied List 3th element  : ",id(copy_list[3]))

# Value of "D" will be added to Copied List only, because No connection between Original & Copied List
copy_list[1][1]="D"
# Value of "X" will be added to Copied List only, because No connection between Original & Copied List
copy_list[3][1]="X"

# Value of "M" will be copied to Original List only, because No connection between Original & Copied List
original_list[1][2]="M"
# Value of "N" will not be copied to Original List only, because No connection between Original & Copied List
original_list[3][2]="N"

print("New Original List : ",original_list)		#Output : [[1, 2, 3], [4, 5, 'M'], [7, 8, 9], ['a', 'b', 'N']]
print("New Copied List : ",copy_list)		#Output : [[1, 2, 3], [4, 'D', 6], [7, 8, 9], ['p', 'X', 'r']]


#This will delete 1st index element from Original list only, No affect on Copy list
original_list.pop(1)
print("original_list after delete in original_list : ",original_list)		#Output : [[1, 2, 3], [7, 8, 9], ['a', 'b', 'N']]
print("copy_list after delete in original_list : ",copy_list)		#Output : [[1, 2, 3], [4, 'D', 'M'], [7, 8, 9], ['p', 'X', 'r']]

#This will delete [7, 8, 9] element from Copy list only, No affect on Original list
copy_list.remove([7, 8, 9])
print("original_list after delete in copy_list : ",original_list)		#Output : [[1, 2, 3], [7, 8, 9], ['a', 'b', 'N']]
print("copy_list after delete in copy_list : ",copy_list)		#Output : [[1, 2, 3], [4, 'D', 'M'], ['p', 'X', 'r']]