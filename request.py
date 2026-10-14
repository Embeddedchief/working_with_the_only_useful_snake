#Ask user to roll a dice {(y/n) option}
#if user enters y
    #generate two random numbers
    #print the numbers
#if user enters n
    #print thanks for playing
    #exit
#if user input is neither y nor n


def diceRoll():
    while True:
        response = input('Roll the dice? (y/n): ').lower
        # valid_options = ('y', 'n')
        if response == 'y':
            # random
            print('1','3')
            continue
        elif response == 'n':
            print('Thanks for playing!')
            break
        else:
            print('Invalid option, pick y/n:')
            continue
    