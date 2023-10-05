'''
クトゥルフ神話trpg
'''
import random
import character

def main():
    player = character.Character('自分')
    enemy = random.choice(character.ENEMY)
    
    print('\n' + '*' * 40 + '\n')
    print(
        f'{player.name:<17}{enemy.name}\n',
        f'str:{player.str:<15}str:{enemy.str}\n',
        f'con:{player.con:<15}con:{enemy.con}\n',
        f'siz:{player.siz:<15}siz:{enemy.siz}\n',
        f'dex:{player.dex:<15}dex:{enemy.dex}\n',
        f'app:{player.app:<15}app:{enemy.app}\n',
        f'int:{player.int:<15}int:{enemy.int}\n',
        f'pow:{player.pow:<15}pow:{enemy.pow}\n',
        f'edu:{player.edu:<15}edu:{enemy.edu}\n',
        f'luc:{player.luc:<15}luc:{enemy.luc}\n',
        f'h p:{player.hp:<15}h p:{enemy.hp}\n',
        f'm p:{player.mp:<15}m p:{enemy.mp}\n',
        f'san:{player.san:<15}san:{enemy.san}\n',
        f'd b:{player.damage_bonus_text(player.dmg_bonus):<15}d b:{enemy.damage_bonus_text(enemy.dmg_bonus)}',
    )
    print('\n' + '*' * 40 + '\n')

if __name__ == '__main__':
    main()