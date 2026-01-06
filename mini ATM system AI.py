print ("Welcome to Mini ATM")

user = input ("Please,Enter your User name:\n").lower ()

pin = float (input ("Please,Enter you Pin:\n"))

currect_user = "ibrahim"
currect_pin = 724

if user == currect_user and pin == currect_pin :
    
    print ("Welcome")
    manu = input ("You have 3 choice:(Withdraw,Deposit and log out): \n").upper ()
    
    withdraw = "WITHDRAW"
    deposit = "DEPOSIT"
    log_out = "LOG OUT"
    amount = 10000
    
    if manu == withdraw :
        
        withdraw_amount = float (input ("Enter the amount you want to withdraw: \n"))
        
        if withdraw_amount <= amount :
            
            amount_blanace = amount - withdraw_amount
            print (f"The transaction was successful, the credit remains in your account:'[{amount_blanace}]'")
        
        else :
            print (f"Sorry,You cannot withdraw because your current balance:'[{amount}]',is insufficient for the withdrawal process.")
    
    elif manu == deposit :
        
        deposited_amount = float (input ("Enter the amount you want to deposit: \n"))
        new_amount = deposited_amount + amount
        
        print (f"The transaction was successful; you now have a balance:'[{new_amount}]'")
    
    elif manu == log_out :
        
        print ("Goodbye,")
    
    else :
        print ("Please follow the instructions.")

else :
    print ("Sorry,Please make sure you have entered your username and password correctly.")