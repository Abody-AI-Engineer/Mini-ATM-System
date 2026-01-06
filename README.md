🏦 Project: Mini-ATM System (Professional Portfolio)

3. الكود النهائي (Final Clean Code)
Python

# Project Name: Mini ATM System
# Developer: Abody (Future Software Engineer)  
# Version: 1.0

print("Welcome to Mini ATM")

# Input phase with normalization
user = input("Please, Enter your User name:\n").lower()
pin = float(input("Please, Enter your Pin:\n"))

# Constants (Standards)
CORRECT_USER = "ibrahim"
CORRECT_PIN = 724
INITIAL_BALANCE = 10000

# Security Gate
if user == CORRECT_USER and pin == CORRECT_PIN:
    print("Welcome")
    
    menu = input("You have 3 choice: (Withdraw, Deposit and Log out):\n").upper()
    
    # Process Logic
    if menu == "WITHDRAW":
        withdraw_val = float(input("Enter the amount you want to withdraw:\n"))
        if withdraw_val <= INITIAL_BALANCE:
            INITIAL_BALANCE -= withdraw_val
            print(f"Transaction successful. Remaining balance: [{INITIAL_BALANCE}]")
        else:
            print(f"Insufficient funds. Your current balance is: [{INITIAL_BALANCE}]")
            
    elif menu == "DEPOSIT":
        deposit_val = float(input("Enter the amount you want to deposit:\n"))
        INITIAL_BALANCE += deposit_val
        print(f"Transaction successful. New balance: [{INITIAL_BALANCE}]")
        
    elif menu == "LOG OUT":
        print("Goodbye, see you soon!")
    else:
        print("Invalid option. Please follow the instructions.")
else:
    print("Access Denied: Incorrect username or PIN.")
4. الدروس المستفادة (Lessons Learned)
تعلمت كيفية دمج المخطط البياني مع الكود الفعلي.

أدركت أهمية توقع أخطاء المستخدم (مثل إدخال مبالغ أكبر من الرصيد).

طبقت هندسة الأوامر (Prompt Engineering) لتحسين جودة الشرح والمراجعة.
