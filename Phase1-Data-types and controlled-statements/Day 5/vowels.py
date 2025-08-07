## Problem Statement : Given a lowercase string s, return the number of vowels in the string.
# Only vowels are: a, e, i, o, u

# 📌 Constraints:

# s can be up to 10^5 characters

# Input will always be lowercase

# 🧩 Hints:

# Use a loop to iterate characters

# Use if to check if the character is in the vowel set




# This function is reusable and can use whenever you want 
def count_vowels(s: str) -> int:
    num_vowels = 0
    s= s.lower()
    for i in s :
    
        if i in "aeiou":
            num_vowels+=1
    return num_vowels               ## This will only return the number of vowels in the string    
            
    pass

s = input("Enter your string here : ")            # Taking input from users 
print(f"Number of vowels in the string is : {count_vowels(s)}")       # calling the function and printing the output 
