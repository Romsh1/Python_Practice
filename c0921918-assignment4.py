#CSD-1223-02
#Assignment-4
#Romika Chaudhary
#11 Oct, 2023

#Programming Question 1
print("Programming solution to question 1")

#Asking user input for the value of 1s, 2s, 3s, 4s, 5s, 6s
ones = int(input("How many ones did you score? "))
twos = int(input("How many twos did you score? "))
threes = int(input("How many threes did you score? "))
fours = int(input("How many fours did you score? "))
fives = int(input("How many fives did you score? "))
sixs = int(input("How many sixs did you score? "))

#calculating score of 1s, 2s. 3s. 4s. 5s. 6s
ones_score = 1 * ones
twos_score = 2 * twos
threes_score = 3 * threes
fours_score = 4 * fours
fives_score = 5 * fives
sixs_score = 6 * sixs

#Calculating total score
total_score = ones_score + twos_score + threes_score + fours_score + fives_score + sixs_score
print("Your subtotal is ", total_score)

#Applying condition for bonus points
if (total_score >= 63):
    #Adding 35 as bonus points in total score
    subTotal = total_score + 35;
    print("You earned a bonus.")
    #Printing sub total after adding bonus points
    print("Your total is ", subTotal, ".")

else:
    print("You did not earn a bonus.")
    print("Your total is ", total_score, ".")


#Programming Question 2
print("\r")
print("Programming solution to question 2: ")
print("\r")

#Asking user input for grade percentage
percentage = int(input("Enter your grade percentage: "))

#Displaying grade points according to the grade percentage value entered by the user 
if (percentage > 100):
    print("The number is too high.")

elif (percentage < 0):
    print("The number cannot be negative.")

elif (percentage >= 94 and percentage <= 100):
    print("Your GPA is 4.")

elif (percentage >= 87 and percentage <= 93):
    print("Your GPA is 3.7")

elif (percentage >= 80 and percentage <= 86):
    print("Your GPA is 3.5")

elif (percentage >= 77 and percentage <= 79):
    print("Your GPA is 3.2")

elif (percentage >= 73 and percentage <= 76):
    print("Your GPA is 3")

elif (percentage >= 70 and percentage <= 72):
    print("Your GPA is 2.7")

elif (percentage >= 67 and percentage <= 69):
    print("Your GPA is 2.3")

elif (percentage >= 63 and percentage <= 66):
    print("Your GPA is 2")

elif (percentage >= 60 and percentage <= 62):
    print("Your GPA is 1.7")

elif (percentage >=50 and percentage <= 59): 
    print("Your GPA is 1")

elif (percentage >=0 and percentage <= 49):
    print("Your GPA is 0")   





