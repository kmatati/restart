"""
Password Strength Checker.

Features:
    - Password Length
    - Mixed-Case Passwords
    - Contains Numbers (Alphanumeric)
    - Contains Special Characters (Punctuation)
    - Checks if Too Common (Against a common passwords list)
"""
import check_is_uppercase 
import check_password_length
import check_for_number


# Ask for the password
answer = input("Hello, you want to check your password? y/n  ")
attempt = 0
#while attempt < 3:
if answer == "y" in answer or "Y" in answer:
    password = input("Enter your password (min 8 char): ")
    #print("",password + "!")
    password_length = len(password)
    print("Password length:" + str(password_length))
    #print(type(password_length)) #just to test if the str change the type it doesn't
elif answer == "n" in answer or "N" in answer:
    exit()

#get the length of the password
password_length = check_password_length.password_length(password)

#check if there is at leas 1 digit
has_a_number = check_for_number.has_number(password)
if has_a_number == False:
    print("you need at least one number")
    exit()
#check if there is at leas one uppercase    
has_uppercase_char = check_is_uppercase.has_uppercase(password)
if has_uppercase_char == False:
    print("However your password must contain uppercase characters!")
    exit()



 # TODO: Change from hardcoded value later.
    

