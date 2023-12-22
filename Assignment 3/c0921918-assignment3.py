#CSD-1233-01
#Assignment 3
#Romika Chaudhary
#Sept 27, 2023

print ("Answer to multiple choice questions 14 to 22")
#Answer to question 14
print ("Question 14: a")

#Answer to question 15
print ("Question 15: a")

#Answer to question 16
print ("Question 16: c")

#Answer to question 17
print ("Question 17: a")

#Answer to question 18
print ("Question 18: b")

#Answer to question 19
print ("Question 19: a")

#Answer to question 20
print ("Question 20: b")

#Answer to question 21
print ("Question 21: b")

#Answer to question 22
print ("Question 22: b")
print ('\r')


print ("Answer to true or false question number 2")
print ("Question 2: True")
print('\r')


#Programming Assignment
print ("Programming assignment 1")
#Assigning the value of named constant
one_hectare = 10000
#Casting the value of total square meters to float
total_sq_meters = float(input("Please enter the total square meters in a tract of land: "))
#Formula to calculate the number of hectare in a tract of land
num_of_hectare = (1/10000)*total_sq_meters
print ("The total number of hectare in the tract is: ", format(num_of_hectare, '.2f'))
print('\r')


print ("Programming assignment 2")
#Casting the value of food charge to float
food_charge = float(input("Enter the charge for food: "))
#Calculating the amount of tip
amtOfTip = (18/100)*food_charge
#Calculating the amount of HST
amtOfHST = (13/100)*food_charge
total_amt = food_charge + amtOfTip + amtOfHST
print ("The amount of tip is: ", format(amtOfTip, '.2f'))
print ("The amount of HST is: ", format(amtOfHST, '.2f'))
print ("The total amount of meal purchased in a restaurant is: ", format(total_amt, '.2f'))
print('\r')


print ("Programming assignment 3")
#Casting the value of principal to float
principal_amt = float(input("Please enter the amount of principal originally deposited in the account: "))
#Casting the value of interest to int
interest = int(input("Please enter the annual interest rate paid by the account: "))
#Casting the value to integer
num_of_times = int(input("Please enter the number of times per year the interest is compounded: "))
num_of_years = int(input("Please enter the number of years the account will be left to earn interest: "))
#Casting the interest rate to float value
interest_rate = float(interest/100)
#Formula to calculate the amount of money in account after specified number of years
amt_of_money = principal_amt*((1+(interest_rate/num_of_times))**(num_of_times*num_of_years))
print("The amount of money in the account after the specified number of years is: ", format(amt_of_money, '.2f'))





