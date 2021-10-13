import random
def numberGuessing():
  n = random.randint(0,11)
  correct = False
  while (correct == False):
    guess = int(input("Guess a number between 1 and 10, inclusive: "))
    if(guess >10 or guess< 1): print("You must print a number between 1 and 10, inclusive.")
    if (guess == n): correct = True
    else:
      print("You guessed the wrong number, try again!")
  print("Congratulations, you guessed the correct number!")