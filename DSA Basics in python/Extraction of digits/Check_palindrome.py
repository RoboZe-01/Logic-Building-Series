# Problem statement : Is palindrome or not 
# Palindrome -->             actual word == word in reverse 

"""
steps : 1. digit extraction 
        2. Making a varible to store the reverse digits 
        3. then checking the logic 


"""

n = int(input("Enter the number : "))
num = n 

# Function to check palindrome 

def check_palindrome(num, num_reverse):
    if num == num_reverse:
        return "It is a palindrome"  
    else :
        return "It is not a palindrome"


# Function to reverse the num
def reverse_num(num):
    result = 0
    while num >0 :
        ld =num%10
        result = result*10 +ld
        num = num//10
    return result       
    




print(f"Your number is {check_palindrome(num , reverse_num(num))}")