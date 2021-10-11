import random
def diceRoll():
    max = int(input("Enter the number of faces for this die:"))
    print(f"The die came up {random.randint(1,max)}.")