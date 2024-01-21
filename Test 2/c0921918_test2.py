#Romika Chaudhary
#C0921918
#Test 2
#Dec 14, 2023


#Creating a function divide_me
def divide_me(num1, num2):
    #Checks if num2 is equals to zero
    if num2 == 0:
        return "Cannot divide by zero"

    #Performing division, integer division and obtaining a remainder
    division = num1 / num2
    int_division = num1 // num2
    remainder = num1 % num2
    
    #Returns a list containing division, integer division and remainder
    return [division, int_division, remainder]



#Creating a function format_currency
def format_currency(number):
    #Checks if input is a valid number(integer or float)
    if not isinstance(number, (int, float)):
        #Returns an empty string if the input is not a number
        return ""

    #Formatting currency with 2 decimal point and a comma separator
    formatted_number = "{:,.2f}".format(number)
    return formatted_number



#Creating a function validate_input
def validate_input(string, valid_strings):
    #Checks if all elements in valid_strings are string
    if not all(isinstance(item, str) for item in valid_strings):
        return False

    #Converting to lowercase
    string_lower = string.lower()
    #Returns True if the lowercase input string is found in lowercase valid_strings
    return string_lower in [valid.lower() for valid in valid_strings]



#Creating a function validate_password
def validate_password(password):
    #Checks password length and presence of specific of characers
    if len(password) < 8 or ';' in password or ' ' in password:
        return False

    #Checks if there is onr uppercase, one lowercase and one digit in password
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    return has_upper and has_lower and has_digit



#Creating a function morse_code
def morse_code(input_string):
    #Dictionary containing mappings for letters, numbers and some special characters
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.', '0': '-----',
        ',': '--..--', '.': '.-.-.-', '?': '..--..', ' ': ' '
    }

    #Checks if all characters in the input string are valid for Morse code translation
    if not all(char.upper() in morse_dict for char in input_string):
        return []

    #Returns a list containing the Morse code representation for each character
    return [morse_dict[char.upper()] for char in input_string]
