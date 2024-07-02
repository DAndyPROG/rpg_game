import random

class Character:
    def __init__(self, name):
        self._name = name
        self._attack = 0
        self._defense = 0
        self._health = 0
        self._experience = 0
        self._level = 1
        self._crit_chance = 0.1
        self._crit_damage = 1.5
        self._inventory = []
        self._equipped_items = {
            "helmet": None,
            "left_hand": None,
            "right_hand": None,
            "armor": None,
            "boots": None,
            "ring": None
        }

    @property
    def name(self):
        return self._name

    @property
    def attack(self):
        return self._attack + self._calculate_equipped_stat('attack')

    @property
    def defense(self):
        return self._defense + self._calculate_equipped_stat('defense')

    @property
    def health(self):
        return self._health + self._calculate_equipped_stat('health')

    @property
    def crit_chance(self):
        return self._crit_chance

    @property
    def crit_damage(self):
        return self._crit_damage

    @property
    def level(self):
        return self._level

    @property
    def experience(self):
        return self._experience

    def gain_experience(self, amount):
        self._experience += amount
        print(f'{self.name} gained {amount} experience points!')
        self._level_up()

    def _level_up(self):
        while self._experience >= self._level * 100:
            self._experience -= self._level * 100
            self._level += 1
            self._increase_stats()
            print(f'{self.name} leveled up to Level {self._level}!')
            self._health = self._calculate_base_health()  # Restore health on level up

    def _increase_stats(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    def equip_item(self, item):
        if item.slot in self._equipped_items:
            self._equipped_items[item.slot] = item
            self._recalculate_stats()

    def unequip_item(self, slot):
        if slot in self._equipped_items:
            self._equipped_items[slot] = None
            self._recalculate_stats()

    def _calculate_equipped_stat(self, stat):
        return sum(item.get_stat(stat) for item in self._equipped_items.values() if item)

    def _recalculate_stats(self):
        self._attack = self._calculate_base_attack()
        self._defense = self._calculate_base_defense()
        self._health = self._calculate_base_health()

    def _calculate_base_attack(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    def _calculate_base_defense(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    def _calculate_base_health(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    def __str__(self):
        return f'{self._name} - Level {self.level}, Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}, Crit Chance: {self.crit_chance}, Crit Damage: {self.crit_damage}'

class Warrior(Character):
    BASE_ATTACK = 10
    BASE_DEFENSE = 5
    BASE_HEALTH = 100

    def __init__(self, name):
        super().__init__(name)
        self._attack = Warrior.BASE_ATTACK
        self._defense = Warrior.BASE_DEFENSE
        self._health = Warrior.BASE_HEALTH

    def _increase_stats(self):
        self._attack += 5
        self._defense += 3
        self._health += 20

    def _calculate_base_attack(self):
        return self.BASE_ATTACK

    def _calculate_base_defense(self):
        return self.BASE_DEFENSE

    def _calculate_base_health(self):
        return self.BASE_HEALTH

class Mage(Character):
    BASE_ATTACK = 12
    BASE_DEFENSE = 3
    BASE_HEALTH = 80

    def __init__(self, name):
        super().__init__(name)
        self._attack = Mage.BASE_ATTACK
        self._defense = Mage.BASE_DEFENSE
        self._health = Mage.BASE_HEALTH

    def _increase_stats(self):
        self._attack += 6
        self._defense += 2
        self._health += 15

    def _calculate_base_attack(self):
        return self.BASE_ATTACK

    def _calculate_base_defense(self):
        return self.BASE_DEFENSE

    def _calculate_base_health(self):
        return self.BASE_HEALTH

class Rogue(Character):
    BASE_ATTACK = 8
    BASE_DEFENSE = 4
    BASE_HEALTH = 90

    def __init__(self, name):
        super().__init__(name)
        self._attack = Rogue.BASE_ATTACK
        self._defense = Rogue.BASE_DEFENSE
        self._health = Rogue.BASE_HEALTH

    def _increase_stats(self):
        self._attack += 4
        self._defense += 3
        self._health += 18

    def _calculate_base_attack(self):
        return self.BASE_ATTACK

    def _calculate_base_defense(self):
        return self.BASE_DEFENSE

    def _calculate_base_health(self):
        return self.BASE_HEALTH

class Paladin(Character):
    BASE_ATTACK = 9
    BASE_DEFENSE = 6
    BASE_HEALTH = 110

    def __init__(self, name):
        super().__init__(name)
        self._attack = Paladin.BASE_ATTACK
        self._defense = Paladin.BASE_DEFENSE
        self._health = Paladin.BASE_HEALTH

    def _increase_stats(self):
        self._attack += 5
        self._defense += 4
        self._health += 22

    def _calculate_base_attack(self):
        return self.BASE_ATTACK

    def _calculate_base_defense(self):
        return self.BASE_DEFENSE

    def _calculate_base_health(self):
        return self.BASE_HEALTH
