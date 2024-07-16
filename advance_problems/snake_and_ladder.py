# Snake & Ladder Simulator
import random

def snake_ladder():
    winning_position = 50
    
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
                player_position += dice_number
            else:
                print("Oops, a snake bite 🐍") 
                player_position -= dice_number
        
            if player_position < 0:
                count = 0
                player_position = start_position
                print("Game-Restart 🔁")
                count += 1
                if count > 3:
                    return "You Lost ☠️"
            if player_position == winning_position:
                return "Player-won 🎉🎉"

            print(f"Rolled dice: {dice_number}, now your at position {player_position}")

    result = game()
    print(result)

# Game execution 
snake_ladder()

