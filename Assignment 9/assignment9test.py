'''
Test Program for Assignment #9
This program will test your Assignment #9 file
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
import c0921918_assignment9 as testFile #<---- UPDATE THIS TO YOUR FILENAME (DO NOT INCLUDE .PY)

# GLOBAL CONSTANTS

# Maximum scores
MAX_SCORES = [5,5,5,5,5]
MAX_TOTAL = 25

# Test values are stored in a two-dimensional array.
# Outer array is different tests
# Inner array is listed for each

#1: 
TEST_VALUES1 = (('google.coM',True),    
    ('lambtoncollege.ca',False),
    ('.com',True),
    ('\n.COM',True),
    ('com',False)
    )
     

#2: 
TEST_VALUES2 = (
    ("y",True),
    ("yo",False),
    ("YeSsir",True),
    ("Y",True),
    ("yes, please", True)
    )

#3: 
TEST_VALUES3 = (
    ("Hello World", "dlroW olleH"),
    ("c0123", "c0123"),
    ("google.com","google.com"),
    ("Hi.","Hi."),
    ("sdrawrof","forwards")
    )

#4: 
TEST_VALUES4 = PROG4DATA = (
    ("12345", 15),
    ("1 2 3 4 5",-1),
    ("1.25",-1),
    ("0",0),
    ("10",1)
    )

#5:
TEST_VALUES5 = (
    ("06/10/1982","June 10, 1982"),
    ("10/06/1982", "October 06, 1982"),
    ("6/10/1982", "InvalidDate"),
    ("13/12/2000", "InvalidDate"),
    ("11/05/1955", "November 05, 1955")
    )

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
        if testprog1(test_values[0], test_values[1]):
            score += 1
            print("PASS")
        else:
            print("FAIL")

    return score

def test_function_2():
    score = 0
    
    for test_values in TEST_VALUES2:
        if testprog2(test_values[0], test_values[1]):
            score += 1
            print("PASS")
        else:
            print("FAIL")

    return score

def test_function_3():
    score = 0

    for test_values in TEST_VALUES3:
        if testprog3(test_values[0], test_values[1]):
            score += 1
            print("PASS")
        else:
            print("FAIL")

    return score

def test_function_4():
    score = 0

    for test_values in TEST_VALUES4:
        if testprog4(test_values[0], test_values[1]):
            score += 1
            print("PASS")
        else:
            print("FAIL")

    return score

def test_function_5():
    score = 0

    for test_values in TEST_VALUES5:
        if testprog5(test_values[0], test_values[1]):
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
#Program 1 Test
def testprog1(arg1, expected):
    print("arg1:", arg1)
    print("expected:", expected)
    result = testFile.is_com_web(arg1)
    print("result:", result)
    return result == expected

#Program 2 Test
def testprog2(arg1, expected):
    print("arg1:", arg1)    
    print("expected:", expected)
    result = testFile.is_yes(arg1)
    print("result:", result)
    return result == expected

#Program 3 Test
def testprog3(arg1, expected):
    print("arg1:", arg1)    
    print("expected:", expected)
    result = testFile.sdrawkcab(arg1)
    print("result:", result)
    return result == expected

#Program 4 Test
def testprog4(arg1, expected):
    print("arg1:", arg1)
    print("expected:", expected)
    result = testFile.total_digits(arg1)
    print("result:", result)
    return result == expected

#Program 5 Test
def testprog5(arg1, expected):
    print("arg1:", arg1)    
    print("expected:", expected)
    result = testFile.convert_date(arg1)
    print("result:", result)
    return result == expected
# END OF TEST FUNCTIONS

# Call to main function (initializes program)
main()

    
