class Item:
    def __init__(self, name, slot, attack=0, defense=0, health=0):
        self._name = name
        self._slot = slot
        self._attack = attack
        self._defense = defense
        self._health = health

    @property
    def slot(self):
        return self._slot
    
    def get_stat(self, stat):
        return getattr(self, f'_{stat}', 0)
    
    def __str__(self):
        return f'{self._name} - Attack: {self._attack}, Defense: {self._defense}, Health: {self._health}'
    

class Inventory:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item):
        self._items.remove(item)

    def list_items(self):
        return [str(item) for item in self._items]

    def __str__(self):
        return ''.join(self.list_items())
