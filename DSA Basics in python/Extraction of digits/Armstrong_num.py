# find out number is armstrong number or not 

"""
Armstrong number is when 
1234 = 1^4 + 2^4 +3^4 + 4^4  == 1234

it is like , if we add the digits in the number of digit having the power of the lenght of the number 
if it is equal to the original number then it is armstrong number

"""

              ###  Programm start from here ### 


n = int(input("Enter the number : "))              # Taking input from the user 
num = n                                            # assigning this to different vatible as we dont want to change original one 


# Making a function to find the armstrong or not 

def find_armstrong(num):              
 nod = len(str(num))            # finding the length of the number ( used str as int dont have len method)
 total = 0                      # inital total put to zero 
 while num>0 :                  # loop to find the total value of armstrong style 
  ld = num %10                  # Finding last digit 
  total = total+(ld**nod)       # adding digit to armstrong 
  num = num //10
 return total 


# calling the function and using it to a new programme
if find_armstrong(num) == n :
 print(f"Your number {n} is an armstrong number")
else:
 print(f'Your number {n} is not armstrong number ') 
 
