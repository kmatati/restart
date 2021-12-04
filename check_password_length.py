"""
This function checks password length
Input password string
Returns True >= 8. False if < 8
"""
def password_length(password):
    if len(password) < 8:
        print("Password too short") 
    else:
        print("Password length is Good")
        
