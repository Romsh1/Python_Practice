#CSD-1233-01
#Assignment 7
#Romika Chaudhary
#November 16,2023


#Creating a function write_to_file
def write_to_file(filename, content):
    result = 0
    try:
        # Open a file in write mode
        with open(filename + ".txt", "w") as file_obj:
            file_obj.write(content)
    except Exception as e:
        result = str(e)
    return result

#Creating a function append_to_file
def append_to_file(filename, content):
    result = 0
    try:
        # Open a file in append mode
        with open(filename + ".txt", "a") as file_obj:
            file_obj.write(content)
    except Exception as e:
        result = str(e)
    return result

#Creating A function read_from_file
def read_from_file(filename):
    result = ""
    try:
        # Open a file in read mode
        with open(filename + ".txt", "r") as file_obj:
            result = file_obj.read()
    except Exception as e:
        result = str(e)
    return result

#Creating a function read_from_file_to_array
def read_from_file_to_array(filename):
    result = []
    try:
        # Open a file in read mode
        with open(filename + ".txt", "r") as file_obj:
            result = file_obj.readlines()
    except Exception as e:
        result = [str(e)]
    return result

#Creating a function improved_read_from_file_to_array
def improved_read_from_file_to_array(filename):
    result = []
    try:
        # Open a file in read mode
        with open(filename + ".txt", "r") as file_obj:
            result = [line.strip() for line in file_obj.readlines()]
    except Exception as e:
        result = [str(e)]
    return result


