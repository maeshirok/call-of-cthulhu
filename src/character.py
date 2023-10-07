'''
ステータス管理
'''
import random
import math

class Character:
    def __init__(self, name):
        '''各種ステータスの値を計算し決定する'''
        self.name = name
        self.str = self.dice(3, 6)
        self.con = self.dice(3, 6)
        self.siz = self.dice(2, 6) + 6
        self.dex = self.dice(3, 6)
        self.app = self.dice(3, 6)
        self.int = self.dice(2, 6) + 6
        self.pow = self.dice(3, 6)
        self.edu = self.dice(3, 6) + 3
        self.luc = self.pow * 5
        self.dmg_bonus = self.str + self.siz
        self.hp = math.ceil((self.con + self.siz)/2)
        self.mp = self.pow
        self.san = self.pow * 5
        self.armor = 0
        
    def dice(self, die, sided):
        '''nDnのダイスを振る'''
        ability_point = 0
        for i in range(die): 
            ability_point += random.randint(1, sided)
        return ability_point
    
    def damage_bonus(self,dmg_bonus):
        '''ダメージボーナスの値を計算'''
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
        '''ダメージボーナスをステータスに表記するようのテキスト'''
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