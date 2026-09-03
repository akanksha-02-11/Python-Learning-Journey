# f = open("poem.txt")
# content = f.read()              #problem no 9
# if("twinkle" in content):
#    print("The word twinkle is present in the content")

# else:
#    print("The word twinkle is not present in the content")
# f.close()
import random

def game():
   print("You are the game..")
   score = random.randint(1,65)
   print(f"Your score: {score}")
game()

