#Jan 3

phonebook = {'Chris': '555-1111', 'Katie': '555-2222', 'Joanne': '555-3333'}
print(phonebook)

if 'Chris' in phonebook:
    print(phonebook['Chris'])

if 'Joanne' not in phonebook:
    print('Joanne is not found.')

test_scores = {'Kayla': [88,98,100], 'Luis': [95,74,81], 'Sophie': [72,88,91], 'Ethan': [70,75,78]}
print(test_scores)


#Creating an empty dictionary
phonebook = {}
phonebook['Chris'] = '555-1111'
phonebook['Katie'] = '555-2222'
phonebook['Joanne'] = '555-3333'
print(phonebook)

#For loop to iterate over a dictionary
phonebook = {'Chris': '555-1111', 'Katie': '555-2222', 'Joanne': '555-3333'}
for key in phonebook:
    print(key)

#Items method
phonebook = {'Chris': '555-1111', 'Katie': '555-2222', 'Joanne': '555-3333'}
for key, value in phonebook.items():
    print(key, value)

#Keys method
for key in phonebook.keys():
    print(key)


#This program uses a dictionary as a deck of cards.
def main():
    #Creating a deck of cards
    #Calls function create_deck
    deck = create_deck()

    #Getting the number of cards to deal
    num_cards = int(input('How many cards should I deal?'))

    deal_cards(deck,num_cards)

def create_deck():
    deck = {'Ace of Spades': 1, '2 of Spades':2, '3 of Spades':3,
        '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
        '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
        '10 of Spades':10, 'Jack of Spades':10,
        'Queen of Spades':10, 'King of Spades': 10,
        'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
        '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
        '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
        '10 of Hearts':10, 'Jack of Hearts':10,
        'Queen of Hearts':10, 'King of Hearts': 10,
        'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
        '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
        '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
        '10 of Clubs':10, 'Jack of Clubs':10,
        'Queen of Clubs':10, 'King of Clubs': 10,
        'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
        '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
        '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
        '10 of Diamonds':10, 'Jack of Diamonds':10,
        'Queen of Diamonds':10, 'King of Diamonds': 10}
    
    return deck

##deal_cards function deals a specified number of cards from the desk
def deal_cards(deck, number):
    ##Initializing an accumulator
    hand_value = 0

    if number > len(deck):
        number = len(deck)

    for count in range(number):
        card, value = deck.popitem()
        print(card)
        hand_value += value

    print('Value of this hand: ', hand_value)

main()

