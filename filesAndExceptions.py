#Dec 26
#Files and Exceptions

#Opening a file
file_var = open(filename, mode)

#Writing data to a file (Calling the write method)
file_var.write(string)

def main():
    outfile = open('philosophers.txt', 'w')

    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    outfile.Close()

main()

#Reading data from a file
def main():
    infile = open('philosophers.txt', 'r')

    file_content = infile.read()

    infile.Close()

    print(file_content)
main()

def main():
    infile = open('philosophers.txt', 'r')

    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    infile.close()

    print(line1)
    print(line2)
    print(line3)
main()

def main():
    print("Enter the names of three friends.")
    name1 = input("Friend #1: ")
    name2 = input("Friend #2: ")
    name3 = input("Friend #3: ")

    myfile = open('friends.txt', 'w')

    myfile.write(name1 + '\n')
    myfile.write(name2 + '\n')
    myfile.write(name3 + '\n')

    myfile.close()
    print("The names were written to friends.txt")

main()

name = 'Joanne Manchester\n'
name = name.rstrip('\n')

def main():
    infile = open('philosophers.txt', 'r')

    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')

    infile.close()

    print(line1)
    print(line2)
    print(line3)
main()

def main():
    myfile = open('friends.txt', 'a')
    myfile.write('Matt\n')
    myfile.write('Chris\n')
    myfile.write('Suze\n')
    myfile.close()
main()


#Converting numbers to strings before they are written to a text file
def main():
    infile = open('numbers.txt', 'w')

    #Asking user input 
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))

    infile.write(str(num1) + '\n')
    infile.write(str(num2) + '\n')
    infile.write(str(num3) + '\n')

    infile.close()
    print("Data written to numbers.txt")
main()


#Demonstrating how numbers that are read from a file must be converted from strings before 
#they are used in a math operation
def main():
    infile = open('numbers.txt', 'r')

    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())

    infile.close()

    total = num1 + num2 + num3

    print('The numbers are: ', num1, num2, num3)
    print('Their total is: ', total)
main()


#Using loops to process files
def main():
    # Get the number of days.
    num_days = int(input('For how many days do ' + 'you have sales? '))
# Open a new file named sales.txt.
    sales_file = open('sales.txt', 'w')

    # Get the amount of sales for each day and write
    # it to the file.
    for count in range(1, num_days + 1):
    # Get the sales for a day.
        sales = float(input('Enter the sales for day #' + str(count) + ': '))
        # Write the sales amount to the file.
        sales_file.write(str(sales) + '\n')


   # Close the file.
    sales_file.close()

    print('Data written to sales.txt.')

  # Call the main function.
main()

def main():
    sales_file = open('sales.txt', 'r')

    line = sales_file.readline()

    while line != '':
        #Convert amount to a float
        amount = float(line)

        print(format(amount, '.2f'))

        line = sales_file.readline()
    sales_file.close()
main()

#This program saves a sequence of video running times
#to the video_times.txt file.

def main():
    num_videos = int(input("How many videos are in the project? "))

    video_file = open('video_times.txt', 'w')

    print('Enter the running times for each video.')
    for count in range(1, num_videos + 1):
        run_time = float(input('Video #' + str(count) + ': '))
        video_file.write(str(run_time) + '\n')

    video_file.close()
    print('The times have been saved to video_times.txt')
main()


#This program the values in the video_times.txt
#file and calculates their total.
def main():
    video_file = open('video_times.txt', 'r')

    total = 0.0

    count = 0

    print('Here are the running times for each video: ')

    for line in video_file:
        run_time = float(line)
        count += 1
        print('Video #', count, ': ', run_time, sep='')

        total += run_time
    video_file.close()

    print('The total running time is', total, 'seconds.')
main()

