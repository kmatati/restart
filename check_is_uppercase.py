"""
Check if there is a uppercase char in password
Takes in a string
Returns True if string contains an uppercase , else returns a False
 
variable below were use to test the function at the begining
uppercase = ("ASDFJFJFFJ")
lowercase = ("jsdhjheddejh")
mixcase = ("dgdhghASDD")
my_list = [1,2,"a",5,"hello"]
for _ in my_list:   #  _ can be any variable
for item in my_list:
"""

def has_uppercase(password):
    for character in password:
    
    #    print(character)
        is_uppercase = character.isupper()
    #    print(is_uppercase)
        if is_uppercase == True:
            print("Found uppercase character")
            return True
    
    return False