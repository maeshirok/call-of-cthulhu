'''
クトゥルフ神話trpg
'''
import random
import character
import enemy

def main():
    player = character.Character('自分')
    monster = random.choice(enemy.ENEMY)
    
    print('\n' + '*' * 40 + '\n')
    print(
        f'{player.name:<17}{monster.name}\n',
        f'str:{player.str:<15}str:{monster.str}\n',
        f'con:{player.con:<15}con:{monster.con}\n',
        f'siz:{player.siz:<15}siz:{monster.siz}\n',
        f'dex:{player.dex:<15}dex:{monster.dex}\n',
        f'app:{player.app:<15}app:{monster.app}\n',
        f'int:{player.int:<15}int:{monster.int}\n',
        f'pow:{player.pow:<15}pow:{monster.pow}\n',
        f'edu:{player.edu:<15}edu:{monster.edu}\n',
        f'luc:{player.luc:<15}luc:{monster.luc}\n',
        f'h p:{player.hp:<15}h p:{monster.hp}\n',
        f'm p:{player.mp:<15}m p:{monster.mp}\n',
        f'san:{player.san:<15}san:{monster.san}\n',
        f'd b:{player.damage_bonus_text(player.dmg_bonus):<15}d b:{monster.damage_bonus_text(monster.dmg_bonus)}',
    )
    print('\n' + '*' * 40 + '\n')

if __name__ == '__main__':
    main()