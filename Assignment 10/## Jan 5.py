## Jan 5
## Classes and OOPs

#Creating a coin class
import random

class coin:
    def __init__(self):
        self.sideup = 'Heads'

    ## The toss method generates a random number
    ## in the range of 0 through 1. If the number
    ## is 0, then sideup is set to 'Heads'.
    ## Otherwise, sideup is set to 'Tails'.

    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    def get_sideup(self):
        return self.sideup 

def main():
    my_coin = coin()

    print('This side is up:', my_coin.get_sideup())

    print('I am tossing the coin ...')
    my_coin.toss()

    print('This side is up:', my_coin.get_sideup())

main()


#Classes and Objects
class Person:
    name = "Harry"
    occupation = "Software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()
c = Person()

a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Amanu"
b.occupation = "Software Engineer"

c.name = "Karinu"
c.occupation = "Doctor"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()


#Constructor
class Person():
    #Special method that helps in making a constructor
    def __init__(self, n, o):
        print("Hey I am a person")
        self.name = n
        self.occupation = o

    def info(self):
        print(f"{self.name} is a {self.occupation}")

#Creating an object
# a and b is passed to self automatically
a = Person("Harry", "Developer")
b = Person("Divya", "Hr")
print(a.name)
a.info()
b.info()


# DECORATORS
print("decorator")