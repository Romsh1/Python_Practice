#CSD-1233-01
#Assignment 6
#Romika Chaudhary
#November 08,2023

#Function for calculating total meal amount
def calc_total_meal_amt():
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


#Function for calculating hectares in a tract of land
def calc_hectares():
    one_hectare = 10000
    #Casting the value of total square meters to float
    total_sq_meters = float(input("Please enter the total square meters in a tract of land: "))
    #Formula to calculate the number of hectare in a tract of land
    num_of_hectare = (1/10000)*total_sq_meters
    print ("The total number of hectare in the tract is: ", format(num_of_hectare, '.2f'))
    print('\r')

#Function for calculating Compound Interest
def calc_compound_interest():
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



#Function for displaying menu and handling user's choice
def menu():
    print("Menu:")
    print("1. Calculate total meal amount")
    print("2. Calculate hectares in a tract of land")
    print("3. Calculate compound interest")
    choice = input("Enter your choice (1, 2, or 3): ")
    while choice not in ['1', '2', '3']:
        print("Invalid choice. Please enter 1, 2, or 3.")
        choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        calc_total_meal_amt()
    elif choice == '2':
        calc_hectares()
    elif choice == '3':
        calc_compound_interest()


#Main Function
def main():
    while True:
        menu()
        another_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if another_calculation.lower() != 'yes':
            print("Thank you for using the program. Goodbye!")
            break


#Calling the main function
if __name__ == "__main__":
    main()
