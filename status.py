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
        self.san = self.pow * 5
        self.mp = self.pow
        
    def is_dead(self):
        return self.con <= 0
    
    def dice(self, die, sided):
        return die * random.randrange(1, sided)
    
    def attack(self, defender, enemy_name):
        pass

    def defend(self, damage, enemy_name):
        pass

ENEMY = [
    Character('敵A'),
]