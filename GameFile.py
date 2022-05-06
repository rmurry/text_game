from random import randint
import random
import math
import itertools

class Character:
    def __init__(self):


        self.name = input("What is your name, Adventurer?")

        type_options = {1:"Tank",2:"Paladin",3:"Rogue",4:"Glass Cannon"}
        
        print("What class would you like to play as? This will determine your stats (type a number):\n1) Tank\n2) Paladin\n3) Rogue\n4) Glass Cannon")
        type_choice = int(input())
        while type_choice not in [1,2,3,4]:
            print("Invalid Choice. What class would you like to play as? This will determine your stats (type a number):\n1) Tank\n2) Paladin\n3) Rogue\n4) Glass Cannon")
            type_choice = int(input())
        self.type = type_options[type_choice]

        if self.type == 'Glass Cannon':
            self.health =randint(20,40)
            self.attack = randint(15,20)
            self.speed = randint(5,10)
            self.ac = 3
            
        elif self.type == 'Rogue':
            self.health = randint(40,60)
            self.attack = randint(12,17)
            self.speed = randint(4,9)
            self.ac = 4

        elif self.type == 'Paladin':
            self.health = randint(60,80)
            self.attack = randint(9,14)
            self.speed = randint(3,8)
            self.ac = 5

        elif self.type == 'Tank':
            self.health = randint(80,100)
            self.attack = randint(8,13)
            self.speed = randint(2,7)
            self.ac = 6

        self.gold = 0

        self.level = 1
        self.xp = 0

        level_req = {}
        for i in range(1,10):
            level_req[i] = (200 + (i * 50)) * (i-1)

    def Start(self):
        print(f"You chose to play as a {self.type}. Your stats are:\nHealth: {self.health}\nAttack: {self.attack}\nSpeed: {self.speed}\nYour Armor Level is {self.ac}\nYou're Level {self.level} with {self.xp}xp\n")

    def earnGold(self,amount):
        self.gold += amount
    
    def spendGold(self,amount):
        self.gold -= amount

    def Heal(self,amount):
        self.health += amount
    
    def Damage(self,amount):
        self.health -= amount
        print(f"Your HP is now {self.health}\n")

    def Slow(self,amount):
        self.speed -= amount

    def Boost(self,amount):
        self.speed += amount

    def Attack(self):
        print(f"You attack for {self.attack}")
        return(self.attack)

    def Level(self,amount):
        self.xp += amount

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
        print(f"A {self.mon} appears ({self.health} HP)!")

    def Attack(self):
        print(f"The {self.mon} attacks for {self.attack}")
        return(self.attack)

    
    def Damage(self,amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            print(f"The {self.mon} has fainted! You gain {self.xp}xp from this encounter.\n")
        else:
            self.health = self.health
            print(f"The {self.mon} has {self.health} health left!\n")
        return self.xp ## I want to have this xp pass to the character

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
        if mon.speed > char.speed:
            char.Damage(mon.Attack())
            mon.Damage(char.Attack())
        else:
            mon.Damage(char.Attack())
            if mon.health > 0:
                char.Damage(mon.Attack())
            else:
                break

        if mon.health > 0:
            print("Would you like to keep battling?\n1)Yes\n2)No")
            value = int(input())
            while value not in [1,2]:
                print("Invalid Choice. Would you like to keep battling?\n1)Yes\n2)No")
                value = int(input())
            if value == 1:
                pass
            else:
                if Run(char,mon) == 2:
                    pass
                else:
                    break


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
#elif value == 2:
#    run_result = Run(hero,mon)
#    if run_result == 1:
#        print("game over\n") ## Placeholder for successful evasion
#    elif run_result == 2:
#        Fight(hero,mon)




