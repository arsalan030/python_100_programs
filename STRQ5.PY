# find the length of string in four ways
string  = "arsalan is a boy"
new_str = string.replace(" ","")
print(len(new_str))
 
 # solve another way
count = 0
for i in string:
    count +=1
print(count)