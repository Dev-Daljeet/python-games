import random

won = False
attempts = 0

def start_game(won, attempts):
    start = int(input("Enter the range\nStart: "))
    end = int(input("End: "))
    rand_num = random.randint(start,end)
    while True:
        try:
            txt = "Guess the number between {0} and {1}: "
            guess = int(input(txt.format(start, end)))
            if guess < start or guess > end:
                raise ValueError("Invalid value! Please enter a number between given range only!")
            if guess == rand_num:
                attempts = attempts + 1
                won = True
                break
            elif guess > rand_num:
                print("Number is lower")
                attempts = attempts + 1
            else:
                print("Number is higher")
                attempts = attempts + 1
            stop = input("Do you want to stop? (\'y\' for stop): ")
            if str(stop) == "y":
                break
        except ValueError as err:
            print("Error occured: "+err) 
    return [won,attempts]
    
won, attempts = start_game(won,attempts)

print("You won! You took "+str(attempts)) if won else print("You quit! Attempts: "+str(attempts))