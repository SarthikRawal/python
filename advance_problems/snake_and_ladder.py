# Snake & Ladder Simulator
import random

WINNING_POSITION = 100

def roll_dice():
    """
    returns integer value 1-6
    """
    return random.randint(1, 6)

def play_option():
    """
    returns the playing options
    """
    return random.choice(['no-play', 'ladder', 'snake'])
    
def game():
    start_position = 0
    player1_position = start_position
    player2_position = start_position
    player1_dice_rolls = 0
    player2_dice_rolls = 0
    current_player = 1

    while player1_position < WINNING_POSITION and player2_position < WINNING_POSITION:
        if current_player == 1:
            player1_dice_rolls += 1
            dice_number = roll_dice()

            play = play_option()
            if play == 'no-play':
                pass
        
            if play == 'ladder':
                if not player1_position + dice_number > WINNING_POSITION:
                    player1_position += dice_number

            if play == 'snake':
                player1_position -= dice_number
        
                if player1_position < start_position:
                    player1_position = start_position
            
            if player1_position == WINNING_POSITION:
                print(f"Player 1 Position: {player1_position}, Player-1 won 🎉🎉")
                break
            
            current_player = 2

        elif current_player == 2:
            player2_dice_rolls += 1
            dice_number = roll_dice()

            play = play_option()
            if play == 'no-play':
                pass
        
            if play == 'ladder':
                if not player2_position + dice_number > WINNING_POSITION:
                    player2_position += dice_number

            if play == 'snake':
                player2_position -= dice_number
        
                if player2_position < start_position:
                    player2_position = start_position
            
            if player2_position == WINNING_POSITION:
                print(f"Player 2 Position: {player2_position}, Player-2 won 🎉🎉")
                break
            
            current_player = 1
    if player1_position == WINNING_POSITION:
        print(f"Player 1 won in {player1_dice_rolls} 🎲 rolls")
    elif player2_position == WINNING_POSITION:
        print(f"Player 2 won in {player2_dice_rolls} 🎲 rolls")
        
    

if __name__ == '__main__':
    # Game execution
    game()