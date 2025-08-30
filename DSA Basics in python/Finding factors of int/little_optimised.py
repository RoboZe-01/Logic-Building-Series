# Let's optimize this programm to get better time compelxity 

"""
for solution we don't need to iterate all the way to the number 
we can just uterate to halfway then append 

it wroks like : for examle find factorial of 10 
1 -1
2-1
3-0
4-0
5-1
6-0
7-0
8-0
9-0
10-1       From that you can see after halfway through the numbers are not factors of the num 
so using same logic here 
"""


n = int(input("ENter the number : "))
num = n 
factors =[]
for i in range(1,(num//2)+1):     # we optimized this code now it don't need to iterate through all the numbers
    if num % i ==0:
        factors.append(i)
print(factors)        