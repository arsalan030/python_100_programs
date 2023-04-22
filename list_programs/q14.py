test_list = [12, 67, 98, 34]

# printing original list
print("The original list is: " + str(test_list))

# Sum of number digits in List
# using loop + str()
res = [sum(int(digit) for digit in str(ele)) for ele in test_list]

# printing result
print("List Integer Summation: " + str(res))
