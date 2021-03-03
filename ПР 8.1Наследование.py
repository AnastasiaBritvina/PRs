'''Разработать класс Warrior со свойствами: количество hp = 100 , armor = 0;
Создать два дочерних класса Red (armor = 5)   и Blue (armor = 3)
Создать два объета класса, которые будет осуществлять сражение.
Каждый из объектов по очереди наносит удар другому (требуется метод, для случайного определения урона от 0 до 10).
Как только у одного из объектов hp <= 0.
Можно добавть больше свойств)
'''

'''Наследование
Дочерние классы наследуют свойства родительского, 
плюс могут иметь какие-то свои свойства
'''

class Warrior:
    hp = 100
    armor = 0

    def __init__(self, hp, armor):
        self.hp = hp
        self.armor = armor

class Red(Warrior):
    def __init__(self):
        self.armor = 5

class Blue(Warrior):
    def __init__(self):
        self.armor = 3

    def show_armor(self):
        armorOfWarrior =('броня ', str(self.armor))
        print(armorOfWarrior)

r = Red()
b= Blue()
r_hp=r.hp
b_hr=b.hp
r_armor=r.armor
b_armor=b.armor

import random
rand = random.randint(1, 10)

while (r.hp<=0 or b.hp<=0):
    r.hp = r.hp - rand
    b.hp = b.hp - rand
    while (r.armor<=0 or b.armor<=0):
        r.hp = r.hp
        r.armor -= 1
        b.hp = b.hp
        b.armor -= 1
if  r.hp <= 0:
    print('Red died')
else:
    print('Blue died')





