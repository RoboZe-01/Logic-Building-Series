
# Count the digits without using the inbuilt function

# the digit extraction logic is same we will just introduced to the new variable count 

n = int(input("Enter the number : "))
number = n
count = 0
while number >0 :    # THis will run untill number becomes 0 
    
    count+=1        # value of cout will increase by one for each iteration 
    number=number//10        # f;oat div reduce len by one each time untill 0 

print(f'Count of the digits in your number is {count}')



# using inbuilt function

# count = print(f"Your count is {len(str(number))}")  ## This is done using inbuilt python methods