list1 = [[1,2,3,],[4,5,6],[7,8,9]]
list2 = list1

print("List 1 : ",list1)		# Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("List 2 : ",list2)		# Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# result/output of below 2 lines will be same as it is not creating new object it is just using/sharing the reference
print("Id of List 1 : ",id(list1))
print("Id of List 2 : ",id(list2))

list1.append([10,11,12])
print("List 1 after append in list 1 : ",list1)		#Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print("List 2 after append in list 1 : ",list2)		#Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

list2.append([13,14,15])
print("List 1 after append in list 2 : ",list1)		#Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
print("List 2 after append in list 2 : ",list2)		#Output : [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
