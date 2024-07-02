import random
from character import Character

class Bot(Character):
    def __init__(self, name, level):
        super().__init__(name)
        self._level = level
        self._attack = random.randint(5, 10) + level
        self._defense = random.randint(3, 6) + level
        self._health = random.randint(30, 60) + level * 10

    def _increase_stats(self):
        pass

    def _calculate_base_attack(self):
        return self._attack

    def _calculate_base_defense(self):
        return self._defense

    def _calculate_base_health(self):
        return self._health

class BotGenerator:
    @staticmethod
    def generate_bot(level):
        return Bot(f'Bot {random.randint(1, 1000)}', level)
