import os
from random import uniform, randint
import time


cls = lambda: os.system("cls" if os.name == "nt" else "clear")

def start():
    global name, lvl, mhp, hp, strength, defense, stage, classes, chants, critc, spells, mana, aegis, aegisheals, alpha, alphas, souls
    if os.name == "nt":
        os.system("color 0f")
        os.system("title Heroes Quest")
    cls()

    name = input("\nUsername: ")
    if not name:
        start()

    cls()
    print("Classes:\n")
    print("A) Warrior")
    print("B) Sorcerer")
    print("C) Ninja")
    print("D) Guardian")
    classes = input("\n\n>> ").lower()
    if not classes:
        start()

    if classes == "a":
        hp = 100
        mhp = 100
        strength = 8
        defense = 16
        aegis = 0
        aegisheals = 0


    elif classes == "b":
        hp = 100
        mhp = 100
        strength = 4
        defense = 0
        mana = 100
        chants = 0
        spells = 0


    elif classes == "c":
        hp = 100
        mhp = 100
        strength = 11
        defense = 4
        critc = 25
        alpha = 4
        alphas = 0


    elif classes == "d":
        hp = 100
        mhp = 100
        strength = 6
        defense = 6
        souls = 0

    else:
        print("\nYou did not make a valid selection.")
        if os.name == "nt":
            os.system("timeout 2 >nul")
        else:
            time.sleep(2)
        start()

    stage = 0
    lvl = 1
    prep()


def gameover():
    print("\nYou have died . . .")
    time.sleep(5)
    start()



def victory():
    cls()
    print(f"{name}, you are victorious!")
    print("\nPlayer stats:\n")
    print(f"Name: {name}")
    if classes == "a":
        print("Class: Warrior")
    elif classes == "b":
        print("Class: Sorcerer")
    elif classes == "c":
        print("Class: Ninja")
    elif classes == "d":
        print("Class: Guardian")
    else:
        print("Class: Unknown to mankind")
    print(f"Level: {lvl}")
    print(f"HP: {round(hp)}/{mhp}")
    print(f"Strength: {round(strength)}")
    print(f"Defense: {defense}")
    if classes == "a":
        print(f"Aegis Stacks: {aegis}")
        print(f"Aegis Heals: {aegisheals}\n")
    if classes == "b":
        print(f"Mana: {mana}")
        print(f"Chants used: {chants}")
        print(f"Spells used: {spells}\n")
    if classes == "c":
        print(f"Alphas: {alphas}\n")
    if classes == "d":
        print(f"Souls: {souls}\n")
    time.sleep(15)
    start()



def prep():
    global ename, elvl, emhp, ehp, estrength, eboost, stage
    cls()

    list = ["Werewolf", "Golem", "Slime King"]
    list2 = ["Vampire", "Reaper", "Demon"]
    list3 = ["Wraith", "Red Crimson Demon", "Wyvern"]
    list4 = ["Titan", "Celestial Entity", "Seraphim"]

    if stage == 0:
        ename = list[randint(0, 2)]
        elvl = randint(1, 6)
        estrength = uniform(6, 11)
        emhp = randint(12, 23)
        ehp = emhp
        eboost = randint(21, 31), uniform(6, 11), randint(8, 12), randint(7, 11)  # hp, str, lvl, def
        battle()

    elif stage == 1:
        ename = list2[randint(0, 2)]
        elvl = randint(10, 30)
        estrength = uniform(16, 36)
        emhp = randint(28, 53)
        ehp = emhp
        eboost = randint(46, 73), uniform(11, 16), randint(18, 24), randint(11, 18)  # hp, str, lvl, def
        battle()

    elif stage == 2:
        ename = list3[randint(0, 2)]
        elvl = randint(40, 60)
        estrength = uniform(38, 67)
        emhp = randint(66, 112)
        ehp = emhp
        eboost = randint(89, 127), uniform(24, 31), randint(26, 37), randint(18, 34)  # hp, str, lvl, def
        battle()

    elif stage == 3:
        ename = list4[randint(0, 2)]
        elvl = randint(70, 100)
        estrength = uniform(92, 136)
        emhp = randint(168, 220)
        ehp = emhp
        eboost = randint(96, 106), uniform(47, 51), randint(58, 63), randint(34, 56)  # hp, str, lvl, def
        battle()


def checkvictory():
    global lvl, hp, mhp, strength, stage, defense, souls

    if ehp <= 0:
        stage += 1
        if stage < 4:
            if classes == "d":
                souls += 1
                mhp += (24 * souls)
                hp += (24 * souls)
            hp += eboost[0]
            mhp += eboost[0]
            strength += eboost[1]
            lvl += eboost[2]
            defense += eboost[3]
            print(f"\n\nYou have killed the {ename}, so you continue to fight other creatures.")
            print(f"\nReward:")
            print(f"{eboost[2]} +LVL")
            print(f"{eboost[0]} +HP")
            print(f"{round(eboost[1])} +STR")
            print(f"{eboost[3]} +DEF")
            if os.name == "nt":
                os.system("timeout 10 >nul")
            else:
                time.sleep(10)
            prep()
        elif stage == 4:
            print(f"\n\nYou have killed the {ename}, but there are no other creatures to fight.")
            if os.name == "nt":
                os.system("timeout 10 >nul")
            else:
                time.sleep(10)
            victory()


def damagesystem():
    global hp, ehp

    if classes == "c":
        if randint(0, 100) <= critc:
            damage = (strength + alphas) * (1 + critc / 100)
        else:
            damage = strength + alphas
    else:
        damage = strength

    ehp -= damage
    print(f"\n\nYou have hit the {ename} for {round(damage)} ({round(ehp)}/{emhp})")
    if os.name == "nt":
        os.system("timeout 3 >nul")
    else:
        time.sleep(3)
    checkvictory()

    if classes == "a":
        ACF = estrength * 100 / (100 + defense + aegis)
    else:
        ACF = estrength * 100 / (100 + defense)

    hp -= ACF
    print(f"The {ename} have hit you for {round(ACF)} ({round(hp)}/{mhp})")
    if os.name == "nt":
        os.system("timeout 3 >nul")
    else:
        time.sleep(3)

    if hp <= 0:
        gameover()
    else:
        battle()


def battle():
    global lvl, hp, mhp, strength, ehp, stage, defense, chants, spells, mana, aegis, alphas, aegisheals
    cls()

    print(f"\n\nName: {name}")
    if classes == "a":
        print("Class: Warrior")
    elif classes == "b":
        print("Class: Sorcerer")
    elif classes == "c":
        print("Class: Ninja")
    elif classes == "d":
        print("Class: Guardian")
    else:
        print("Class: Unknown to mankind")
    print(f"Level: {lvl}")

    print(f"\nHealth: {round(hp)} / {mhp}")
    print(f"Strength: {round(strength)}")
    print(f"Defense: {defense}")
    if classes == "a":
        print(f"Aegis: {aegis}")
    if classes == "b":
        print(f"Mana: {mana}")
    print("====================    ooooooooooooooooo")
    print("                        o A) Attack     o")
    if classes == "a":
        print("                        o B) Aegis      o")
    if classes == "b":
        print("                        o B) Chant      o")
        print("                        o C) Fireball   o")
        print("                        o D) Mightycure o")
    if classes == "c":
        print("                        o B) Alpha      o")
    print("====================    ooooooooooooooooo")
    print(f"Name: {ename}")
    print(f"Level: {elvl}")

    print(f"\nHealth: {round(ehp)} / {emhp}")
    print(f"Strength: {round(estrength)}")


    battlechoice = input("\n\n>> ").lower()
    if not battlechoice:
        battle()

    if battlechoice == "a":
        damagesystem()

    elif battlechoice == "b":
        if classes == "a":
            if stage >= 1:
                if aegis < 100:
                    aegis += 20
                    ACF = estrength * 100 / (200 + defense + aegis)
                    hp -= ACF
                    print(f"\n\nThe {ename} have hit you for {round(ACF)} ({round(hp)}/{mhp})")
                    if os.name == "nt":
                        os.system("timeout 3 >nul")
                    else:
                        time.sleep(3)
                    if hp <= 0:
                        gameover()
                    else:
                        battle()
                else:
                    ACF = estrength * 100 / (300 + defense + aegis)
                    hp -= ACF
                    maxaegis = int((estrength - ACF) / uniform(3.2, 4.4))
                    aegisheals += maxaegis
                    hp += maxaegis
                    print(f"\n\nThe {ename} have hit you for {round(ACF)} ({round(hp)}/{mhp})")
                    print(f"Aegis Heals: {maxaegis} +HP")
                    if os.name == "nt":
                        os.system("timeout 3 >nul")
                    else:
                        time.sleep(3)
                    if hp <= 0:
                        gameover()
                    else:
                        battle()

            else:
                print("\nYou cannot start stacking Aegis at the first stage.")
                if os.name == "nt":
                    os.system("timeout 2 >nul")
                else:
                    time.sleep(2)
            battle()

        elif classes == "b":
            if chants < 5:
                if lvl >= 30:
                    chants += 1
                    print("\nChanting yourself for restoration.. (30 sec.)")
                    time.sleep(30)
                    chant = randint(16, 32)
                    mhp += chant
                    hp += chant
                    mana = 100
                    print(f"\n{chant} +HP")
                    print("Mana restored")
                    if os.name == "nt":
                        os.system("timeout 3 >nul")
                    else:
                        time.sleep(3)

                elif lvl >= 20:
                    chants += 1
                    print("\nChanting yourself for restoration.. (20 sec.)")
                    time.sleep(20)
                    chant = randint(8, 16)
                    mhp += chant
                    hp += chant
                    mana = 100
                    print(f"\n{chant} +HP")
                    print("Mana restored")
                    if os.name == "nt":
                        os.system("timeout 3 >nul")
                    else:
                        time.sleep(3)

                elif lvl >= 10:
                    chants += 1
                    print("\nChanting yourself for restoration.. (10 sec.)")
                    time.sleep(10)
                    chant = randint(4, 8)
                    mhp += chant
                    hp += chant
                    mana = 100
                    print(f"\n{chant} +HP")
                    print("Mana restored")
                    if os.name == "nt":
                        os.system("timeout 3 >nul")
                    else:
                        time.sleep(3)

                else:
                    print("\nYour level is too low to start chanting. (Level 10 Required.)")
                    if os.name == "nt":
                        os.system("timeout 2 >nul")
                    else:
                        time.sleep(2)
                battle()

            else:
                print("\nYou cannot chant yourself more than 3 times.")
                if os.name == "nt":
                    os.system("timeout 2 >nul")
                else:
                    time.sleep(2)
            battle()

        elif classes == "c":
            if alphas < 3:
                alphas += 1
                damage = (strength/alpha) * 0.42 * alpha  #46 default

                for loop in range(0, alpha):
                    ehp -= damage
                    print(f"You have hit the {ename} for {round(damage)} ({round(ehp)}/{emhp})")

                if os.name == "nt":
                    os.system("timeout 3 >nul")
                else:
                    time.sleep(3)
                checkvictory()

                ACF = estrength * 100 / (100 + defense)
                hp -= ACF
                print(f"The {ename} have hit you for {round(ACF)} ({round(hp)}/{mhp})")
                if os.name == "nt":
                    os.system("timeout 3 >nul")
                else:
                    time.sleep(3)
                if hp <= 0:
                    gameover()
                else:
                    battle()

            else:
                print("\nAlpha cannot be done more than 3 times.")
                if os.name == "nt":
                    os.system("timeout 2 >nul")
                else:
                    time.sleep(2)
                battle()

        else:
            print("\nYou did not make a valid selection.")
            if os.name == "nt":
                os.system("timeout 2 >nul")
            else:
                time.sleep(2)
            battle()


    elif battlechoice == "c":
        if classes == "b":
            if spells < 3:
                spells += 1
                if mana >= 20:
                    mana -= 20
                    print("\nYou've casted Fireball.")
                    damage = strength * 1.60

                    ehp -= damage
                    print(f"\nYou have hit the {ename} for {round(damage)} ({round(ehp)}/{emhp})")
                    if os.name == "nt":
                        os.system("timeout 3 >nul")
                    else:
                        time.sleep(3)
                    checkvictory()

                    ACF = estrength * 100 / (100 + defense)
                    hp -= ACF
                    print(f"The {ename} have hit you for {round(ACF)} ({round(hp)}/{mhp})")
                    if os.name == "nt":
                        os.system("timeout 3 >nul")
                    else:
                        time.sleep(3)
                    if hp <= 0:
                        gameover()
                    else:
                        battle()
                else:
                    print("\nInsufficient amount of mana to cast Fireball.")
                    if os.name == "nt":
                        os.system("timeout 2 >nul")
                    else:
                        time.sleep(2)
                    battle()

            else:
                print("\nYou cannot cast more than 3 spells.")
                if os.name == "nt":
                    os.system("timeout 2 >nul")
                else:
                    time.sleep(2)
                battle()

        else:
            print("\nYou did not make a valid selection.")
            if os.name == "nt":
                os.system("timeout 2 >nul")
            else:
                time.sleep(2)
            battle()


    elif battlechoice == "d":
        if classes == "b":
            if spells < 3:
                spells += 1
                if mana >= 70:
                    mana -= 70
                    print("\nMightycure has been casted.")
                    mightycure = randint(46, 58)
                    mhp += mightycure
                    hp += mightycure
                    print(f"{mightycure} +HP")
                    if os.name == "nt":
                        os.system("timeout 2 >nul")
                    else:
                        time.sleep(2)
                    battle()
                else:
                    print("\nInsufficient amount of mana to cast Mightycure.")
                    if os.name == "nt":
                        os.system("timeout 2 >nul")
                    else:
                        time.sleep(2)
                    battle()

            else:
                print("\nYou cannot cast more than 3 spells.")
                if os.name == "nt":
                    os.system("timeout 2 >nul")
                else:
                    time.sleep(2)
                battle()

        else:
            print("\nYou did not make a valid selection.")
            if os.name == "nt":
                os.system("timeout 2 >nul")
            else:
                time.sleep(2)
            battle()

    else:
        print("\nYou did not make a valid selection.")
        if os.name == "nt":
            os.system("timeout 2 >nul")
        else:
            time.sleep(2)
        battle()
start()
