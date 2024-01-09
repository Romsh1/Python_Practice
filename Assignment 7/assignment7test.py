'''
Test Program for Assignment #7
This program will test your Assignment #7 file
WARNING: Do not make any changes to the file other than the one shown below.
Doing so may cause the program to not work correctly.
To use program, follow these steps:
1. Update the first import line below to the name of your program (do not include .py)
2. Save this file
3. Copy this file to the same location as your assignment (if it is not already)
4. Run the test program
The program should display the results compared to the expected results,
your score for each function, and your total score for the assignment.
'''

# IMPORTS
import c0921918Assignment7 as testFile #<---- UPDATE THIS TO YOUR yourFileNameHere (DO NOT INCLUDE .PY)
import os

# GLOBAL CONSTANTS

# Maximum scores
MAX_SCORES = [5,5,5,5,5]
MAX_TOTAL = 25

# Filename for file to test reading
TEST_FILENAME = "readtest"
# Content for file to test reading
TEST_FILE_CONTENT = "This is the first line.\nThis is the second line.\nThis is the third line."

# Test values are stored in a two-dimensional array.
# Outer array is different tests
# Inner array is listed for each

#1: filename, text written, expected value returned by funnction, expected file contents after writing
TEST_VALUES1 = [ ["testfile1","This is the text","0","This is the text"],
                ["testfile1","This is also text","0","This is also text"],
                ["bad/path","This shouldn't work.","[Errno 2] No such file or directory: 'bad/path.txt'",""],
                ["bad*char","This also shouldn't work.","[Errno 22] Invalid argument: 'bad*char.txt'",""],
                ["<badchar>","This also shouldn't work.","[Errno 22] Invalid argument: '<badchar>.txt'",""]
                ]

#2: filename, text written/appended, expected value returned by function, contents after writing/appending
TEST_VALUES2 = [ ["testfile2","This is the text","0","This is the text"],
                ["testfile2","This is also text","0","This is the textThis is also text"],
                ["bad/path","This shouldn't work.","[Errno 2] No such file or directory: 'bad/path.txt'",""],
                ["bad*char","This also shouldn't work.","[Errno 22] Invalid argument: 'bad*char.txt'",""],
                ["<badchar>","This also shouldn't work.","[Errno 22] Invalid argument: '<badchar>.txt'",""]
                ]

#3 filename, expected contents returned by function
TEST_VALUES3 = [ [TEST_FILENAME,TEST_FILE_CONTENT],
                 [TEST_FILENAME,TEST_FILE_CONTENT],
                 ["bad/path","[Errno 2] No such file or directory: 'bad/path.txt'"],
                 ["bad*char","[Errno 22] Invalid argument: 'bad*char.txt'"],
                 ["<badchar>","[Errno 22] Invalid argument: '<badchar>.txt'"]
                 ]

#4 filename, expected contents returned by function
TEST_VALUES4 = [ [TEST_FILENAME,['This is the first line.\n','This is the second line.\n','This is the third line.']],
                 [TEST_FILENAME,['This is the first line.\n','This is the second line.\n','This is the third line.']],
                 ["bad/path",["[Errno 2] No such file or directory: 'bad/path.txt'"]],
                 ["bad*char",["[Errno 22] Invalid argument: 'bad*char.txt'"]],
                 ["<badchar>",["[Errno 22] Invalid argument: '<badchar>.txt'"]]
                 ]

#4 filename, expected contents returned by function
TEST_VALUES5 = [ [TEST_FILENAME,TEST_FILE_CONTENT.split('\n')],
                 [TEST_FILENAME,TEST_FILE_CONTENT.split('\n')],
                 ["bad/path",["[Errno 2] No such file or directory: 'bad/path.txt'"]],
                 ["bad*char",["[Errno 22] Invalid argument: 'bad*char.txt'"]],
                 ["<badchar>",["[Errno 22] Invalid argument: '<badchar>.txt'"]]
                 ]

#GLOBAL VARIABLES


def main():
    # Initialize test scores at 0
    test_scores = [0,0,0,0,0]
    total_score = 0

    #Test each function
    print("Testing Function #1:")
    test_scores[0] = test_function_1()
    print("Function 1:", test_scores[0], "/", MAX_SCORES[0])

    print("\nTesting Function #2:")
    test_scores[1] = test_function_2()
    print("Function 2:", test_scores[1], "/", MAX_SCORES[1])

    print("\nTesting Function #3:")
    test_scores[2] = test_function_3()
    print("Function 3:", test_scores[2], "/", MAX_SCORES[2])

    print("\nTesting Function #4:")
    test_scores[3] = test_function_4()
    print("Function 4:", test_scores[3], "/", MAX_SCORES[3])

    print("\nTesting Function #5:")
    test_scores[4] = test_function_5()
    print("Function 5:", test_scores[4], "/", MAX_SCORES[4])

    #Display total score
    for score in test_scores:
        total_score += score

    print("\nTOTAL SCORE:", total_score, "/", MAX_TOTAL)
    
# TESTING LOOPS
# LOOP THROUGH TEST VALUES FOR EACH FUNCTION. CALL TEST FUNCTIONS WITH THESE VALUES
# AND RETURN TOTAL SCROE FOR EACH FUNCTION
# (5 FUNTIONS TO TEST)
def test_function_1():
    score = 0
    
    for test_values in TEST_VALUES1:
        if (test_write_to_file(test_values[0], test_values[1], test_values[2], test_values[3])):
            score += 1
            print("PASS")
        else:
            print("FAIL")

    return score

def test_function_2():
    score = 0
    
    if (os.path.exists(TEST_VALUES2[0][0] + ".txt")):
        os.remove(TEST_VALUES2[0][0] + ".txt")
    for test_values in TEST_VALUES2:
        if (test_append_to_file(test_values[0], test_values[1], test_values[2], test_values[3])):
            score += 1
            print("PASS")
        else:
            print("FAIL")

    return score

def test_function_3():
    score = 0

    file_obj = open(TEST_FILENAME + ".txt", "w")
    file_obj.write(TEST_FILE_CONTENT)
    file_obj.close()

    for test_values in TEST_VALUES3:
        if (test_read_from_file(test_values[0], test_values[1])):
            score += 1
            print("PASS")
        else:
            print("FAIL")

    return score

def test_function_4():
    score = 0

    file_obj = open(TEST_FILENAME + ".txt", "w")
    file_obj.write(TEST_FILE_CONTENT)
    file_obj.close()

    for test_values in TEST_VALUES4:
        if (test_read_from_file_to_array(test_values[0], test_values[1])):
            score += 1
            print("PASS")
        else:
            print("FAIL")

    return score

def test_function_5():
    score = 0

    file_obj = open(TEST_FILENAME + ".txt", "w")
    file_obj.write(TEST_FILE_CONTENT)
    file_obj.close()

    for test_values in TEST_VALUES5:
        if (test_improved_read_from_file_to_array(test_values[0], test_values[1])):
            score += 1
            print("PASS")
        else:
            print("FAIL")

    return score

# END OF TESTING LOOPS

# TEST FUNCTIONS. THESE EACH ACCEPT TEST VALUES AND EXPECTED RESULTS.
# USING THESE VALUES, THEY EACH TEST A SPECIFIC FUNCTION IN THE IMPORTED FILE
# EACH RETURNS TRUE IF ACTUAL RESULTS MATCH EXPECTED RESULTS
# (5 FUNCTIONS TO TEST)
def test_write_to_file(filename, text, expected_result, expected_contents):
    passed = False
    file_contents = ''
    result = ''

    try:
        result = testFile.write_to_file(filename, text)

        if (str(result) == '0'):
            file_obj = open(filename + ".txt", "r")
            file_contents = file_obj.read().rstrip('\n')
            file_obj.close()
    except Exception as e:
        result = 'YOUR FUNCTION THREW AN UNCAUGHT ERROR: ' + str(e)

    print("Expected Result:", expected_result)
    print("Result:", result)

    print("Expected file contents:", expected_contents)
    print("File contents:",file_contents)

    if file_contents == expected_contents and str(result) == str(expected_result):
        passed = True

    return passed

def test_append_to_file(filename, text, expected_result, expected_contents):
    passed = False
    file_contents = ''
    result = ''

    try:
        result = testFile.append_to_file(filename, text)

        if (str(result) == '0'):
            file_obj = open(filename + ".txt", "r")
            file_contents = file_obj.read().rstrip('\n')
            file_obj.close()
    except Exception as e:
        result = 'YOUR FUNCTION THREW AN UNCAUGHT ERROR: ' + str(e)

    print("Expected Result:", expected_result)
    print("Result:", result)

    print("Expected file contents:", expected_contents)
    print("File contents:",file_contents)

    if file_contents == expected_contents and str(result) == str(expected_result):
        passed = True

    return passed

def test_read_from_file(filename, expected_result):
    passed = False
    file_contents = ''
    result = ''

    try:
        result = testFile.read_from_file(filename)

    except Exception as e:
        result = 'YOUR FUNCTION THREW AN UNCAUGHT ERROR: ' + str(e)

    print("Expected Result:", expected_result)
    print("Result:", result)

    if result == expected_result:
        passed = True

    return passed

def test_read_from_file_to_array(filename, expected_result):
    passed = False
    file_contents = ''
    result = ''

    try:
        result = testFile.read_from_file_to_array(filename)

    except Exception as e:
        result = 'YOUR FUNCTION THREW AN UNCAUGHT ERROR: ' + str(e)

    print("Expected Result:", expected_result)
    print("Result:", result)

    if result == expected_result:
        passed = True

    return passed

def test_improved_read_from_file_to_array(filename, expected_result):
    passed = False
    file_contents = ''
    result = ''

    try:
        result = testFile.improved_read_from_file_to_array(filename)

    except Exception as e:
        result = 'YOUR FUNCTION THREW AN UNCAUGHT ERROR: ' + str(e)

    print("Expected Result:", expected_result)
    print("Result:", result)

    if result == expected_result:
        passed = True

    return passed
# END OF TEST FUNCTIONS

# Call to main function (initializes program)
main()

    
