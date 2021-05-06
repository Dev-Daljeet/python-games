import random

score = 0
moves = ["Rock","Paper","Scissors"]

def start_game():
    try:
        while True:
            global score
            comp_move = random.randint(0,2)
            user_move = int(input("Please select your move:\n1 for Rock\n2 for Paper\n3 for Scissors\n"))
            if user_move not in [1,2,3]:
                raise ValueError("Invalid value")
            user_move = user_move - 1
            #Draw! Same moves like User move: Rock and Comp move: Rock
            if user_move == comp_move:
                print("Draw! The computer chose "+moves[comp_move]+". You chose "+moves[user_move])
            #User move: Rock and Comp move: Scissors
            elif user_move == 0 and comp_move == 2:
                print("You won! The computer chose "+moves[comp_move]+". You chose "+moves[user_move])
                score = score + 1
            #User move: Paper and Comp move: Rock
            elif user_move == 1 and comp_move == 0:
                print("You won! The computer chose "+moves[comp_move]+". You chose "+moves[user_move])
                score = score + 1
            #User move: Scissors and Comp move: Paper
            elif user_move == 2 and comp_move == 1:
                print("You won! The computer chose "+moves[comp_move]+". You chose "+moves[user_move])
                score = score + 1
            #Rest of the moves that result in defeat
            else:
                print("You lost! The computer chose "+moves[comp_move]+". You chose "+moves[user_move])
            stop = input("Do you want to stop? (\'y\' for stop)")
            if str(stop) == "y":
                break
    except ValueError as err:
        print("Error occured! "+err)
 
start_game()
result = "Your score: {0}"
print(result.format(score))