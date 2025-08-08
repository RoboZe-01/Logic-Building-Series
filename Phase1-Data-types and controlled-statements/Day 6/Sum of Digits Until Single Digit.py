
# Sum of Digits Until Single Digit

# Problem statement : Given a positive integer n, repeatedly add all its digits until the result has only one digit, then return that digit.



# Concept : int is not interatable

# Defining the digital add funtion 
def digi_add(n):
   while n>=10:     # Condition so that more than and equal to the 10 is added 
      digi_sum=0
      for digit in str(n) :         # Converted the integer to str so that it can be iterated 
         digi_sum+=int(digit)       # Str is converted back to int so that the addition can be applied 
      n = digi_sum                  # Assinging the digi_sum to n so that it can check again 

   return n                         # Atlast retuning the final output 
 
digi_num = int(input("Enter the number for which u want to find the digi sum : "))   # Taikng number from the user 
print(f"Digital sum of {digi_num} is {digi_add(digi_num)}")
 
         