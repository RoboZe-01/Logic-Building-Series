
# Here we can extract the num in reverse order

# here we will learn how can we extract the digits in the number 
#Like 3456 becomes --> 3 4 5 6 - seperate digits 

"""
for that we need to understand one concept that when we divide any number to 10 
the remainder will be the last number 

for example if we divide 3456 / 10 the remainder will be 6 --> 345.6 the 6 will be the remainder

that is 3456 % 10 = 6

thus we will get our first later from there
then we can float divide the rest of the number to get only the int value 
and put that in the loop 

"""

n  = int(input("Enter the number for which you want to extract the digits : "))

number = n   # it is a good practice to not to change the input directly rather than that we can assign different varible and put input in there

# creating the while loop untill the the float division is 0 

while number >0 :
    new_num = number %10 
    print ("This is the digit : ",new_num)

    number=number//10
