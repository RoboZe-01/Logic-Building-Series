
# Problem Title: Unique Elements Count

# Problem statement : Given a list of integers nums, return the number of unique elements in the list.
# Two elements are considered the same if they have the same value.


# Input list of integers (numbers)

list1= [1,2,2,3,3,4,4,1,5,3,5,6,7]

# convert the list to set 

# Made a function to convert the anything to set
def convert_to_set(list):
    converted_set = set(list1)
     
    return converted_set

# called the function 
print(f"The unique numbers are {convert_to_set(list1)} , so the unique count is {len(convert_to_set(list1))}")


