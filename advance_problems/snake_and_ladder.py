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

def player_turn(player_position):
    dice_number = roll_dice()
    play = play_option()

    if play == 'no-play':
        return player_position, False

    if play == 'ladder' and player_position + dice_number <= WINNING_POSITION:
        player_position += dice_number

    if play == 'snake':
        player_position -= dice_number
        if player_position < 0:
            player_position = 0

    return player_position, player_position == WINNING_POSITION

def game():
    start_position = 0
    player1_position = start_position
    player2_position = start_position
    player1_dice_rolls = 0
    player2_dice_rolls = 0
    current_player = 1

    while player1_position < WINNING_POSITION > player2_position:
        if current_player == 1:
            player1_dice_rolls += 1
            player1_position, won = player_turn(player1_position)
            if won:
                print(f"Player 1 won 🎉🎉 in {player1_dice_rolls} dice rolls!")
                break
            current_player = 2
        else:
            player2_dice_rolls += 1
            player2_position, won = player_turn(player2_position)
            if won:
                print(f"Player 2 won 🎉🎉 in {player2_dice_rolls} dice rolls!")
                break
            current_player = 1

    print(f"Final Positions: player-1 at {player1_position}, player-2 at {player2_position}")
        
    

if __name__ == '__main__':
    # Game execution
    game()