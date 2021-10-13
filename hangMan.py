import random
def win(guess, word):
  for i in guess:
    if i not in word: return False
  return True

def hangMan():
  words = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
  wordToGuess = list(random.choice(words))
  alreadyGuessed =[]
  strikes = 6
  print("The word is " + str(len(wordToGuess)) + " letters long.")
  while (strikes > 0):
    print("You have this many strikes left: " + str(strikes))
    print("These are the letters you have correctly guessed:")
    print(alreadyGuessed)
    guess = input("Guess a single letter: ").lower()
    if (guess in alreadyGuessed): print("You already guessed this letter, try again.")
    elif (guess in wordToGuess):
      print("You guessed one of the letters!")
      alreadyGuessed.append(guess)
    else:
      print("You guessed a wrong letter.")
      strikes -= 1
    if (win(alreadyGuessed, wordToGuess)): ("Congratulations!  You won!")
  if (strikes == 0): print("You ran out of guesses.  The word was " + "".join(wordToGuess)+".")