# remove the duplicate in a string 
def duplicate(string):
    st = []
    for char in string:
        if char not in st:
            st.append(char)
        else:
            continue
    return ''.join(st)

print(duplicate("arsalan"))

# find out the duplicates
def duplicates(strings):
    st = []
    for cha in strings:
        if strings.count(cha) > 1 and   cha not in st:
            st.append(cha)


        else:
            continue
    return ''.join(st)

print(duplicates("arsalanddffggh"))

