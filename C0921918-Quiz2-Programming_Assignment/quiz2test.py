# Quiz 2 Tests
# Tests the function required for Quiz 2
import C0921918quiz2 as testFile

def test_my_function():
    # Initialize score accumulator to 0
    score = 0

    # Sequence of sequences - test arguments and expected results
    TEST_DATA = (
        (['foo',3,7.5],[['foo'],[3],[7.5]]),        
        ([1.0,'foo',3,'bar',9,7.5], [['foo','bar'],[3,9],[1.0,7.5]]),
        ([1.0,'foo','3','bar',9,7.5],[['foo','3','bar'],[9],[1.0,7.5]]),
        (('bar',3,7.5),[['bar'],[3],[7.5]]),
        ((1.0,'foo','bar','7.5'), [['foo','bar','7.5'],[],[1.0]])
        )

    # Loop through test data and test
    for test in TEST_DATA:
        testarg = test[0]
        expected = test[1]

        # Print test data
        print("Test argument:", testarg)
        print("Expected result:", expected)

        # Get result and print
        result = testFile.sort_str_int_float_list(testarg)
        print("Result:",result)

        # If expected result, add 5 to score
        if result == expected:
            score += 5
            print ("Passed.")
        else:
            print ("Failed.")

    # Output final score
    print("Score:",score)


test_my_function()    
    

    

