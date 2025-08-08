## Hard Problem 
#Python Script Challenge: ATM Simulation


# Problem:

# Initial balance = ₹5000

# Ask the user to enter the amount to withdraw

# If amount > balance → print "Insufficient funds"

# Else → deduct amount and show remaining balance

# Allow multiple transactions (use a loop)

# Exit when user enters "exit" or balance becomes 0




# Fisrt current amont stored as a int 

current_amt = int(2500)
user_pass = "12345"

# We should make actions functions --> check amount , --> withdraw (w)(Subtract) , --> Deposit ( add)(D)



# Define check amt function 
def check_amt(amt):
    amt = current_amt
    return print(f'Your current amount is : {current_amt}')         ## Return the current amoount 

# Calling current_amt function 

# check_amt(current_amt)


# Making withdraw function 

def withdraw(amt):
    global current_amt
    withdraw_amt =  amt
    current_amt = current_amt-withdraw_amt
    check_amt(current_amt)
    return withdraw_amt

# checking withdraw function 
# amt = 500
# print(f'your withdraw amount is {withdraw(amt)}')


def deposit(amt):
     global current_amt
     current_amt = current_amt+amt
     print(f'This amout is deposited : {amt}')
     return current_amt

# amt2= 500 
# print(f'After deposit your amount is : {deposit(amt2)}')



                           ### Main Script ### 

# We will loop this according to users input 


while True :
    print("Good Greeting welcome to our ATM ")
    user_input = input(" Do want to proceed Choose (Y/N) : " )

    while user_input.lower()=='y':
        print("Welcome to your account")

        use_pass = input("Please enter your secret number : ")
    
        if use_pass== user_pass:
            action_input= int( input(""" Enter 1 --> check current balance  ,
                                    Enter 2 --> To withdraw Amount ,
                                    Enter 3 --> To deposit  amount"""))
            if action_input == 1:
                check_amt(current_amt)
            elif action_input == 2:
                amount = int(input("Enter the amount you want to withdraw : "))   
                print(f"{withdraw(amount)} is withdrawn from your account")
            elif action_input ==3 :
                depo_amount = int(input("Enter the amount you wanna deposit to your account : "))    
                print(f'Current amount is : {deposit(depo_amount)}')
            else:
             print("Exiting the screen  ")    

        else:  
            break   


        




