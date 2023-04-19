# remove the ith character from the string
string = "arsalan is boy"
strings = string.split()
del(strings[2])
a =" ".join(strings)
print(a)

# another way to do this question
strn =  "ARSsALAN"

new_str = ""
new_str =''.join([strn[i]for i in range(len(strn))if i!= 2])
print(new_str)
