# Problem statements : COnvert celcius to feranite or kelvin


## Function to convert celcius to kelvin 
def celcius_to_kelvin(temp):
    return temp + 273.15

# Function to convert kelvin to celcius 
def kelvin_to_celcius(temp):
    return temp - 273.15

# Function to convert celcius to fahranite 
def celcius_to_fahrenite(temp):
    return ( temp*1.8) + 32

# Function to convert fahranite to celcius 
def fahrenite_to_celcius(temp):
    return (temp -32)*1.8

#  Creating the loop to ask the question to make temperature convertor



while True : 
    print("Which value you want to convert to which ? ")
    ask_user = input("""
            1 . Enter 1 to convert celcius to kelvin
            2 . Enter 2 to convert kelvin to celcius 
            3 . Enter 3 to conver celcius to fahranite 
            4 . Enter 4 to convert fahranite to celcius 
                    

                    Choose :""")
    if ask_user== "1" :
        user_value = int(input("Enter the temp in celcius ( only give int value ): "))
        print( f' {user_value} is celcius is {celcius_to_kelvin(user_value)} in kelvin ')
    elif ask_user== "2" :
        user_value = int(input("Enter the temp in kelvin ( only give int value ): "))
        print( f' {user_value} is kelvin is {kelvin_to_celcius(user_value)} in celcius')    
    elif ask_user== "3" :
        user_value = int(input("Enter the temp in celcius ( only give int value ): "))
        print( f' {user_value} is celcius is {celcius_to_fahrenite(user_value)} in farhnite')    
    elif ask_user== "4" :
        user_value = int(input("Enter the temp in farhanite ( only give int value ): "))
        print( f' {user_value} is farhanite is {fahrenite_to_celcius(user_value)} in celcius')    

