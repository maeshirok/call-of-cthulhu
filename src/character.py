'''
ステータス管理
'''
import random
import math

class Character:
    def __init__(self, name):
        self.name = name
        self.str = self.dice(3,6)
        self.con = self.dice(3,6)
        self.siz = self.dice(3,6)
        self.dex = self.dice(3,6)
        self.app = self.dice(3,6)
        self.int = self.dice(3,6)
        self.pow = self.dice(3,6)
        self.edu = self.dice(3,6)
        self.luc = self.pow * 5
        self.dmg_bonus = self.str + self.siz
        self.hp = math.ceil((self.con + self.siz)/2)
        self.mp = self.pow
        self.san = self.pow * 5
        
    def dice(self, die, sided):
        ability_value = 0
        for i in range(die): 
            ability_value += random.randint(1, sided)
        return ability_value
    
    def damage_bonus(self,dmg_bonus):
        if 2 <= dmg_bonus <= 12:
            return -self.dice(1, 6)
        elif 13 <= dmg_bonus <= 16:
            return -self.dice(1, 4)
        elif 17 <= dmg_bonus <= 24:
            return 0
        elif 25 <= dmg_bonus <= 32:
            return self.dice(1, 4)
        elif 33 <= dmg_bonus <= 40:
            return self.dice(1, 6)
        
    def damage_bonus_text(self, dmg_bonus):
        if 2 <= dmg_bonus <= 12:
            return '-1D6'
        elif 13 <= dmg_bonus <= 16:
            return '-1D4'
        elif 17 <= dmg_bonus <= 24:
            return 'none'
        elif 25 <= dmg_bonus <= 32:
            return '1D4'
        elif 33 <= dmg_bonus <= 40:
            return '1D6'
        
    def is_dead(self):
        return self.con <= 0
    
    def attack(self, defender, enemy_name):
        pass

    def defend(self, damage, enemy_name):
        pass

ENEMY = [
    Character('敵A'),
]