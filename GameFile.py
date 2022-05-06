from random import randint
import random

class Character:
    def __init__(self):
        self.health = randint(20,100)
        if self.health < 40:
            self.attack = randint(15,20)
            self.speed = randint(5,10)
            self.ac = 3
            self.type = 'Glass Cannon'
        elif self.health < 60:
            self.attack = randint(12,17)
            self.speed = randint(4,9)
            self.ac = 4
            self.type = 'Rogue'
        elif self.health < 80:
            self.attack = randint(9,14)
            self.speed = randint(3,8)
            self.ac = 5
            self.type = 'Paladin'
        elif self.health <= 100:
            self.attack = randint(8,13)
            self.speed = randint(2,7)
            self.ac = 6
            self.type = 'Tank'
        self.gold = 0
        self.level = 1
        self.xp = 0

    def Start(self):
        print("You roll for stats.\nHealth is {}\nAttack is {}\nSpeed is {}\nYou're playing as a {}, which makes your Armor Level {}\nYou're Level {} with {}xp\n".format(self.health,self.attack,self.speed,self.type,self.ac,self.level,self.xp))

    def earnGold(self,amount):
        self.gold += amount
    
    def spendGold(self,amount):
        self.gold -= amount

    def Heal(self,amount):
        self.health += amount
    
    def Damage(self,amount):
        self.health -= amount
        print("Your HP is now {}\n".format(self.health))

    def Slow(self,amount):
        self.speed -= amount

    def Boost(self,amount):
        self.speed += amount

    def Attack(self):
        print("You attack for {}".format(self.attack))
        return(self.attack)

class Enemy:
    def __init__(self):
        monsters = ["dragon","liger","goblin","gremlin","leprechaun","sphinx"]
        self.mon = random.choice(monsters)
        self.health = randint(10,20)
        self.attack = randint(4,12)
        self.speed = randint(1,4)
        self.gold = randint(2,10)
        self.xp = randint(50,150)

    def Appear(self):
        print("A {} appears ({} HP)!".format(self.mon,self.health))

    def Attack(self):
        print("The {} attacks for {}".format(self.mon,self.attack))
        return(self.attack)

    
    def Damage(self,amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            print("The {} has fainted!\n".format(self.mon))
        else:
            self.health = self.health
            print("The {} has {} health left!\n".format(self.mon,self.health))

def Encounter():
    mon = Enemy()
    mon.Appear()
    print("Would you like to engage or attempt to get away?\n1 to fight\n2 to flee")
    value = int(input())
    while value not in [1,2]:
        print("Invalid Choice.\nWould you like to engage or attempt to get away?\n1 to fight\n2 to flee")
        value = int(input())
    return value,mon

def Fight(char,mon):
    while mon.health > 0:
        char.Damage(mon.Attack())
        mon.Damage(char.Attack())

def Run(char,mon):
    print("In order to flee, you need to be faster than the monster - I need a speed check")
    if char.speed >= mon.speed:
        print("You're able to get away!")
        value = 1
    else:
        print("You're unable to get away!")
        value = 2
    return value
    




hero = Character()
hero.Start()

value,mon = Encounter()

if value == 1:
    Fight(hero,mon)
elif value == 2:
    run_result = Run(hero,mon)
    if run_result == 1:
        print("game over\n") ## Placeholder for successful evasion
    elif run_result == 2:
        Fight(hero,mon)




