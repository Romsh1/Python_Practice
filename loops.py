#Dec 23, 2023

#Repition Structures
#Calculating retail price
# mark_up = 2.5
# another = 'y'
# while another == 'y' or another == 'Y':
#     wholesale = float(input("Enter the item's "+"wholesale cost: "))
#     retail = wholesale * mark_up
#     print('Retail price: $', format(retail, '.2f'), sep=' ')
    
#     another = input('Do you have another item? '+ '(Enter y for yes): ')

# mark_up = 2.5
# another = 'y'
# while another == 'y' or another == 'Y':
#     wholesale = float(input("Enter the item's "+"wholesale cost: "))

#     while wholesale < 0:
#         print("ERROR: the cost cannot be negative.")
#         wholesale = float(input("Enter the correct "+"wholesale cost: "))

#         retail = wholesale * mark_up

#         print("Retails price $", format(retail, '.2f'), sep=" ")

#         another = input("Do you have another item? " + '(Enter y for yes):') 

# for seconds in range(60):
#     print(seconds)


# for minutes in range(60):
#     for seconds in range(60):
#         print(minutes, ':', seconds)

# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours, ':', minutes, ':', seconds)

#test_score_averages
# num_students = int(input("How many students do you have? "))
# num_test_scores = int(input("How many test scores per student? "))

# for student in range(num_students):
#     total = 0.0
#     print("Student number", student + 1)
#     print("---------------")

#     for test_num in range(num_test_scores):
#         print("Test number", test_num + 1 , end=" ")
#         score = float(input(': '))
#         total += score

#     average = total / num_test_scores

#     print("The average for student number", student + 1, 'is: ', average)
#     print()


# for row in range(8):
#     for col in range(6):
#         print('*', end=" ")
#     print()

# rows = int(input("How many rows?"))
# cols = int(input("How many columns?"))
# for r in range(rows):
#     for c in range(cols):
#         print('*', end=" ")
#     print()

# rows = 8
# for i in range(rows + 1):
#     for j in range(i):
#         print('*', end=' ')
#     print()

# num_steps = 6
# for r in range(num_steps):
#     for c in range(r):
#         print(' ', end=' ')
#     print('#')

#Programming exercises Chapter 4
#Q14
# rows = 7
# for i in range(rows + 1,0,-1):
#     for j in range(i -1):
#         print('*', end=" ")
#     print()

#Q15
# rows = 6
# for i in range(rows):
#     for j in range(i+1):
#         if i == j:
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# for i in range(1, 7):
#     for j in range(1, 8):
#         if j == i:
#             print("#", end="")
#         else:
#             print(" ", end="")
#     print()


#Q1
# days = 5
# total = 0
# for num in range(5):
#     num_of_bugs = int(input("Enter the number of bugs: "))
#     total += num_of_bugs
# print("The tolal number of bugs collected in ", days, " days are ",total)

#Q2
# calories_burn_per_min = 4.2
# minutes = 5
# num = 31

# for j in range(10,num,5):
#     burned_calories = j * calories_burn_per_min
#     print("The calories burned in ", j, " minutes is", burned_calories,)
# print()

#Q3
# total = 0
# lap_time = []
# run_times = int(input("Enter the number of times you have run around a racetrack: "))
# for i in range(1,run_times+1):
#     time = float(input("Enter the lap time for lap "))
#     lap_time.append(time)
#     total += time
# avg = total / run_times
# fastest_lap = max(lap_time)
# slowest_lap = min(lap_time)
# print("The slowest lap time is ", slowest_lap)
# print("The fastest lap time is ", fastest_lap)
# print("The average lap time for ", run_times, "lap round is ", avg)

# Ask the user to enter the number of laps
# num_laps = int(input("Enter the number of laps you've run around the racetrack: "))

# Initialize variables to track lap times
# lap_times = []
# total_time = 0

# Loop to input lap times
# for lap in range(1, num_laps + 1):
#     time = float(input(f"Enter the time for lap {lap} (in seconds): "))
#     lap_times.append(time)
#     total_time += time

# Calculate fastest, slowest, and average lap times
# fastest_lap = min(lap_times)
# slowest_lap = max(lap_times)
# average_lap = total_time / num_laps

# Display results
# print(f"\nFastest lap time: {fastest_lap} seconds")
# print(f"Slowest lap time: {slowest_lap} seconds")
# print(f"Average lap time: {average_lap} seconds")


#Q4
# speed = float(input("Enter the speed of a vehicle: "))
# hrs_traveled = int(input("Enter the number of hours traveled: "))

# print("Hour\tDistance Traveled")
# print("-----------------------")
# for i in range(1,hrs_traveled + 1):
#     distance = speed * i
#     print(f"{i}\t\t{distance}")
# print()


#Q5
# total_inch = 0.0
# total_month = 12

# num_of_yrs = int(input("Enter the number of years: "))
# for yrs in range(1, num_of_yrs + 1):
#     for months in range(1, total_month + 1):
#         inches = float(input(f"Enter the inches of rainfall for month {months}: "))
#         total_inch += inches

# num_of_months = total_month * num_of_yrs
# average_rainfall = total_inch / num_of_months
# print("The number of months is ",num_of_months)
# print("The total inches of rainfall ", total_inch)
# print("The average rainfall per month for the entire period is ", average_rainfall)


#Q6
# mile = 1.60934 #in kilometers
# max_limit = 80
# print("Miles\tEquivalent Distances")
# print("--------------------------------------")
# for i in range(10, max_limit + 1, 10):
#     conversion = i * mile
#     print(i, '\t', format(conversion, '.2f'))
    # print(format(conversion, '.2f'))
# print()

#Q7
# salary = 0
# num_of_days = int(input("Enter the number of days: "))
# print("Days\t\tSalary")
# for i in range(1, num_of_days + 1):
#     calc_salary = 2 * (i - 1)
#     salary += calc_salary
#     print(f"{i}\t${calc_salary / 100:.2f}")
# total_pay_dollars = salary / 100
# print(total_pay_dollars)
# print()

# def calculate_salary():
#     days = int(input("Enter the number of days: "))
#     total_pay = 0
#     print("Day\tSalary")
    
#     for day in range(1, days + 1):
#         salary = 2 ** (day - 1)  # Calculate the salary for the current day
#         total_pay += salary
#         print(f"{day}\t${salary / 100:.2f}")  # Convert salary from pennies to dollars
    
#     total_pay_dollars = total_pay / 100  # Convert total pay from pennies to dollars
#     print(f"\nTotal pay over {days} days: ${total_pay_dollars:.2f}")

# calculate_salary()

