from character import Warrior, Mage, Rogue, Paladin
from game import Game
import time
import random

def create_character():
    name = input('✍Enter character name: ')
    print('🕹Choose a character class: ')
    print('🗡 1.Warrior')
    print('🔮 2.Mage')
    print('🪓 3.Rogue')
    print('⚔ 4.Paladin')
    choice = input('Enter your choice (1 - 4): ')
    
    if choice == '1':
        return Warrior(name)
    elif choice == '2':
        return Mage(name)
    elif choice == '3':
        return Rogue(name)
    elif choice == '4':
        return Paladin(name)
    
    else:
        print('Invalid choice. Please try again.☠')
        return Warrior(name)

def main():
    game = Game()
    
    print('Welcome to the RPG game! 🎮')
    player = create_character()
    game.add_player(player)
    
    while True:
        print("\n🎫Menu:")
        print('1. Go to the forest🎄')
        print('2. Go to the cave🕳️')
        print('3. Go to the mountains🏔️')
        print('4. Save the game💾')
        print('5. Load the game📀')
        print('6. Exit🚫')
        
        choice = input('✍Enter choice (1-6): ')
        
        if choice == '1':
            game.go_to_location(player, 'forest')
        elif choice == '2':
            game.go_to_location(player, 'cave')
        elif choice == '3':
            game.go_to_location(player, 'mountains')
        elif choice == '4':
            filename = input('💾Enter filename to save: ')
            game.save_game(filename)
        elif choice == '5':
            filename = input('📀Enter filename to load: ')
            game = Game.load_game(filename)
            player = game.players[0]
        elif choice == '6':
            break
        else:
            print('Invalid choice. Please try again.💩')

if __name__ == "__main__":
    main()
