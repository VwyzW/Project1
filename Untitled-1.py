import random

def roll_dice():
    """
    If the two dice are the same, multiply the sum of the two dice points by 2, otherwise just add them together
    """
    dice1 = random.randint(1,2,3,4,5,6)
    dice2 = random.randint(1,2,3,4,5,6)
    tota1 = dice1 + dice2 
    if dice1 == dice2:
        tota1 *= 2
    return dice1, dice2, tota1

def play_game(rounds=10)
    """
    Each games has 10 rounds by default.
    In each round, the player and the robot roll the dice and compare the scores to determine the winner of that round.
    Finally, the total score and the final winner are output
    """
    player_score = 0
    robot_score = 0
    