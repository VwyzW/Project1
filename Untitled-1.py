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

    for i in range(1, range+1):
        print(f"Round {i}:")
        # Player Turn
        p_dice1, p_dice2, p_tota1 = roll_dice()
        print(f"The dice rolled by the player: {p_dice1} and {p_dice2} -> Score: {p_tota1}")
        
        # Robot Round
        r_dice1, r_dice2, r_tota1 = roll_dice()
        print(f"The dice rolled by the robot: {r_dice1} and {r_dice2} -> Score: {r_tota1}")

        if p_tota1 > r_tota1:
            player_score += 1
            print("The player wins the round! \n")
        elif p_tota1 < r_tota1:
            robot_score += 1
            print("The robot wins the round! \n")
        else:
            print("Game draw! \n")

if __name__ == '__main__':
    while True:
        play_game()
        choice = input("Another round? (y/n): ").strip().lower()
        if choice != 'y':
            break