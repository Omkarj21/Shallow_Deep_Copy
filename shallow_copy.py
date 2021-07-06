import copy
# SC = Shallow copy actually creates a new object but stores reference of original object.

original_list = [[1,2,3,],[4,5,6],[7,8,9]]
copy_list = copy.copy(original_list)

# creating new object with 3 nested objects
print("Original List : ",original_list)		# Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Copied List : ",copy_list)		# Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# result/output of below 2 lines will not be same as it is creating new object but nested objects will
# will not be created, it will share reference of original nested objects
print("Id of Original List : ",id(original_list))  # Id of Original List :  1563020705864
print("Id of Copied List : ",id(copy_list))        # Id of Copied List   :  1563020707272

# result/output of below 2 lines will be same as it is sharing the reference of nested elements of original object
# output of nested 3 elements will be same as when this step "copy.copy(original_list)" executed ,
# it was having 3 nested elements
print("Id of Original List 0th element : ",id(original_list[0])) # Id of Original List 0th element :  1563020678984
print("Id of Copied List 0th element  : ",id(copy_list[0]))      # Id of Copied List 0th element   :  1563020678984

original_list.append(["a","b","c"])
print("Original List after append in original_list : ",original_list)		#Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['a', 'b', 'c']]
print("Copied List after append in original_list : ",copy_list)		#Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

copy_list.append(["p","q","r"])
print("Original List after append in copy_list : ",original_list)		#Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['a', 'b', 'c']]
print("Copied List after append in copy_list : ",copy_list)		#Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['p', 'q', 'r']]

# result/output of below 2 lines will not be same as it is not sharing the reference of nested elements of
# original object, So output of only nested 3 elements will be same as when this step "copy.copy(original_list)" executed ,
# it was having 3 nested elements, after 3rd nested elements every newly created nested element will
# have different reference.
print("Id of Original List 3th element : ",id(original_list[3])) # Id of Original List 3th element :  2304153175752
print("Id of Copied List 3th element  : ",id(copy_list[3]))      # Id of Copied List 3th element   :  2304153175432

# Value of "D" will be added to both Original & Copied List, because of above reason : line 30 to 33
copy_list[1][1]="D"
# Value of "X" will not be added to both Original & Copied List, because of above reason : line 30 to 33
copy_list[3][1]="X"

# Value of "M" will be added to both Original & Copied List, because of above reason : line 30 to 33
original_list[1][2]="M"
# Value of "N" will not be added to both Original & Copied List, because of above reason : line 30 to 33
original_list[3][2]="N"

print("New Original List : ",original_list)		#Output : [[1, 2, 3], [4, 'D', 'M'], [7, 8, 9], ['a', 'b', 'N']]
print("New Copied List : ",copy_list)		#Output : [[1, 2, 3], [4, 'D', 'M'], [7, 8, 9], ['p', 'X', 'r']]

#This will delete 1st index element from Original list only, No affect on Copy list
original_list.pop(1)
print("original_list after delete in original_list : ",original_list)		#Output : [[1, 2, 3], [7, 8, 9], ['a', 'b', 'N']]
print("copy_list after delete in original_list : ",copy_list)		#Output : [[1, 2, 3], [4, 'D', 'M'], [7, 8, 9], ['p', 'X', 'r']]

#This will delete [7, 8, 9] element from Copy list only, No affect on Original list
copy_list.remove([7, 8, 9])
print("original_list after delete in copy_list : ",original_list)		#Output : [[1, 2, 3], [7, 8, 9], ['a', 'b', 'N']]
print("copy_list after delete in copy_list : ",copy_list)		#Output : [[1, 2, 3], [4, 'D', 'M'], ['p', 'X', 'r']]
