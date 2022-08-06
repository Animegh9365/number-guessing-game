#find a random number
from random import randint

HARD_NO_TURNS=10
EASY_NO_TURNS=5


#checking the guessing number if it is right
def checkanswer(guess,answer,turns):
    """checks answer against guess, and returns number of turns remaining"""
    if (guess == answer):
        print(f"you win! your answer {answer} is right")
    elif(guess > answer):
        print("Too high")
        return turns-1
    else:
        print("Too low")
        return turns-1


#setting the difficulty level of the game
def difficulty():
    level = input("Choose the difficulty level, type hard or easy:")
    if level=="hard":
        return HARD_NO_TURNS
    else:
        return EASY_NO_TURNS

#choosing a random number between 1 and 100
def game():
    print("Welcome to the number guessing game")
    print("I am thinking of a number between 1 and 100")
    answer = randint(1,100)
    print(f"the correct answer is {answer}")
    turns = difficulty()
    

    guess=0
    #looping the game for getting the correct answer
    while guess != answer:
        print(f"you have {turns} of attempts remaining to guess the number")
        #guessing the random number
        guess = int(input("Make a guess:"))
        turns = checkanswer(guess,answer,turns)
        
        if turns ==0:
            print("you are out of attempts, you loose!")
            return
        elif guess !=answer:
            print("Guess again")

game()
#track the number of turns, reduce by 1 if they are wrong
