# Dice Rolling Simulator
# Room 5 - David Osei Antwi, Deirdre Boland, Nora Ishmael, Daniel Popowych Jan 2025

# import random function
import random
 
# randomly roll dice function
# function randomly grabs number within range
# setting default values with the random roll function
def get_roll(min_roll=1,max_roll=6):
    """ Rolls a dice between 1 and 6 """
    dice_roll = random.randint(min_roll,max_roll)
    # print what number is
    print(f"You rolled a {dice_roll}")
 
# run function
get_roll()
 
# ask if you'd like to roll again
while True:
   user_input = input("Would you like to roll again? - yes/no: ").lower()
   if user_input == "yes":
      get_roll()
   elif user_input == "no":
      print("Thanks for playing!")
      break
   else:
      print("Incorrect entry - please enter yes or no.")