#CSD-1233-01
#Test 1
#Romika Chaudhary
#Oct 19, 2023


#Declaring named constants 
MIN_GRADE = 0
MAX_GRADE = 100
DEAN_LIST_BOUNDARY = 90
PASS_LIST_BOUNDARY = 60


#Initializing accumulator
total_grade = 0
num_of_courses = 0


#Asking user input for the number of courses to average
no_courses_to_average = int(input("Please enter the number of courses to average: "))
 

#Looping the program to specified number of times
for i in range(no_courses_to_average):
    while True:
        #Asking the user to enter for grade in terms of percentage
        grade = float(input("Please enter the grade (as a percentage): "))

        #Verifying if the user have entered the grade value within valid range
        if MIN_GRADE <= grade <= MAX_GRADE:
            break
        else:
            print("Error! Grade must be between 0 and 100. Please Try Again.")
 
#Adding the grade and courses to the accumulator
total_grade += grade
num_of_courses += 1
 
#Formula to calculate the average grade
avg_grade = total_grade / num_of_courses
 
# Displaying the average grade
print(f"Average Grade: {avg_grade:.2f}%")

# Displaying a message based on the average grade
if avg_grade >= DEAN_LIST_BOUNDARY:
    print("Student has made the Dean's List")
elif avg_grade >= PASS_LIST_BOUNDARY:
    print("Student has passed the program")
else:
    print("Student has not passed")
