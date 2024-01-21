#Test 2 Function Testing
# IMPORTS
import c0921918_test2 as testFile #<---- UPDATE THIS TO YOUR FILENAME (DO NOT INCLUDE .PY)


FUNCT1DATA = (
    (19,9,[2.111111111111111, 2, 1]),    
    (20,7,[2.857142857142857, 2, 6]),
    (5,3,[1.6666666666666667, 1, 2]),
    (100,10,[10.0, 10, 0]),
    (1,1,[1.0, 1, 0])
     )

FUNCT2DATA = (
    (100,"100.00"),
    (15300,"15,300.00"),
    (1.23456,"1.23"),
    (2345.6789,"2,345.68"),
    (1234567.239,"1,234,567.24")
    )

FUNCT3DATA = (
    ("test", ["test","me","out"], True),
    ("test", ["TEST","me","out"], True),
    ("test", ["not","in","here"], False),
    ("test", ["bad","test",10], False),
    ("test", ["t3st","me","out"], False)
    )

FUNCT4DATA = (
    ("Passw0rd", True),
    ("Pass w0rd", False),
    ("Pa55", False),
    ("passw0rd", False),
    ("Passw0rd;", False)
    )

FUNCT5DATA = (
    ("Hello", ['....','.','.-..','.-..','---']),
    ("WorLd", ['.--','---','.-.','.-..','-..']),
    ("Hello World", ['....','.','.-..','.-..','---',' ','.--','---','.-.','.-..','-..']),
    ("Invalid1?", ['..','-.','...-','.-','.-..','..','-..','.----','..--..']),
    ("Invalid!", [])    
    )

#Main Function
def test_my_functions():
    
    progscore = 0
    finalscore = 0
    progpass = [False, False, False, False, False]
    #Test program 1
    print ("\nProgram 1:")
    try:
        for item in FUNCT1DATA:
            if testprog1(item[0], item[1], item[2]):
                progscore += 2
                finalscore += 2
                print("PASSED")
            else:
                print("FAILED")
    except:
        print('Fatal Exception in Program 1')
        
    print('Program 1 score:',progscore,'//',len(FUNCT1DATA) *2)
    if progscore == len(FUNCT1DATA):
        progpass[0] = True
    

    #reset program score
    progscore = 0         

    #Test program 2
    print ("\nProgram 2:")
    try:
        for item in FUNCT2DATA:
            if testprog2(item[0], item[1]):
                progscore += 2
                finalscore += 2
                print("PASSED")
            else:
                print("FAILED")
    except:
        print('Fatal Exception in Program 2')
        
    print('Program 2 score:',progscore,'//',len(FUNCT2DATA) *2)
    if progscore == len(FUNCT2DATA):
        progpass[1] = True

    #reset program score
    progscore = 0 
    
    #Test program 3
    print ("\nProgram 3:")
    try:
        for item in FUNCT3DATA:
            if testprog3(item[0], item[1], item[2]):
                progscore += 2
                finalscore += 2
                print("PASSED")
            else:
                print("FAILED")
    except:
        print('Fatal Exception in Program 3')
        
    print('Program 3 score:',progscore,'//',len(FUNCT3DATA) *2)
    if progscore == len(FUNCT3DATA):
        progpass[2] = True

    #reset program score
    progscore = 0 

    #Test program 4
    print ("\nProgram 4:")
    try:
        for item in FUNCT4DATA:
            if testprog4(item[0], item[1]):
                progscore += 2
                finalscore += 2
                print("PASSED")
            else:
                print("FAILED")
    except:
        print('Fatal Exception in Program 4')

    print('Program 4 score:',progscore,'//',len(FUNCT4DATA) *2)
    if progscore == len(FUNCT4DATA):
        progpass[3] = True

    #reset program score
    progscore = 0 

    #Test program 5
    print ("\nProgram 5:")
    try:
        for item in FUNCT5DATA:
            if testprog5(item[0], item[1]):
                progscore += 2
                finalscore += 2
                print("PASSED")
            else:
                print("FAILED")

    except:
        print('Fatal Exception in Program 5')
        
    print('Program 5 score:',progscore,'//',len(FUNCT5DATA) *2)
    if progscore == len(FUNCT5DATA):
        progpass[4] = True        

    print ('\nTotal Score:',finalscore,"/ 50")

    


#Program 1 Test
def testprog1(arg1, arg2, expected):
    print("arg1:", arg1)
    print("arg2:", arg2)    
    print("expected:", expected)
    result = testFile.divide_me(arg1, arg2)
    print("result:", result)
    return result == expected

#Program 2 Test
def testprog2(arg1, expected):
    print("arg1:", arg1)    
    print("expected:", expected)
    result = testFile.format_currency(arg1)
    print("result:", result)
    return result == expected

#Program 3 Test
def testprog3(arg1, arg2, expected):
    print("arg1:", arg1)
    print("arg2:", arg2)    
    print("expected:", expected)
    result = testFile.validate_input(arg1, arg2)
    print("result:", result)
    return result == expected

#Program 4 Test
def testprog4(arg1, expected):
    print("arg1:", arg1)    
    print("expected:", expected)
    result = testFile.validate_password(arg1)
    print("result:", result)
    return result == expected

#Program 5 Test
def testprog5(arg1, expected):
    print("arg1:", arg1)    
    print("expected:", expected)
    result = testFile.morse_code(arg1)
    print("result:", result)
    return result == expected




if __name__ == "__main__":
    test_my_functions()
