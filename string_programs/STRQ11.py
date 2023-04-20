# find number of vowels in a string using set
string  = "aaeeious"
dict = {}
vowels = "aeious"
for char in range(len(string)):
    if string[char] not in dict:
        dict[string[char]] =1
    else :
        dict[string[char]] +=1
print(dict)

print(len(dict))

count = 0
s = set(string)
for i in s:
    if i in vowels:
        count +=1
print(count)

def vowel_count(str):
	# Creating a list of vowels
	vowels = "aeiouAEIOU"
	
	# Using list comprehension to count the number of vowels in the string
	count = len([char for char in str if char in vowels])
	
	# Printing the count of vowels in the string
	print("No. of vowels :", count)

# Driver code
str = "GeeksforGeeks"

# Function Call
vowel_count(str)





