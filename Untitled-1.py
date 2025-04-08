import random
import time

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

def play_game(rounds=10, player_name="player"):
    """
    Each games has 10 rounds by default.
    In each round, the player and the robot roll the dice and compare the scores to determine the winner of that round.
    Finally, the total score and the final winner are output
    """
    player_score = 0
    robot_score = 0
    player_bonus = 0
    robot_bonus = 0  

    for i in range(1, range+1):
        print(f"==== Round {i} ====")

        print(f"{player_name} rolling the dice......")
        time.sleep(2)
        # 玩家回合
        p_dice1, p_dice2, p_tota1 = roll_dice()
        print(f"The dice rolled by the {player_name}: {p_dice1} and {p_dice2} -> Score: {p_tota1}")

        if p_dice1 == 6 and p_dice2 == 6:
            player_score += 1
            player_bonus += 1
            print("Super Rewards! {player_name} rolling a double 6, an extra round victory point is awarded! ")

        print("Robot rolling the dice......")
        time.sleep(2)
        # 机器人回合
        r_dice1, r_dice2, r_tota1 = roll_dice()
        print(f"The dice rolled by the robot: {r_dice1} and {r_dice2} -> Score: {r_tota1}")

        if r_dice1 == 6 and r_dice2 == 6:
            robot_score += 1
            robot_bonus += 1
            print("Super Rewards! Robot rolling a double 6, an extra round victory point is awarded! ")

        if p_tota1 > r_tota1:
            player_score += 1
            print("The player wins the round! \n")
        elif p_tota1 < r_tota1:
            robot_score += 1
            print("The robot wins the round! \n")
        else:
            print("Game draw! \n")

    print("==== 最终比分 ====")
    print(f"{player_name}: {player_score} (The super rewards include: {player_bonus})")
    print(f"Robot: {robot_score} (The super rewards include: {robot_bonus})")
    if player_score > robot_score:
        print(f"{player_name} Won the game!")
    elif player_score < robot_score:
        print("Robot Won the game!")
    else:
        print("Game draw!")

if __name__ == '__main__':
    name = input("Please enter your name: ").strip()
    if not name:
        name = "Player"
    while True:
        play_game(player_name=name)
        choice = input("Another round? (y/n): ").strip().lower()
        if choice != 'y':
            break