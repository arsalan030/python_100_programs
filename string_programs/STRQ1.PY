#string palidrome
def palindrome(n):
    mid = (len(n)-1)//2
    left= 0
    right = len(n)-1
    flag = 0
    while(left <=mid):
        if n[left]!= n[right]:
            return print("it is not palindrome string")
        elif n[left] == n[right]:
            left +=1
            right-=1

    return  print("string is palindrome")
palindrome('amaama')
    
# Another way to do this question
string = 'amaama'
half = (len(string))//2
first_half = string[:half]
second_half = string[half:]

if first_half == second_half:
    print("string is palindrome")
else:
    print("string is not palindrome")



    

            

