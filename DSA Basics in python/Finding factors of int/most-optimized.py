


                    ### Most optimized solution ###

# for that we need to import math module from python 

from math import sqrt


factors = []
def find_factors(num):
    for i in range (1,int(sqrt(num))+1):
        if num %i ==0 :
            factors.append(i)
            if num //i!=i:
                factors.append(num//i)
        factors.sort()
    return factors

def main():
    try :
    # take input from the user    
        n = int(input("Enter the number :" ))  
        num = n
        print(f"factors are : {find_factors(num)}")

    except ValueError:
        print("plz enter approprite number !! ")    

# run the programm 

if __name__ == "__main__" :
    main()




        
