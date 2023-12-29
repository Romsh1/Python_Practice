#Dec 28
#Function

def greet():
    print("Hello")
    print("Good Morning")
greet()

def greet(name):
    print("Hello", name)
    print("Good Morning")
greet("Jack")


def add_numbers(n1,n2):
    result = n1 + n2
    return result
number1 = 7.8
number2 = 9.0
result = add_numbers(number1, number2)
print("The sum is", result)


#Function to find average marks
def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    average_marks = sum_of_marks / total_subjects
    return average_marks

def compute_grade(average_marks):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return grade

marks = [55,64,75,80,65]
average_marks = find_average_marks(marks)
print("Your average marks is", average_marks)

grade = compute_grade(average_marks)
print("Your grade is", grade)


def add_numbers(n1, n2):
    sum = n1 + n2
    return sum
result = add_numbers(5.4,6.7)
print("The sum is", format(result, '.2f'))


#Providing default value
def add_numbers(n1 = 100, n2 = 1000):
    sum = n1 + n2
    return sum
result = add_numbers(10.98)
print("The sum is", format(result, '.2f'))


def message():
    print("I am Arthur,")
    print("King of the Britons.")

main()

def main():
    startup_message
    input("Press Enter to see Step 1.")
    step1()
    input("Press enter to see Step 2.")
    step2()
    input("Press enter to see step 3")
    step3()
    input("Press enter to see step 4")
    step4()


def startup_message():
    print("This program tells you how to")
    print("disassemble an ACME laundry dryer.")
    print("There are 4 steps in the process.")
    print()

def step1():
    print("Step 1: Unplug the dryer and ")
    print("move it away from the wall.")
    print()

def step2():
    print("Step 2: Remove the six screws")
    print("from the back of the dryer.")
    print()

def step3():
    print("Step 3: Remove the back panel")
    print("from the dryer.")
    print()

def step4():
    print("Step 4: Pull the top of the")
    print("dryer straight up.")

main()

#Program to convert cups to fluid ounces
def main():
    intro()
    cups_needed = int(input("Enter the number of cups: "))
    cups_to_ounces(cups_needed)


def intro():
    print("This program converts measurements")
    print("in cups to fluid ounces. For your")
    print("reference the formula is:")
    print("1 cup = 8 fluid ounces")
    print()

def cups_to_ounces(cups):
    ounces = cups * 8
    print("That converts to", ounces, "ounces.")

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    addMe(num1, num2)

def addMe(num1, num2):
    sum = num1 + num2
    print("The sum of given two number is: ",sum)

#Passing multiple arguments
def main():
    print("The sum of 12 and 45 is")
    show_sum(12,45)

def show_sum(num1, num2):
    result = num1 + num2
    print(result)

main()

#Passing two strings
def main():
    str1 = input("Enter your first name: ")
    str2 = input("Enter your last name: ")
    print("Your name is: ")
    concatStr(str1, str2)


def concatStr(str1, str2):
    print(str1, str2)

main()

def main():
    value = 99
    print("The value is", value)
    change_my(value)
    print("Back in main the value is", value)

def change_my(arg):
    print("I am changing the value.")
    arg = 0
    print("Now the value is", arg)

main()

def main():
    show_interest(rate = 0.01, periods=10, principal=10000.0)

def show_interest(principal, rate, periods):
    interest = principal * rate * periods
    print("The simple interest will be $", format(interest, ',.2f'), sep='')

main()

#Learning about global variable
my_value = 10
def main():
    print(my_value)

main()

number = 0
def main():
    global number
    number = int(input("Enter a number: "))
    show_number()

def show_number():
    print("The number you entered is", number)

main()

#Global Constants
contribution_rate = 0.05

def main():
    gross_pay = float(input("Enter the gross pay: "))
    bonus = float(input("Enter the amount of bonuses: "))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)

def show_pay_contrib(gross):
    contrib = gross * contribution_rate
    print("Contribution for gross pay: $", format(contrib, '.2f'), sep='')

def show_bonus_contrib(bonus):
    contrib = bonus * contribution_rate
    print("Contribution for bonuses: $", format(contrib, '.2f'), sep='')

main()

#Random numbers
import random

def main():
    number = random.randint(1, 10)
    print("The number is ", number)

main()
def main():
    for count in range(15):
        number = random.randint(1, 100)
        print(number)
main()

min = 1
max = 6

def main():
    again = 'y'

    while again == 'y' or again == 'Y':
        print("Rolling the dice.....")
        print("Their values are: ")
        print(random.randint(min, max))
        print(random.randint(min,max))

        again = input("Roll them again? (y=yes):")

main()

Heads and Tails

HEADS = 1
TAILS = 2
TOSSES = 10

def main():
    for toss in range(TOSSES):
        if random.randint(HEADS,TAILS) == HEADS:
            print('Heads')
        else:
            print('Tails')
main()
import random

number = random.randrange(0,101,10)


def get_regular_price():
    price = float(input("Enter the item's regular price: "))
    return price
reg_price = get_regular_price()

discount_percentage = 0.20

def main():
    reg_price = get_regular_price()

    sale_price = reg_price - discount(reg_price)

    print("The sale price is $", format(sale_price, '.2f'), sep='')

def get_regular_price():
    price = float(input("Enter the item's regular price: "))
    return price

def discount(price):
    return price * discount_percentage

main()

#Q1
def shout(str1):
    upperName = str1.upper()
    print(upperName)

name = input("Enter your name: ") + '!'
shout(name)

