import json 
import random

#Classes

class General:
    def __init__(self, name, HP, MAX_HP, exp, wins):
        self.name = name
        self.HP = HP
        self.MAX_HP = MAX_HP
        self.exp = exp
        self.wins = wins
    
    def stats(self):
        if self.HP < 0:
            self.HP = 0

        health = str(self.HP)
        max_health = str(self.MAX_HP)
        experience = str(self.exp)
        wins = str(self.wins)

        print()
        print("--Stats--")
        print(self.name + ":    ") 
        print("HP:   " + health + "/" + max_health)
        print("Exp.    " + experience)
        print("Wins:    " + wins)
        
        
    def rules(self):
        print("I see you want to hear the rules " + self.name + ".")
        print()
        print("You are required to win 5 battles in any biome of your choice. You will verse a variety of enemies with elements unique to their biome.")
        print("This is a role-playing based game. You will select a battle option first, your opponent will select a battle option after you.")
        print("You will gain experience with every win. Gain 827 or more experience and you will level up, raising your HP. If your HP reaches 0, you must start over.")
        
    def win(self):
        print(self.name + " wins!")
        player.wins = player.wins + 1
    
    def victory(self):
        print('Congratulations ' + name + '. You have won the game.')
        print()
        player.stats()
        print()
        print(json.dumps(General.stats, indent = 4))

    
    def game_over(self):
        print("HP has reached 0...")
        print(name + " has lost consciousness...")
        confirm = ''
        print("-Game Over-")


    
   



#Variables
increment = 0 + random.randint(2,7)
level = 1
victory = False
win = 0
matches = 0
chance = 0
experience = 0
game_over = False
run = False

stats = {}
maps = ["The Junkyard", "The Woods", "The Underpass", "Rules", "Stats"]
junkyard_enemies = ["Mad Taxi", "Plague Rat of Doom", "Dirty Soap Bubble"]
woods_enemies = ["Territorial Oak", "Sssssssneaky Snake", "Arachnid!"]
underpass_enemies = ["Shallow Shallow Shadow", "Well-Nutritioned Deer", "Pineapple-Hating Squirrel"]
credits = tuple("Thank You!")
size = len(maps)

#Entry prompt
print("***********Welcome***********")
print("This is a role-playing video game. The format will require you to use the ENTER key to continue.")
print("You may test this now.")
print()
print("Press ENTER to continue...")
name = input()

print()
print("'Welcome Traveler. Please tell me your name:")
name = input()

if (name == "Don't Care"):
    name = 'Bryan'

print(name + ", is this correct? Enter 'Y' or 'yes' to confirm.")
confirm = input()

while not (confirm == 'Y' or confirm == 'yes'):
    print("Traveler. Please tell me your name.")
    name = input()

    print(name + ", is this correct? Enter 'Y' or 'yes' to confirm.")
    confirm = input()

player = General(name, 50, 50, 0, 0)

#Rules
print("Ok " + name + ". Let's get going. You will be allowed to enter 3 biomes of your choice.")
print("Press any key to continue")
space = input()

print("In order to prove yourself, you must cross any of the following biomes of your choice 5 times.")
space = input()

print("Should your HP points fall to 0, you must start from the beginning. If you level up, you will replenish some health.")
space = input()

while not (player.HP <= 0 or win >= 5):

    #Level Up Condition
    if (player.exp >= 827):
        print()
        print("Congratulations, you have leveled up!")

        level = level + 1
        player.exp = player.exp - 827

        player.MAX_HP = player.MAX_HP + increment
        player.HP = player.HP + increment

        '''level_stat = ("Level " + str(level))
        exp_stat = str(experience)
        stats[name] = level_stat
        stats["HP"] = health
        stats["Exp."] = exp_stat'''



    #Game Over condition
    if (player.HP == 0):
        break

    print(General.stats)
    print(json.dumps(stats, indent = 4))
    print()


    #Biome Selection
    print("Where do you want to go?")
    for i,item in enumerate(maps, 1):
        print(i, item)

    #Fixes the index of choice for the user 
    option = int(input())

    #Out-Of-Bounds Loop
    while (option <= 0 or option >= 6 or option == ' '):
        print("I don't see that option on the map. Would you mind trying again?")
        print("Press ENTER to continue")
        space = input()

        print()
        print("Where do you want to go?")
        for i,item in enumerate(maps, 1):
            print(i, item)

        #Fixes the index of choice for the user 
        option = int(input())

    #Junkyard Biome
    if (option == 1):
        print("Let's head inside the Junkyard. Enemies in this biome are very standard.")
        print("They do not have any outstanding advantages but also do not have any resounding weaknesses.")

        space = input()
        enemy = random.choice(junkyard_enemies)
        enemy_hp = random.randint(20, 25)

        print("--You encounter a " + enemy + "!--")
        print()

        #Battle condition
        while (victory == False):
            print("What do you want to do?")
            print("1. Fight")
            print("2. Run")
            print()

            choice = input()
            damage = 0
            
            #Attack Condition
            if (choice == '1'):
                damage = random.randint(10,20)
                critical = random.randint(1,100)
                
                #Critical Hit aspect
                if (critical == 100):
                    damage * 10
                    enemy_hp  = enemy_hp - damage
                    dmg = str(damage)

                    print(player.name + " attacked.")
                    space = input()
                    print()
                    print("Critical hit! " + name + " dealt " + dmg + " damage.")
                    print()

                    #Enemy Defeat Condition
                if (enemy_hp <= 0):
                    player.exp += player.exp + random.randint(217,728)

                    player.win()

                    break
                       
                else:
                    enemy_hp = enemy_hp - damage
                    dmg = str(damage)

                    print(player.name + " attacked.")
                    space = input()
                    print()
                    print(name + " dealt " + dmg + " damage.")
                    print()

                #Enemy Attack Path
                attack = random.randint(10,15)
                player.HP  = player.HP - attack
                atk = str(attack)
                health = str(player.HP)

                print('The ' + enemy + ' attacks.')
                print()
                space = input()

                print("The " + enemy + " dealt " + atk + " damage.")
                print()

                space = input()

            #Run Condition
            if (choice == '2'):
                chance = random.randint(1,4)
                    
                if (chance == 1 or chance == 2 or chance == 3):
                    print("You have escaped successfully!")
                    print()
                    break

                if (chance == 4):
                    print("There was no way out.")
                    print()

                    player.HP  = player.HP - attack
                    atk = str(attack)

                    print('The ' + enemy + ' attacks.')
                    print()
                    space = input()

                    print("The " + enemy + " dealt " + atk + " damage.")
                    print()
                
            #Game Over Condition
            if (player.HP <= 0):
                break
    
    #The Woods Biome
    if (option == 2):
        print("Alright, we're outside the woods. Creatures in this biome have a rage gene, which have a chance to amplify their attacks.") 
        print("Be careful as they are hard to run away from.")

        space = input()
        enemy = random.choice(woods_enemies)
        enemy_hp = 0 + random.randint(25,50)

        print("--You encounter a " + enemy + "!--")
        print()

        #Battle Condition
        while (victory == False):
            print("What do you want to do?")
            print("1. Fight")
            print("2. Run")
            print()

            choice = input()
            damage = 0
                
            #Fight Condition    
            if (choice == '1'):
                damage = random.randint(5,30)
                critical = random.randint(1,5)

                #Critical Hit Condition
                if (critical == 5):
                    damage * 3
                    enemy_hp  = enemy_hp - damage
                    dmg = str(damage)

                    print(player.name + " attacked.")
                    space = input()
                    print()
                    print("Critical hit! " + player.name + " dealt " + dmg + " damage.")
                    print()

                if (enemy_hp <= 0):
                    player.exp = player.exp + random.randint(170,1307)
                    player.win()

                    break

            #Enemy Attack Path
            attack = 5
            rage = random.randint(1,5)

            #Rage Condition
            if (rage == 5):
                attack = attack * 8
                print('The ' + enemy + ' attacks.')
                print()
                space = input()

                player.HP  = player.HP - attack
                atk = str(attack)

                print("Ouch! The " + enemy + " dealt " + atk + " damage.")
                print()

            else :
                player.HP  = player.HP - attack
                atk = str(attack)

                print('The ' + enemy + ' attacks.')
                print()
                space = input()

                print("The " + enemy + " dealt " + atk + " damage.")
                print()

                space = input()

            #Run Condition
            if (choice == '2'):
                chance = random.randint(1,4)

                if (chance == 1):
                    print("You have escaped successfully!")
                    print()
                    break

                if (chance == 2 or chance == 3 or chance == 4):
                    print("There was no way out.")

                    player.HP  = player.HP - attack
                    atk = str(attack)

                    print('The ' + enemy + ' attacks.')
                    print()
                    space = input()

                    print("The " + enemy + " dealt " + atk + " damage.")
                    print()
                    space = input()

            #Game Over Condition
            if (player.HP <= 0):
                break
    
    #The Underpass Condition
    if (option == 3):
        print('''We have arrived to the Underpass. Enemies in this biome have the ability to strike twice each turn and have immunity to the radioactive environment,
              which will damage you passively with each turn in combat. Their low susceptibility to critical hits is offset by their chance to miss each attack.''')

        space = input()
        enemy = random.choice(underpass_enemies)
        enemy_hp = 0 + random.randint(47, 63)

        print("--You encounter a " + enemy + "!")
        print()
        space = input()

        #Battle Condition
        while (victory == False):
            print("What do you want to do?")
            print("1. Fight")
            print("2. Run")
            print()

            choice = input()
            damage = 0
            
            #Fight Condition
            if (choice == '1'):
                damage = random.randint(29,74)
                critical = random.randint(1,17)

                if (critical == 17):
                    damage * 3
                    enemy_hp  = enemy_hp - damage
                    dmg = str(damage)

                    print(player.name + " attacked.")
                    space = input()
                    print()
                    print("Critical hit! " + name + " dealt " + dmg + " damage.")
                    print()
                    
                else:
                    enemy_hp = enemy_hp - damage
                    atk = str(damage)

                    print(player.name + " attacked.")
                    space = input()
                    print()
                    print(player.name + " dealt " + atk + " damage.")
                    print()

                if (enemy_hp <= 0):
                    player.exp = player.exp + random.randint(170,1307)
                    player.win()

                    break

                #Enemy Miss Condition
                chance = random.randint(0,2)
                attack = random.randint(10,17)

                print('The ' + enemy + ' attacks.')
                print()
                space = input()

                if (chance == 0):
                    print('The ' + enemy + " missed!")
                    space = input()

                else:
                    player.HP = player.HP - attack
                    atk = str(attack)
                    print("The " + enemy + " dealt " + atk + " damage.")
                    print()

                    space = input()


                #Enemy Miss Condition
                chance = random.randint(0,2)
                attack = random.randint(10,17)

                print('The ' + enemy + ' attacks.')
                print()
                space = input()

                if (chance == 0):
                    print('The ' + enemy + " missed!")
                    space = input()

                else:
                    player.HP = player.HP - attack
                    atk = str(attack)
                    print("The " + enemy + " dealt " + atk + " damage.")
                    print()

                    space = input()

            #Run Condition
            if (choice == '2'):
                chance = random.randint(1,4)
                    
                if (chance == 1 or chance == 2 or chance == 3):
                    print("You have escaped successfully!")
                    print()
                    break

                if (chance == 4):
                    print("There was no way out.")
                    print()

                    player.HP  = player.HP - attack
                    atk = str(attack)

                    print('The ' + enemy + ' attacks.')
                    print()
                    space = input()

            #Enemy Defeat Condition
            if (enemy_hp <= 0):
                    player.exp = player.exp + random.randint(170,1307)
                    player.win()

                    break

            #Game Over Condition
            if (player.HP <= 0):
                break
            
            #Damage per round Condition(Biome Specific)
            print("Radioactive toxins poison the environment.")
            space = input()

            player.HP = player.HP - 5
            print(player.name + " took 5 damage from the radiation!")
            print()
            space = input()

    if (option == 4):
        player.rules()
        confirm = input()

    if (option == 5):
        player.stats()
        confirm = input()

    else:
        while not (option == 1 or option == 2 or option == 3 or option == 4 or option == 5):
            while (option <= 0 or option >= 6):
                print("I don't see that option on the map. Would you mind trying again?")
                print("Press any key to continue")
                space = input()

                #Level Up Condition
    if (player.exp >= 827):
        print()
        print("Congratulations, you have leveled up!")

        level = level + 1
        player.exp = player.exp - 827

        player.MAX_HP = player.MAX_HP + increment
        player.HP = player.MAX_HP + 0

        '''level_stat = ("Level " + str(level))
        exp_stat = str(experience)
        stats[name] = level_stat
        stats["HP"] = health
        stats["Exp."] = exp_stat'''



    #Game Over condition
    if (player.HP == 0):
        break

    print(General.stats)
    print(json.dumps(stats, indent = 4))
    print()


    #Biome Selection
    print("Where do you want to go?")
    for i,item in enumerate(maps, 1):
        print(i, item)

    #Fixes the index of choice for the user 
    option = int(input())

    #Out-Of-Bounds Loop
    while (option <= 0 or option >= 6):
        print("I don't see that option on the map. Would you mind trying again?")
        print("Press ENTER to continue")
        space = input()

        print()
        print("Where do you want to go?")
        for i,item in enumerate(maps, 1):
            print(i, item)

        #Fixes the index of choice for the user 
        option = int(input())

    #Junkyard Biome
    if (option == 1):
        print("Let's head inside the Junkyard. Enemies in this biome are very standard.")
        print("They do not have any outstanding advantages but also do not have any resounding weaknesses.")

        space = input()
        enemy = random.choice(junkyard_enemies)
        enemy_hp = random.randint(20, 25)

        print("--You encounter a " + enemy + "!--")
        print()

        #Battle condition
        while (victory == False):
            print("What do you want to do?")
            print("1. Fight")
            print("2. Run")
            print()

            choice = input()
            damage = 0
            
            #Attack Condition
            if (choice == '1'):
                damage = random.randint(10,20)
                critical = random.randint(1,100)
                
                #Critical Hit aspect
                if (critical == 100):
                    damage * 10
                    enemy_hp  = enemy_hp - damage
                    dmg = str(damage)

                    print(player.name + " attacked.")
                    space = input()
                    print()
                    print("Critical hit! " + name + " dealt " + dmg + " damage.")
                    print()

                    #Enemy Defeat Condition
                if (enemy_hp <= 0):
                    player.exp += player.exp + random.randint(217,728)

                    player.win()

                    break
                       
                else:
                    enemy_hp = enemy_hp - damage
                    dmg = str(damage)

                    print(player.name + " attacked.")
                    space = input()
                    print()
                    print(name + " dealt " + dmg + " damage.")
                    print()

                #Enemy Attack Path
                attack = random.randint(10,15)
                player.HP  = player.HP - attack
                atk = str(attack)
                health = str(player.HP)

                print('The ' + enemy + ' attacks.')
                print()
                space = input()

                print("The " + enemy + " dealt " + atk + " damage.")
                print()

                space = input()

            #Run Condition
            if (choice == '2'):
                chance = random.randint(1,4)
                    
                if (chance == 1 or chance == 2 or chance == 3):
                    print("You have escaped successfully!")
                    print()
                    break

                if (chance == 4):
                    print("There was no way out.")
                    print()

                    player.HP  = player.HP - attack
                    atk = str(attack)

                    print('The ' + enemy + ' attacks.')
                    print()
                    space = input()

                    print("The " + enemy + " dealt " + atk + " damage.")
                    print()
                
            #Game Over Condition
            if (player.HP <= 0):
                break
    
    #The Woods Biome
    if (option == 2):
        print("Alright, we're outside the woods. Creatures in this biome have a rage gene, which have a chance to amplify their attacks.") 
        print("Be careful as they are hard to run away from.")

        space = input()
        enemy = random.choice(woods_enemies)
        enemy_hp = 0 + random.randint(25,50)

        print("--You encounter a " + enemy + "!--")
        print()

        #Battle Condition
        while (victory == False):
            print("What do you want to do?")
            print("1. Fight")
            print("2. Run")
            print()

            choice = input()
            damage = 0
                
            #Fight Condition    
            if (choice == '1'):
                damage = random.randint(5,30)
                critical = random.randint(1,5)

                #Critical Hit Condition
                if (critical == 5):
                    damage * 3
                    enemy_hp  = enemy_hp - damage
                    dmg = str(damage)

                    print(player.name + " attacked.")
                    space = input()
                    print()
                    print("Critical hit! " + player.name + " dealt " + dmg + " damage.")
                    print()

                if (enemy_hp <= 0):
                    player.exp = player.exp + random.randint(170,1307)
                    player.win()

                    break

            #Enemy Attack Path
            attack = 5
            rage = random.randint(1,5)

            #Rage Condition
            if (rage == 5):
                attack = attack * 8
                print('The ' + enemy + ' attacks.')
                print()
                space = input()

                player.HP  = player.HP - attack
                atk = str(attack)

                print("Ouch! The " + enemy + " dealt " + atk + " damage.")
                print()

            else :
                player.HP  = player.HP - attack
                atk = str(attack)

                print('The ' + enemy + ' attacks.')
                print()
                space = input()

                print("The " + enemy + " dealt " + atk + " damage.")
                print()

                space = input()

            #Run Condition
            if (choice == '2'):
                chance = random.randint(1,4)

                if (chance == 1):
                    print("You have escaped successfully!")
                    print()
                    break

                if (chance == 2 or chance == 3 or chance == 4):
                    print("There was no way out.")

                    player.HP  = player.HP - attack
                    atk = str(attack)

                    print('The ' + enemy + ' attacks.')
                    print()
                    space = input()

                    print("The " + enemy + " dealt " + atk + " damage.")
                    print()
                    space = input()

            #Game Over Condition
            if (player.HP <= 0):
                break
    
    #The Underpass Condition
    if (option == 3):
        print('''We have arrived to the Underpass. Enemies in this biome have the ability to strike twice each turn and have immunity to the radioactive environment,
              which will damage you passively with each turn in combat. Their low susceptibility to critical hits is offset by their chance to miss each attack.''')

        space = input()
        enemy = random.choice(underpass_enemies)
        enemy_hp = 0 + random.randint(47, 63)

        print("--You encounter a " + enemy + "!")
        print()
        space = input()

        #Battle Condition
        while (victory == False):
            print("What do you want to do?")
            print("1. Fight")
            print("2. Run")
            print()

            choice = input()
            damage = 0
            
            #Fight Condition
            if (choice == '1'):
                damage = random.randint(29,74)
                critical = random.randint(1,17)

                if (critical == 17):
                    damage * 3
                    enemy_hp  = enemy_hp - damage
                    dmg = str(damage)

                    print(player.name + " attacked.")
                    space = input()
                    print()
                    print("Critical hit! " + name + " dealt " + dmg + " damage.")
                    print()
                    
                else:
                    enemy_hp = enemy_hp - damage
                    atk = str(damage)

                    print(player.name + " attacked.")
                    space = input()
                    print()
                    print(player.name + " dealt " + atk + " damage.")
                    print()

                if (enemy_hp <= 0):
                    player.exp = player.exp + random.randint(170,1307)
                    player.win()

                    break

                #Enemy Miss Condition
                chance = random.randint(0,2)
                attack = random.randint(10,17)

                print('The ' + enemy + ' attacks.')
                print()
                space = input()

                if (chance == 0):
                    print('The ' + enemy + " missed!")
                    space = input()

                else:
                    player.HP = player.HP - attack
                    atk = str(attack)
                    print("The " + enemy + " dealt " + atk + " damage.")
                    print()

                    space = input()


                #Enemy Miss Condition
                chance = random.randint(0,2)
                attack = random.randint(10,17)

                print('The ' + enemy + ' attacks.')
                print()
                space = input()

                if (chance == 0):
                    print('The ' + enemy + " missed!")
                    space = input()

                else:
                    player.HP = player.HP - attack
                    atk = str(attack)
                    print("The " + enemy + " dealt " + atk + " damage.")
                    print()

                    space = input()

            #Run Condition
            if (choice == '2'):
                chance = random.randint(1,4)
                    
                if (chance == 1 or chance == 2 or chance == 3):
                    print("You have escaped successfully!")
                    print()
                    break

                if (chance == 4):
                    print("There was no way out.")
                    print()

                    player.HP  = player.HP - attack
                    atk = str(attack)

                    print('The ' + enemy + ' attacks.')
                    print()
                    space = input()

            #Enemy Defeat Condition
            if (enemy_hp <= 0):
                    player.exp = player.exp + random.randint(170,1307)
                    player.win()

                    break

            #Game Over Condition
            if (player.HP <= 0):
                break
            
            #Damage per round Condition(Biome Specific)
            print("Radioactive toxins poison the environment.")
            space = input()

            player.HP = player.HP - 5
            print(player.name + " took 5 damage from the radiation!")
            print()
            space = input()

    if (option == 4):
        player.rules()
        confirm = input()

    if (option == 5):
        player.stats()
        confirm = input()



if (win >= 5):
    player.victory()

if (player.HP <= 0):
    player.game_over()

