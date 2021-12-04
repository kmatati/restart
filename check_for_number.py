"""
Check if there is a 'number character' in password
Takes in a string
Returns True if string contains a number , else returns a False
 
"""

def has_number(password):
    for character in password:
        is_digit = character.isdigit()
        if is_digit == True:
            print("digit is present")
            return True
    return False
   