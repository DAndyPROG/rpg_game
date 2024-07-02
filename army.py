class Army:
    def __init__(self, characters):
        self.characters = characters
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.characters):
            result = self.characters[self.index]
            self.index += 1
            return result
        else:
            self.index = 0
            raise StopIteration
    
    def battle(self, other_army):
        while any(char.health > 0 for char in self.characters) and any(char.health > 0 for char in other_army.characters):
            for char1, char2 in zip(self, other_army):
                if char1.health > 0 and char2.health > 0:
                    self._single_battle(char1, char2)
        
        self._reset_iterator()
    
    def _single_battle(self, char1, char2):
        while char1.health > 0 and char2.health > 0:
            damage_to_c2 = char1.attack - char2.defense
            damage_to_c1 = char2.attack - char1.defense
            char2._health -= max(damage_to_c2, 0)
            char1._health -= max(damage_to_c1, 0)
    
    def _reset_iterator(self):
        self.index = 0
