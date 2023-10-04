'''
クトゥルフ神話trpg
'''
import random
import status

def main():
    player = status.Character('自分')
    enemy = random.choice(status.ENEMY)
    
    print('\n' + '*' * 40 + '\n')
    print(
        f'{player.name:<12}{enemy.name}\n',
        f'str:{player.str:<10}str:{enemy.str}\n',
        f'con:{player.con:<10}con:{enemy.con}\n',
        f'siz:{player.siz:<10}siz:{enemy.siz}\n',
        f'dex:{player.dex:<10}dex:{enemy.dex}\n',
        f'app:{player.app:<10}app:{enemy.app}\n',
        f'int:{player.int:<10}int:{enemy.int}\n',
        f'pow:{player.pow:<10}pow:{enemy.pow}\n',
        f'edu:{player.edu:<10}edu:{enemy.edu}\n',
        f'luc:{player.luc:<10}luc:{enemy.luc}\n',
        f'h p:{player.hp:<10}h p:{enemy.hp}\n',
        f'm p:{player.mp:<10}m p:{enemy.mp}\n',
        f'san:{player.san:<10}san:{enemy.san}'
    )
    print('\n' + '*' * 40 + '\n')

if __name__ == '__main__':
    main()