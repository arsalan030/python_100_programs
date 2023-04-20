# to change first and last element in list
lst = [1,3,5,7,9]
temp=lst[0]
lst[0] = lst[len(lst)-1]
lst[len(lst)-1] = temp
print(lst)

# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):
	
	newList[0], newList[-1] = newList[-1], newList[0]

	return newList
	
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))

# Python3 program to swap elements at
# given positions

# Swap function
def swapPositions(list, pos1, pos2):

	# Storing the two elements
	# as a pair in a tuple variable get
	get = list[pos1], list[pos2]
	
	# unpacking those elements
	list[pos2], list[pos1] = get
	
	return list

# Driver Code
List = [23, 65, 19, 90]

pos1, pos2 = 1, 3
print(swapPositions(List, pos1-1, pos2-1))

