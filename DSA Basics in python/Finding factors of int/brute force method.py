# finding factors using brute force method"

"""
Factors of the num = it like a divisibles 
"""
n = int(input("Enter the number: "))
num = n 
factors = []

for i in range (1,num+1):
    if num % i==0 :
        factors.append(i)
        
print(factors)         


# This will take so much time for very high number 