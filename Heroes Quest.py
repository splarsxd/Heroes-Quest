from os import system
from random import uniform, randint
import time

def start():
    global name, lvl, mhp, hp, dmg, defense, xd, classes, chants
    system("cls")

    name = input("\nUsername: ")
    if not name:
        start()

    system("cls")
    print("Classes:\n")
    print("A) Warrior")
    print("B) Sorcerer")
    classes = input("\n\n>> ").lower()
    if not classes:
        start()

    if classes == "a":
        hp = 100
        mhp = 100
        dmg = 8
        defense = 16

    elif classes == "b":
        hp = 100
        mhp = 100
        dmg = 3
        defense = 0
        chants = 0

    else:
        print("\nYou did not make a valid selection.")
        system("timeout 2 >nul")
        start()

    xd = 0
    lvl = 1
    prep()


def gameover():
    print("\nYou have died . . .")
    time.sleep(5)
    start()



def victory():
    system("cls")
    print(f"{name}, you are victorious!")
    print("\nPlayer stats:\n")
    print(f"Name: {name}")
    if classes == "a":
        print("Class: Warrior")
    elif classes == "b":
        print("Class: Sorcerer")
    else:
        print("Class: Unknown to mankind")
    print(f"Level: {lvl}")
    print(f"HP: {hp}/{mhp}")
    print(f"Strength: {round(dmg)}")
    print(f"Defense: {defense}")
    if classes == "b":
        print(f"Chants used: {chants}\n")
    system("timeout -1")
    start()



def prep():
    global ename, elvl, emhp, ehp, edmg, eboost, xd
    system("cls")

    list = ["Werewolf", "Golem", "Slime King"]
    list2 = ["Vampire", "Reaper", "Demon"]
    list3 = ["Wraith", "Red Crimson Demon", "Wyvern"]
    list4 = ["Titan", "Celestial Entity", "Seraphim"]

    if xd == 0:
        ename = list[randint(0, 2)]
        elvl = randint(1, 6)
        edmg = uniform(6, 11)
        emhp = randint(12, 23)
        ehp = emhp
        eboost = randint(21, 31), uniform(9, 12), randint(8, 11), randint(7, 11)  # hp, dmg, lvl, def
        battle()

    elif xd == 1:
        ename = list2[randint(0, 2)]
        elvl = randint(10, 30)
        edmg = uniform(14, 27)
        emhp = randint(28, 53)
        ehp = emhp
        eboost = randint(46, 73), uniform(12, 14), randint(18, 24), randint(11, 18)  # hp, dmg, lvl, def
        battle()

    elif xd == 2:
        ename = list3[randint(0, 2)]
        elvl = randint(40, 60)
        edmg = uniform(34, 61)
        emhp = randint(66, 112)
        ehp = emhp
        eboost = randint(132, 184), uniform(33, 38), randint(26, 37), randint(18, 37)  # hp, dmg, lvl, def
        battle()

    elif xd == 3:
        ename = list4[randint(0, 2)]
        elvl = randint(70, 100)
        edmg = uniform(83, 129)
        emhp = randint(168, 220)
        ehp = emhp
        eboost = randint(96, 106), uniform(47, 51), randint(58, 63), randint(37, 105)  # hp, dmg, lvl, def
        battle()

def battle():
    global lvl, hp, mhp, dmg, ehp, xd, defense, chants
    system("cls")

    print(f"\n\nName: {name}")
    if classes == "a":
        print("Class: Warrior")
    elif classes == "b":
        print("Class: Sorcerer")
    else:
        print("Class: Unknown to mankind")
    print(f"Level: {lvl}")

    print(f"\nHealth: {hp} / {mhp}")
    print(f"Strength: {round(dmg)}")
    print(f"Defense: {defense}")
    print("====================    ooooooooooooooooo")
    print("                        o A) Attack     o")
    print("                        o B) Run        o")
    if classes == "b":
        print("                        o C) Heal       o")
    print("====================    ooooooooooooooooo")
    print(f"Name: {ename}")
    print(f"Level: {elvl}")

    print(f"\nHealth: {round(ehp)} / {emhp}")
    print(f"Strength: {round(edmg)}")


    battlechoice = input("\n\n>> ").lower()
    if not battlechoice:
        battle()

    if battlechoice == "a":
        ehp -= dmg
        print(f"\n\nYou have hit the {ename} for {round(dmg)} ({round(ehp)}/{emhp})")
        system("timeout 3 >nul")

        if ehp <= 0:
            hp += eboost[0]
            mhp += eboost[0]
            dmg += eboost[1]
            lvl += eboost[2]
            defense += eboost[3]
            xd += 1
            if xd < 4:
                print(f"\n\nYou have killed the {ename}, so you continue to fight other creatures.")
                print(f"\nReward:")
                print(f"{eboost[2]} +LVL")
                print(f"{eboost[0]} +HP")
                print(f"{eboost[2]} +DMG")
                print(f"{eboost[3]} +DEF")
                system("timeout 10 >nul")
                prep()
            elif xd == 4:
                hp += eboost[0]
                mhp += eboost[0]
                dmg += eboost[1]
                lvl += eboost[2]
                defense += eboost[3]
                print(f"\n\nYou have killed the {ename}, but there are no other creatures to fight.")
                print(f"\nReward:")
                print(f"{eboost[2]} +LVL")
                print(f"{eboost[0]} +HP")
                print(f"{eboost[2]} +DMG")
                print(f"{eboost[3]} +DEF")
                system("timeout 10 >nul")
                victory()


        ACF = round(int(edmg*100/(100+defense)))
        hp -= ACF
        print(f"The {ename} have hit you for {ACF} ({hp}/{mhp})")
        system("timeout 3 >nul")

        if hp <= 0:
            gameover()
        else:
            battle()


    elif battlechoice == "b":
        print("\nYou have chosen to flee the battle.\nYou retreat to your castle and recover from the damage taken.")
        system("timeout 5 >nul")
        start()

    elif battlechoice == "c":
        if classes == "b":

            if lvl >= 60:
                chants += 1
                print("\nChanting yourself for health points.. (30 sec.)")
                time.sleep(30)
                chant = randint(22, 46)
                mhp += chant
                hp += chant
                print(f"\n{chant} +HP")
                system("timeout 3 >nul")

            elif lvl >= 30:
                chants += 1
                print("\nChanting yourself for health points.. (20 sec.)")
                time.sleep(20)
                chant = randint(16, 38)
                mhp += chant
                hp += chant
                print(f"\n{chant} +HP")
                system("timeout 3 >nul")

            elif lvl >= 10:
                chants += 1
                print("\nChanting yourself for health points.. (10 sec.)")
                time.sleep(10)
                chant = randint(8, 22)
                mhp += chant
                hp += chant
                print(f"\n{chant} +HP")
                system("timeout 3 >nul")

            else:
                print("\nYour level is too low to start chanting. (Level 10 Required.)")
                system("timeout 2 >nul")
            battle()

        else:
            print("\nYou did not make a valid selection.")
            system("timeout 2 >nul")
            battle()

    else:
        print("\nYou did not make a valid selection.")
        system("timeout 2 >nul")
        battle()
start()