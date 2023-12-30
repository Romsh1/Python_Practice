#CSD-1233-01
#Assignment 5
#Romika Chaudhary
#18 Oct, 2023

#Programming exercises question number 2
print("Programming solution to question number 2")

calories_burned_per_minute = 4.2

# Displays calorie burned for each minute specified
for minutes in [10, 15, 20, 25, 30]:
    caloriesBurned = calories_burned_per_minute * minutes
    print(f"Calories burned in {minutes} minutes: {caloriesBurned}")



print("")
#Programming exercises question number 12
print("Programming solution to question number 12")

#Defining a factorial function
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

#Taking user input
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
    print(f"The factorial of {n} is: {factorial(n)}")



print("")
#Programming exercises question number 14
print("Programming solution to question number 14")

rows=7
#Handles number of rows, along with decrement by 1
for i in range(rows,0,-1):
#print '*' according to the current value of i 
    for j in range(i):
        print('*', end='')
    print()


