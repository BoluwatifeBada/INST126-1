# create function to roll
# check if they tuple out
# if tupled, player's turn ends with zero points
# if two are the same, they are fixed and cant be rerolled
# function for if player wants to stop, add up scores
# use loop to give players turn until they reach target score
import random

# create function to give players an introduction
def introduction():
    print("Welcome to the Tuple out Dice Game")
    print("Rules:")
    print("1. The object of the game is to score the most points or reach the target score first.")
    print("2. Players take turns rolling three dice.")
    print("3. If all three dice are the same, you 'tuple out' and score 0 points for the turn.")
    print("4. If two dice are the same, they are 'fixed' and cannot be rerolled.")
    print("5. You can reroll non-fixed dice as often as you want or stop to score points.")
    print("6. When you stop, your score is the total of all three dice.")
    print("7. The game ends when a player reaches the target score and wins.")

# function to roll all 3 dice and return their values as a list
def roll_dice():
    # roll the three dice
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    die3 = random.randint(1,6)

# store the value of the dice in a list
    dice = [die1, die2, die3]
    return dice # return the list

# function to calculate the total score of the dice
def calculate_score(dice):
    return sum(dice)

# player rolls. implement rules. 
def player_turn(player_name):
    dice = roll_dice()
    print(f"player_name's turn") 
    print(f"roll value: {dice}") # display roll value

# check if it tuples
    if dice[0] == dice[1] == dice[2]: 
        print("you tupled out! 0 points.")
        return 0
    
# check if fixed
    fixed_dice = []
# compare what each dice says
    if dice[0] == dice[1]:
     fixed_dice = [dice[0], dice[1]]
    elif dice[1] == dice[2]:
     fixed_dice = [dice[1], dice[2]] ##

     if fixed_dice:
        print(f"Fixed dice: {fixed_dice}")

# give the player a chance to reroll or stop
    choice = input("Type 'reroll' to reroll the die, or 'stop' to stop and keep your score: ") ##
    if choice == 'reroll':
        for i in range(3):
         if dice[i] not in fixed_dice:
             dice[i] = random.randint(1,6)
             # print the new roll
             print (f"New roll: {dice}")
        return sum(dice)
    else:
       # player stops. return score
       return sum(dice)
        
# let's set target score 
#
while True:
   try:
      target_score = input("Enter a target score between 10 and 100: ")
      if 0< target_score <10:
         break
      if 10> target_score  > 100:
         break
      else:
        print ("Target score must be between 10 and 100.")
    except ValueError:
        print ("Invalid input. Please enter another number.")

    # Initialize player scores
    #
        scores = ["player 1": 0, "Player 2": 0]

# The loop to run the game until one player reaches the target score
#
# Player 1
if scores["Player 1"] < target_score and scores["Player 2"] < target_score:
   scores["Player 1"] += player_turn("Player 1")
   print (f"Player 1's score: {scores['Player 1']}")

   if scores["Player 1"] >= target_score:
      print(f"\nPlayer 1 wins the game. Score: {scores['Player 1']}")
    break

# Player 2
   scores["Player 2"] += player_turn("Player 2")
   print (f"Player 2's score: {scores['Player 2']}")

   if scores["Player 2"] >= target_score:
      print(f"\nPlayer 2 wins the game. Score: {scores['Player 2']}")
    break




    
