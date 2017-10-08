import os
import sys
from random import randint


class Player:
    def __init__(self, namn, hp, attack, status):
        self.namn = namn
        self.hp = hp
        self.attack = attack
        self.status = status


def bump(self):
    self.hp = self.hp + 1

def stats(self):
    print "Name:", self.namn
    print "HP:", self.hp
    print "Damage:", self.attack
    print "Attack bonus:", self.status



# Your character
player = Player("Hej", 100000, "5-10", 0)

class Fiende:
    def __init__(self, namn, hp, attack):
        self.namn = namn # Fiendens namn (string)
        self.hp = hp # Fiendens liv (int)
        self.attack = attack # Fiendens skada (int)

    def stats(self): # Visar info om fienden
        print "Name:", self.namn
        print "HP:", self.hp
        print "Damage:", self.attack


Y = "Y"
N = "N"
Yes = "Yes"
No = "No"
Ja = "Ja"
Nej = "Nej"
J = "J"
N = "N"
j = "j"
n = "n" #Works for both no and nej
y = "y"
YEs = "YEs"
NO = "NO"
yes = "yes"
no = "no"

#name = raw_input(" ")

#name = [1]
def begin():
    print "Tell me your name"
    player.name = raw_input("")
    print player.name + ", what a nice name"


def main():
    print "Welcome to the world of Z0rk"
    print " "
    c = raw_input("Do you wish to begin? ")
    if c in (Y, Yes, Ja, J, j, y, YEs, yes):
        begin()
    elif c in (N, No, Nej, N, n, NO, no):
        sys.exit()
    else:
        main()
main()

#name = raw_input(" ")
#print name
#name[0] = raw_input("")

def gamemenu():
    print(chr(27) + "[2J")
    print player.name + ", what a nice name"
    Examine = "e"
    print " "
    print player.name,", use the key 'e' to search for nearby objects and to analyze your surroundings" #% name
gamemenu()


print ""
print "You wake up in a dark room, with the smell of burnt candles"
print "Analyze your surroundings"


def analyze():
        print "There is a sharp and shiny object in the corner, go pick it up"


        done = False
        while not done: #While key is wrong, dvs not E/e print the else statement as a loop
            a = raw_input(">>")
            if a == "e" or a == "E" or a == "Yes" or a == "yes":
                print "You walk over to the corner, and pick up the shiny object"
                done = True #if it is true then print the if statement
            else: #Will loop until input is E or e
                print "The darkness is starting to scare you, you must move quickly"
analyze()

def analyze_item():
    print "You picked up the shiny object and start to inspect it"
    print "Must be a knife"
    print "A loud sound is heard outside of the room"
    print "Go outside and look?"

    done = False

    while not done: #While key is wrong, dvs not E, print the else statement
        a = raw_input(">>")
        if a == "e" or a == "E":
            print "You open the door"
            done = True #If it is true then print the if statement
        else: #Else loop the function until the user write the correct input
            print "The sound is getting louder, you must move before the sound is too close"
analyze_item()

def open_door():
    print "You take a step outside"
    print "The sunlight hurts your eyes"
    print "The loud noises have suddenly stopped"
    print "An unknown creature jumps infront of you"
    print "FIGHT OR FLEE?!"

    done = False
    while not done:
        a = raw_input(">>")
        if a == "e" or a == "E" or a == "fight" or a == "Fight":
            print "You choose wisely"
            done = True
        else:
            print "You have nowhere to flee, the door is locked. You must fight"
            print " "
open_door()

def unknown_creature():
    print "The creature reveals itself, it looks rather friendly"
    print "Talk with the creature?"

    done = False
    while not done:
        a = raw_input(">>")
        if a == "e" or a == "E" or a == "Yes" or a == "yes":
            print "You interact with the creature"
            done = True
        else:
            print "The creature interacts with you"
unknown_creature()

def healing_lore():
    print " "
    print "Welcome to the world of Z0rk, outsider"
    print "In this world, every living creature has the ability to attack and heal themselves"
    print "Try healing yourself, by typing 'heal'"

    done = False
    while not done:
        a = raw_input(">>")
        if a == "heal" or a == "Heal" or a == "E" or a == "e":
            print "You heal yourself"
            done = True
        else:
            print "Try healing yourself"
healing_lore()


def zork_lore():
    print " "
    print "Outsider, we need your help"
    print "For the last couple of months there has been a monster torturing us inhabitants of Z0rk"
    print "We need your help to take down the monster, since no inhabitant in Z0rk has the ability to fight him"
    print " "
    print "Is it possible for you to help us?"

    done = False
    while not done:
        a = raw_input(">>")
        if a == "E" or a == "e" or a == "Yes" or a == "yes":
            print "Yes, i will help"
            done = True
        else:
            print "No, i don't have time for such things"
zork_lore()

def fighting():
    print " "
    print "The creature gave you instructions on how to get to the monster"
    print "But the way to the last boss wont be easy"
    print "The final boss has a bunch of henchmen that you must defeat before facing the boss"
    print " "
    print "You reach the monsters stronghold, and begin to fight your way through until you reach the final boss"
fighting()



# Enemies
enemy = Fiende("Monster", 50, "1-3")
enemy2 = Fiende("Super Monster", 75, "3-7")
enemy3 = Fiende("Angry Monster", 100, "3-10")
Boss = Fiende("Z0rk", 120, "5-15")

potion = "Potion +5 attack"
inventory = []
inventory.append(potion)

# combat
monster = [enemy, enemy2, enemy3, Boss]

print "Type 'attack' to attack, 'heal' to heal, 'inventory' too see your inventory and 'info' to see your stats. Use the 'use' command to use your potion. Good luck!"

for m in monster:
    print m.namn, "attacks!"
    m.stats()
    turn = 1

while m.hp > 0 and player.hp > 0:
    inp = raw_input(">>")
    if turn == 1:

        if inp == "attack" or inp == "Attack":
            pdmg = randint(100,100)
            print"You attack, dealing:",(pdmg + player.status), "damage to the enemy."
            m.hp = m.hp -(pdmg + player.status)
            print"Monster hp:", m.hp
            player.status = 0
            turn = 0


        elif inp == "heal" or inp == "Heal":
            heal = randint(5, 10)
            player.hp = player.hp + heal
            print"You heal yourself for:",heal, "hp."
            print"Your hp:",player.hp
            turn = 0

        elif inp == "info" or inp == "Info":
            player.stats()

        elif inp == "inventory" or inp == "Inventory":
            print inventory

        elif inp == "use attack potion" or inp == "Use attack potion" or inp == "use potion":
            if inventory[0] == "Potion +5 attack":
                print"You drink the potion! Your next attack will deal 5 extra damage!"
                inventory[0] = []
                player.status = 5
                print"Your inventory is empty!"

        elif inp != "":
            print"I don't know how to do that."

        if m.hp <= 0 and m != Boss:
            print "You win, face the next enemy now!"




        if turn == 0 and m.hp > 0:
            if m == enemy:
                dmgm = randint(1, 3)
            elif m == enemy2:
                dmgm = randint(1, 15)
            elif m == enemy3:
                dmgm = randint(15, 50)
            else:
                dmgm = randint(30, 90)

            print m.namn, "attacks, dealing:",(dmgm), "damage to you."
            player.hp = player.hp - (dmgm)
            print"Your hp: ", player.hp
            turn = 1
            print"What will you do?"


        if player.hp <= 0:
            print"EXIT TERMINAL!!"

print "You have deafeated the evil Boss and his henchmen! Congratulations!"
