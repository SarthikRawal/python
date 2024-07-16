# Snake & Ladder Simulator
import random

WINNING_POSITION = 100

def roll_dice():
    return random.randint(1, 6)

def play_option():
    return random.choice(['no-play', 'ladder', 'snake'])
    
def game():
    start_position = 0
    player_position = start_position
    no_of_times_dice_rolled = 0

    while player_position < WINNING_POSITION:
        no_of_times_dice_rolled += 1
        dice_number = roll_dice()

        play = play_option()
        if play == 'no-play':
            pass
        
        if play == 'ladder':
            if not player_position + dice_number > WINNING_POSITION:
                player_position = player_position + dice_number

        if play == 'snake':
            player_position -= dice_number
    
            if player_position < start_position:
                player_position = start_position
            
        if player_position == WINNING_POSITION:
            print(f"Player Position: {player_position}, Player-won 🎉🎉")

    print(f"Number of times 🎲 rolled to win: {no_of_times_dice_rolled}")

if __name__ == '__main__':
    # Game execution
    game()