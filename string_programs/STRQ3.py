# revers words in given string in python
strings = "arsalan"
st = []
for char in strings[::-1]:
    st.append(char)
a = "".join(st)

print(a)

# another way to this question
# Function to reverse words of string

def rev_sentence(sentence):

	# first split the string into words
	words = sentence.split(' ')

	# then reverse the split string list and join using space
	reverse_sentence = ' '.join(reversed(words))

	# finally return the joined string
	return reverse_sentence

input = 'geeks quiz practice code'
print (rev_sentence(input))



