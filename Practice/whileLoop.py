#number = int(input("Enter a number: "))
#while (number <= 5):
 #   print("Hello")
 #   number +=1

#positiveInteger = int(input("Please enter a positive integer: "))
#while(positiveInteger > 0 ):
 #   positiveInteger = int(input("Please enter a positive integer: "))

#for i in range(10):
 #   print (i)

total = 0
count = 8
max = flaot(input("Enter the maximum amount you want to spend: "))
for ( count, count<11, count++ ):
    cost = float(input("Enter the cost of an item: "))
    total = total + cost
    if total > max:
        print("You have reached your spending limit.")
        print("You cannot buy this item or anything else.")
        total = total - cost
    else:
        print("You have bought ", count, " items.")
print("Your total cost is ", cost)



