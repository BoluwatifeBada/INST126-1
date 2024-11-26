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
def turn(player_name):
    dice = roll_dice()
    print(f"player_name's turn") 
    print(f"roll value: {dice}") # display roll value

# check if it tuples
    if dice[0] == dice[1] == dice[2]: 
        print("you tupled out! 0 points.")
        return 0
    
# check if fixed
    fixed_dice = []



    
