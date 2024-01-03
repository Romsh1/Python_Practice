#Romika Chaudhary
#Jan 2, 2024

import random
import string

def generate_password(min_length, numbers = True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

#Creating string that contains all of the characters
#from whivh we could be selecting
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
    
    pwd = " "
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd 

#Asking user input or minimum length of password, whether or not to include number or special characters
min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"

#Calling the main function by passing arguments
pwd = generate_password(min_length, has_number, has_special)
print("The generated password is: ", pwd)