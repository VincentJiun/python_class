import random


class Role():
    def __init__(self, name):
        self.name = name

    def attack(self):
        print(f'{self.name}使用普通攻擊!!!')

    def defense(self, instruction):
        if instruction == 1:
            print(f'{self.name}使用格檔!!!')
            return random.choice([1, 0.3]) # 格檔成功:對方攻擊*0.3
        elif instruction == 2:
            print(f'{self.name}使用閃避!!!')
            return random.choice([0, 1])


class Warrior(Role):
    def __init__(self, name):
        super().__init__(name)

        self.blood = 500
        self.harm = 200

    def charge(self, instruction):
        if instruction == 1:
            self.attack()
            return self.harm
        elif instruction == 2:
            print(f'{self.name}衝向敵人攻擊!!!')
            return 300

class Monster(Role):
    def __init__(self, name):
        super().__init__(name)

        self.blood = 200
        self.harm = 150

    def  vennom(self, instruction):
        if instruction == 1:
            self.attack()
            return self.harm
        elif instruction == 2:
            print(f'{self.name}使用毒液攻擊!!!')
            return 200


player_name = input('請輸入角色名稱:')
player = Warrior(player_name)

monster = Monster('哥布林')
r = random.choice([1, 2])

while True:
    a = int(input('請輸入攻擊指令: (1)普通攻擊 (2)衝鋒攻擊'))
    player_attack = player.charge(a)
    m_loss =  int(monster.defense(r)*player_attack)
    monster.blood -= m_loss
    if monster.blood <= 0:
        print(f'{monster.name}倒下了，{player.name}勝利!!!')
        break
    else:
        print(f'{monster.name}受到{m_loss}傷害! 生命值剩下{monster.blood}')
        print('')

    d = int(input('請輸入防禦指令: (1)格檔 (2)閃避'))
    moster_attack = monster.vennom(r)
    p_loss =  player.defense(d)*moster_attack
    player.blood -= p_loss
    if player.blood <= 0:
        print(f'{player.name}倒下了，遊戲結束!!!')
        break
    else:
        print(f'{player.name}受到{p_loss}傷害! 生命值剩下{player.blood}')
        print('')





