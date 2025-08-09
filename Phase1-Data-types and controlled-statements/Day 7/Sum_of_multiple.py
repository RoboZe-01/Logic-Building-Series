# Proble tittle : Sum of Multiples
# Problem statement : Given an integer n, return the sum of all numbers from 1 to n that are divisible by 3 or 5.

def sum_of_multiple (n):
    sum_num = 0
    for num in range(1,n+1):
        if num%3==0 or num%5 ==0:
             sum_num+=num
    
    return sum_num

use_input= int(input("Enter the num to find the addition of multiple : "))        
print(f'For the given number {use_input} the addition of multiples is {sum_of_multiple(use_input)}')
