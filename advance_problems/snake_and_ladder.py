# Snake & Ladder Simulator
import random

def snake_ladder():
    player_position = 0

    def roll_dice():
        return random.randint(1, 6)

    def play_option():
        dice_number = roll_dice()
        play = random.choice(['no-play', 'ladder', 'snake'])
        if play == 'no-play':
            return
        elif play == 'ladder':
            player_position += dice_number
            return player_position
        else: 
            player_position -= dice_number
            return player_position
        
    
