# find the length of string in four ways
string  = "arsalan is a boy"
new_str = string.replace(" ","")
print(len(new_str))
 
 # solve another way
count = 0
for i in string:
    count +=1
print(count)

# Python3 code to demonstrate working of
# Avoid Spaces in Characters Frequency
# Using isspace() + sum()

# initializing string
test_str = 'geeksforgeeks 33 is best'

# printing original string
print("The original string is : " + str(test_str))

# isspace() checks for space
# sum checks count
res = sum(not chr.isspace() for chr in test_str)
	
# printing result
print("The Characters Frequency avoiding spaces : " + str(res))


