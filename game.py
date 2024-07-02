import random
import pickle
import time
from character import Warrior, Mage, Rogue, Paladin
from bot import Bot, BotGenerator

class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def save_game(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_game(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

    def battle(self, player1, player2):
        print(f'{player1} VS {player2}')
        time.sleep(1)
        while player1.health > 0 and player2.health > 0:
            damage_to_p2 = player1.attack - player2.defense
            damage_to_p1 = player2.attack - player1.defense
            
            if random.random() < player1.crit_chance:
                damage_to_p2 *= player1.crit_damage
                print(f'{player1.name} CRITICAL HIT!')
                time.sleep(1)
            
            if random.random() < player2.crit_chance:
                damage_to_p1 *= player2.crit_damage
                print(f'{player2.name} CRITICAL HIT!')
                time.sleep(1)
            
            player2._health -= max(damage_to_p2, 0)
            player1._health -= max(damage_to_p1, 0)
            
            print(f'{player1.name} attacks {player2.name} for {damage_to_p2} damage.')
            time.sleep(1)
            print(f'{player2.name} attacks {player1.name} for {damage_to_p1} damage.')
            time.sleep(1)
    
        if player1.health > 0:
            print(f'{player1.name} wins!')
            exp_gained = player2.level * 20
            player1.gain_experience(exp_gained)
            time.sleep(1)
        else:
            print(f'{player2.name} wins!')
            exp_gained = player1.level * 20
            player2.gain_experience(exp_gained)
            time.sleep(1)
        
    def go_to_location(self, player, location):
        print(f'You find yourself in a {location}.')
        time.sleep(1)
        while True:
            bot = BotGenerator.generate_bot(player.level)
            print(f'Encountered {bot.name}')
            self.battle(player, bot)
            if input('Continue? Yes|No: ').lower() == 'no':
                break
