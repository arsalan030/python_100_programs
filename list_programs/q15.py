# second largest element in a list:
lst  = [12,34,56,77,88,99,100]
lst.sort()
lst.remove(max(lst))
print(max(lst))

def findLargest(arr):
	secondLargest = 0
	largest = min(arr)

	for i in range(len(arr)):
		if arr[i] > largest:
			secondLargest = largest
			largest = arr[i]
		else:
			secondLargest = max(secondLargest, arr[i])

	# Returning second largest element
	return secondLargest


# Calling above method over this array set
print(findLargest([10, 20, 4, 45, 99]))

