import random

n = random.randint(1,10)
guess = 5

print("Let' Play Guess The Number")

input()

print(":: Here's The Rule are ::")
input()

print("I will think about any Number between (1 to 10) you have to guesss it")
input()

print("You have Only 5 Guesses USE it carefully")
input()


print("::::Let's start now::::")

while guess!=0:
    print("Guess")
    
    
    yourGuess = input()
    if yourGuess.isnumeric()  and int(yourGuess) <= 10:
        yourGuess = int(yourGuess)
    else:
        print("Yo Bruv put a Number innit of Range (1 - 10)")
        input()
        guess = guess+1
        
    if yourGuess == n:
        print(":::: You've Won Congratulation ::::")
        break
    guess = guess-1
else:
    print("::::You are a LOSER::::")