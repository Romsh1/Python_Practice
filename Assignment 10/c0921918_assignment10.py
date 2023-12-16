#CSD 1233-01
#Assignment 10
#Romika Chaudhary
#C0921918
#December 14, 2023

# Function to add an element to a dictionary
def dict_add_element(dictionary, key, value):
    #Assigns a value to specific key
    dictionary[key] = value
    return dictionary


# Function to get the value corresponding to a key in a dictionary
def dict_get(dictionary, key):
    #If key exists, returns corresponding value for dictionary
    if key in dictionary:
        return dictionary[key]
    else:
        #returns sepcified message if key in not found
        return f"Value {key} not found"


# Function to change a key in a dictionary
def dict_change_key(dictionary, existing_key, new_key):
    if existing_key in dictionary:
        #Moves the value associated with existing_key to new_key
        dictionary[new_key] = dictionary.pop(existing_key)
    return dictionary



# Function to pop a random key-value pair from a dictionary
import random

def dict_pop_item(dictionary):

    dict_copy = dictionary.copy()
    #Checks if the dictionary is not empty
    if dictionary:
        #Chooses a random key from the dictionary
        key = random.choice(list(dictionary.keys()))
        
        # =Creates a tuple with the popped key-value pair
        popped_item = (key, dictionary[key])
        
        #Removes the key-value pair from the dictionary
        del dict_copy[key]
        
        #Returns a list with the updated dictionary as the first element and the popped item as the second element
        return [dict_copy, popped_item[0]]
    else:
        #Returns the original dictionary and None as the popped item, if the dictionary is empty
        return [dictionary, None]



# Function to convert keys to lowercase in a dictionary
def dict_lower(dictionary):
    #Creates a dictionary where keys are converted to lowercase if they are strings
    lowercase_dict = {str(key).lower(): value for key, value in dictionary.items() if isinstance(key, str)}
    #Updates the lowercase_dict with key-value pairs from the original dictionary
    lowercase_dict.update({key: value for key, value in dictionary.items() if not isinstance(key, str)})
    #Returns the resulting dictionary containing keys that are all lowercase if they were initially strings
    return lowercase_dict