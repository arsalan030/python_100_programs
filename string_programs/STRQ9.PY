# check all vovwels in a string
vowels = "aeious"
string = "areiousd"
s = set({})
for i  in range(len(string)):
    if string[i] in vowels:
        s.add(string[i])
    else:
        pass

if len(s) == len(vowels):
    print("accepted")
else:
    print("not accepted")

## Python program to accept the strings
# which contains all the vowels

# Function for check if string
# is accepted or not

#using all() method

def check(string):
	vowels = "aeiou" #storing vowels
	if all(vowel in string.lower() for vowel in vowels):
		return "Accepted"
	return "Not accepted"



#initializing string
string = "SEEquoiaL"
# test the function
print(check(string))

#this code contributed by tvsk
