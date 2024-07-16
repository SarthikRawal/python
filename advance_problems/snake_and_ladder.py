# Snake & Ladder Simulator
import random

winning_position = 100

def roll_dice():
    return random.randint(1, 6)

def play_option():
    return random.choice(['no-play', 'ladder', 'snake'])
    
def game():
    start_position = 0
    player_position = start_position

    while player_position < winning_position:
        input("Hit 'enter' to roll the dice 🎲") 
        dice_number = roll_dice()

        play = play_option()
        if play == 'no-play':
            print("No Play 😖")
        
        if play == 'ladder':
            print("Ohh you got a ladder 🪜")
            new_position = player_position + dice_number
            if new_position <= winning_position:
                player_position = new_position
            else:
                print(f"Rolled {dice_number}, which would exceed position {winning_position}. Stay at position {player_position}.")
        else:
            print("Oops, a snake bite 🐍") 
            player_position -= dice_number
    
        if player_position < 0:
            
            player_position = start_position
            print("Game-Restart 🔁")
            
        if player_position == winning_position:
            return "Player-won 🎉🎉"

        print(f"Rolled dice: {dice_number}, now your at position {player_position}")

# Game execution
result = game()
print(result)