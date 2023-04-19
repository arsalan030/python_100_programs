# RETURN EVEN word in string
string = "This is a python language"
new_str = string.split()
ss = ""
ss =' '.join([i for i in new_str if len(i)%2==0])
print(ss)

# code
def print_even_length_words(s):
	words = s.replace(',', ' ').split()
	for word in words:
		if len(word) % 2 == 0:
			print(word, end=' ')


s = "geeks for geek"
print_even_length_words(s)
