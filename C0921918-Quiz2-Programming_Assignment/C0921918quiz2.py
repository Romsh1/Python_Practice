#Romika Chaudhary
#C0921918
#Quiz 2 - Programming Assignment
#November 23, 2023


#Defining sort_str_int_float_list() function
def sort_str_int_float_list(sequence):

    #Creating an empty list to store string elements
    str_list = []

    #Creating an empty list to store integer elements
    int_list = []

    #Creating an empty list to store float elements
    float_list = []


    #Loop through each item in the input sequence
    for item in sequence:
        #Checking if the item is string
        if isinstance(item, str):
            #Appending the string to string list
            str_list.append(item)
        #Checking if the item is integer
        elif isinstance(item, int):
            #Appending the integer to integer list
            int_list.append(item)
        #Checking if the item is float
        elif isinstance(item, float):
            #Appending the float to float list
            float_list.append(item)

#Returns a two dimensional list with the sorted elements
    return [str_list, int_list, float_list]


