'''
Test Program for Assignment #8
This program will test your Assignment #8 file
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
import assignment8 as testFile #<---- UPDATE THIS TO YOUR FILENAME (DO NOT INCLUDE .PY)

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
TEST_VALUES1 = (
    (7,9,16),    
    (1.5,2.9,4.4),    
    ('Hello ','World!','Hello World!'),
    ([1,2,3],[4,5],[1,2,3,4,5]),
    (('A','B'),('C',),('A','B','C'))
     )

#2: filename, text written/appended, expected value returned by function, contents after writing/appending
TEST_VALUES2 = (
    ([3,9,12],24),
    ((1,2,3),6),
    ([0.0,-1.5,5.0],3.5),
    ((1.3,2.4,10.0), 13.7),    
    (['Monty ','Python''s ','Flying ','Circus'], 'Monty Python''s Flying Circus')
    )

#3 filename, expected contents returned by function
TEST_VALUES3 = (
    ([1,3,10,20], [[1,3],[10,20]]),
    ((1,5,7), [(1,5),(7,)]),
    (["Split","These","Four","Up"], [["Split","These"],["Four","Up"]]),
    ([18,7,100,2], [[18,7],[100,2]]),
    ((99,"String",7), [(99,"String"),(7,)])
    )

#4 filename, expected contents returned by function
TEST_VALUES4 = PROG4DATA = (
    ([1,3,5],100,[1,3,5]),
    ([2,4,6,8],6,[2,4,8]),
    ([1,3,5,3,7,3],3,[1,5,3,7,3]),
    (["These","Don't","Work"],"Don't",["These","Work"]),
    (["Please","Don't","Say","Please","Twice"],"Please",["Don't","Say","Please","Twice"])
    )

#4 filename, expected contents returned by function
TEST_VALUES5 = (
    ([10,1,99,50],(1,99)),
    ((100,2, 3), (2,100)),
    (("Which","Words","Are","Least","And","Greatest"), ("And","Words")),
    ((1, 1), (1, 1)),
    (("!", "@", "#", "$", "%", "\n"), ("\n","@"))
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
        if testprog1(test_values[0], test_values[1], test_values[2]):
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

    file_obj = open(TEST_FILENAME + ".txt", "w")
    file_obj.write(TEST_FILE_CONTENT)
    file_obj.close()

    for test_values in TEST_VALUES3:
        if testprog3(test_values[0], test_values[1]):
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
        if testprog4(test_values[0], test_values[1], test_values[2]):
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
def testprog1(arg1, arg2, expected):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("expected:", expected)
    result = testFile.add_two(arg1, arg2)
    print("result:", result)
    return result == expected

#Program 2 Test
def testprog2(arg1, expected):
    print("arg1:", arg1)    
    print("expected:", expected)
    result = testFile.seq_total(arg1)
    print("result:", result)
    return result == expected

#Program 3 Test
def testprog3(arg1, expected):
    print("arg1:", arg1)    
    print("expected:", expected)
    result = testFile.seq_split(arg1)
    print("result:", result)
    return result == expected

#Program 4 Test
def testprog4(arg1, arg2, expected):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("expected:", expected)
    result = testFile.safe_list_remove(arg1, arg2)
    print("result:", result)
    return result == expected

#Program 5 Test
def testprog5(arg1, expected):
    print("arg1:", arg1)    
    print("expected:", expected)
    result = testFile.seq_min_max(arg1)
    print("result:", result)
    return result == expected
# END OF TEST FUNCTIONS

# Call to main function (initializes program)
main()

    
