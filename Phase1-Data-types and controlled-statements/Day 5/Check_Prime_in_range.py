
#itle: Check Prime Between Range

# Problem Statement:
# Given a number n, return a list of all prime numbers from 2 to n (inclusive).


## BAsic code 


# Defined the function 
def prime_num(n):
    # Initialise the empty list 
    prime_list = []
    for num in range (2,n+1):
        is_prime= True
        for i in range(2,int(num**0.5)+1):        ## This will only checks till 
            if num % i==0:
                is_prime=False
                continue
        if is_prime:
                prime_list.append(num)
    return prime_list


# Taking user input 

num_range = int(input("Enter the range for which you want prime numbers :"))
print(f"Prime numbers in the range is : {prime_num(num_range)}")



   
