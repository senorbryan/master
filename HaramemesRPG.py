import json 
import random

#Classes

class Character(object):
    def __init__(self, name = '', HP = 0, debuff = False):
        self.name = name
        self.hp = HP
        self.debuff = debuff
        
        def crit(damage):
            chance = (1,5)

            if (chance == 1):
                damage = damage * 1.2
                return damage

            else:
                return damage

        def debuff(debuff):
            if (debuff == False):
                return
            
            elif (debuff == True):
                penalty = random.randint(1,3)
                return 


            
            

#Functional   
 
class Bryan(Character):
    def __init__(self, name='Bryan', HP = 50,):
        super().__init__(name, HP)

    def BryanMenu():
        print("What will Bryan do?")
        print("1. Foresight")
        print("2. Supernova")
        print("3. Broken Record")
        print("4. Alexa Goodnight")


        select = input()

        if (select == 1):
            Bryan.foresight()

        elif (select == 2):
            Bryan.supernova()

        elif (select == 3):
            Bryan.brokenRecord()
        
        elif (select == 4):
            Bryan.alexaGoodnight()

        else:
            while (select != 1 or select != 2 or select != 3 or select != 4):
                print("You did not select a move. Please select a move")

                Bryan.BryanMenu()
        


    #Foresight Move            
        
    def foresight():
        
        print("Bryan used foresight!")
        accuracy = random.randint(0,100)
        concuss_stat = False

        #Foresight failed
        if (accuracy > 60):
            print("The move failed...")
            return

        #Foresight successful

        elif (accuracy <= 60):
            damage = random.randint(10,30)
            print("Bryan dealt " + str(damage) + " damage!")


        turn = input()
        return damage


    #Supernova Move

    def supernova():

        print("Bryan used supernova!")
        turn = input()

        chance = random.randint(1,3)

        if (chance > 2):
            damage = random.randint(10,20)
            concuss_stat = True
            print("Bryan dealt " + str(damage) + " damage!")
            print("The move caused concussion. Your opponent will be concussed for 2 rounds.")

            return damage
        
        else:
            damage = random.randint(10,20)
            print("Bryan dealt " + str(damage) + " damage!")

            return damage

    
    #BrokenRecord Move
    def brokenRecord():

        print("Bryan used broken record!")
        instances = random.randint(2,5)
        total = 0

        while (instances != 0):
            damage = random.randint(2,5) 
            total = total + damage
            print("Bryan dealt " + str(damage) + " damage!")
            instances -= 1
            turn = input()

        print("Bryan dealt " + str(damage) + " damage!")
        turn = input()
        return total 

    #AlexaGoodnight Move

    def alexaGoodnight():

        print("Bryan used Alexa Goodnight!")
        heal = random.randint(5,25)
        print("Time flew past, healing Bryan overnight! Bryan healed " + str(heal) + " HP!")

        turn = input()
        return heal


#Jordan Character Class

class Jordan(Character):
    def __init__(self, name='', HP = 85 ,critBuff = 0):
        super().__init__(name, HP, )

    def JordanMenu():
        print("What will Jordan do?")
        print("1. Dynamic")
        print("2. Hard Hat Hazard")
        print("3. Tarnished")
        print("4. Bedtime")

        

        select = input()

        if (select == 1):
            Jordan.dynamic()

        elif (select == 2):
            Jordan.hardHatHazard()

        elif (select == 3):
            Jordan.tarnished()
        
        elif (select == 4):
            Jordan.bedtime()

        else:
            while (select != 1 or select != 2 or select != 3 or select != 4):
                print("You did not select a move. Please select a move")

                Jordan.JordanMenu()

    #Dynamic Move

    def dynamic():
        print("Jordan used Dynamic!")
        chance = random.randint(1,4)

        if (chance == 1):
            print("The move failed...")
            turn = input()
            return
        
        else:  
            if (JordOUT.critBuff == 0):
                print("The bass was deep with that one! Power increased slightly")
                player.critBuff += 1
                turn = input()
            
            elif (JordOUT.critBuff == 1):
                player.critBuff += 1
                print("The bass was deep with that one! Power increased slightly")
                turn = input()

            elif (JordOUT.critBuff >= 2):
                player.critBuff = 3
                print("The bass was deep with that one! Power increased slightly")
                turn = input()
            else:
                print("Jordan is at max dynamic. Power cannot go any higher.")
                turn = input()

    #Hard Hat Hazard Move

    def hardHatHazard():

        copium = False
        copium = Jordan.cope(copium)

        if (JordOUT.cope == True):
            print("Jordan is coping; he is unable to attack this round")
            next = input()
            return

        print("Jordan used Hard Hat Hazard")
        turn = input()

        damage = random.randint(15,35)
        JordOUT.JordCrit(damage)

        print("Jordan dealt " + str(damage) + " damage")


    #Tarnished Move    
        
    def tarnished():
        copium = False
        copium = Jordan.cope(copium)

        if (JordOUT.cope == True):
            print("Jordan is coping; he is unable to attack this round")
            turn = input()
            return

        
        else:

            print("Jordan used tarnished!")
            turn = input()
            
            damage = random.randint(5, 10)
            JordOUT.JordCrit(damage)

            print("Jordan dealt " + str(damage) + " damage!")

        copium = False
        copium = Jordan.cope(copium)

        if (JordOUT.cope == True):
            print("Jordan is coping; he is unable to attack this round")
            turn = input()
            return


        else:
            print("Jordan striked twice!")
            turn = input()

            damage = random.randint(20,40)
            JordOUT.JordCrit(damage)

            print("Jordan dealt " + str(damage) + " damage!")


    #Bedtime Move
        
    def bedtime():
        print("Jordan used bedtime!")
        turn = input()

        chance = random.randint(1,4)

        if (chance == 1 or chance == 2 or chance == 3):
            print("The opponent fell asleep!")
            turn = input()
            sleep_stat = True
            return sleep_stat

        else:
            print("The move failed...Jordan was told to go to bed by his mom.")
            print("Jordan was put to sleep!")
            turn = input()

            fixed_sleep = True
            return fixed_sleep


    def cope(copium):
        copium = random.randint(1,3)

        if (copium == 1):
            copium = False
            return copium
        else:
            copium = True
            return copium
        
    def JordCrit(damage):
        chance = (1,2)
        critical = 0
        if (chance == 1):
            if (JordOUT.critBuff == 0):
                critical = damage * 1.4
            
            if (JordOUT.critBuff == 1):
                critical = damage * 1.6

            if (JordOUT.critBuff == 2):
                critical = damage * 1.8

            if (JordOUT.critBuff == 3):
                critical = damage * 2.0

        else:
            return critical

#Dilan Character Class    

class Dilan(Character):
    def __init__(self, name='', HP = 65,):
        super().__init__(name, HP,)  

    def DilanMenu():
        print("What will Dilan do?")
        print("1. Criticize")
        print("2. Fast 9")
        print("3. Hot Wheels")
        print("4. Chug Jug")

        select = input()

        if (select == 1):
            Dilan.criticize()

        if (select == 2):
            Dilan.fast9()

        if (select == 3):
            Dilan.hotWheels()

        if (select == 4):
            Dilan.chugJug()

    #Criticize Move    

    def criticize():
        dilanQuotes = ["YASSINE WHAT ARE YOU DOING???", "I'M SO MUCH BETTER THAN YOU", "STAY BELOW ME"]

        print("Dilan summoned Yassine.")
        quote = random.choice(dilanQuotes)
        print(quote)
        turn = input()

        damage = random.randint(13, 27)

        print("Dilan dealt " + str(damage) + " damage!")

        return damage
    
    #Fast 9 Move
    
    def fast9():
        print("Dilan used Fast 9!")
        turn = input()

        chance = random.randint(1,18)

        if (chance <= 9):
            damage = (50 * 2) * .09
            print("Dilan dealt " + str(damage) + " damage!")
            return damage

        elif (chance >= 10 and chance <= 15):
            damage = (50 * 4) * .09
            print("Dilan two-starred the move!")
            print("Dilan dealt " + str(damage) + " damage!")
            return damage
        
        elif (chance >= 16):
            damage = (50 * 8) * .09
            print("Dilan three-starred the move")
            print("Dilan dealt " + str(damage) + " damage!")
            return damage
    
    #Hot Wheels Move

    def hotWheels():
        print("Dilan used Hot Wheels!")
        turn = input()

        speed = random.randint(25, 65)
        damage = 50 - (speed / 2)

        print("Dilan hopped on a motorcycle going " + str(speed) + " MPH!")
        print("Dilan dealt " + str(damage) + " damage.")

    #Chug Jug Move    

    def chugJug():
        print("Dilan used Chug Jug!")
        turn = input()

        heal = random.randint(7,32)

        print("Dilan healed " + str(heal) + " HP!")


#Jarod Character Class

class Jarod(Character):
    def __init__(self, name='', HP = 70,):
        super().__init__(name, HP = 70,)

    def JarodMenu():
        print("What will Jarod do?")
        print("1. Help!!!")
        print("2. Flash")
        print("3. Overheat")
        print("4. Sing")


        select = input()

        if (select == 1):
            Jarod.help()

        elif (select == 2):
            Jarod.flash()

        elif (select == 3):
            Jarod.overheat()
        
        elif (select == 4):
            Jordan.bedtime()

        else:
            while (select != 1 or select != 2 or select != 3 or select != 4):
                print("You did not select a move. Please select a move")

                Jarod.JarodMenu()

    #Help!!! Move

    def help():
        gift_prompts = ["Jarod got Ginger Ale! Jarod healed 30 HP", "Jarod got an oatmeal-raisin cookie! Jarod's status effects were cleansed."
                        "Jarod opened Pandora's Box!"]

        print("Jarod cried! HEEELLLLPPPPPP!")
        turn = input()      

        chance = random.randint(1,3)


        if (chance == gift_prompts[0]):
            rodPlay.HP = rodPlay.HP + 30
        
        elif (chance == gift_prompts[1]):
            rodPlay.debuff = False
            
        else:
            print("Pandora's box dropped a bunny farm above Jarod. He is unable to attack!")

    #Flash Move

    def flash():
        print("Jarod used flash! Jarod flashed the room with light")
        turn = input()

        chance = random.randint(0,100)


        if (chance > 70):
            print("Jarod flashed the enemy! TThe enemy is crying!")
            enemy.flash_stat = True
            return enemy.flash_stat

        else:
            print("The move failed...")

    #Overheat Move

    def overheat():
        print("Jarod used overheat")
        turn = input()

        damage = random.randint(15, 25)

        chance = random.randint(1,7)

        if (chance == 1):
            rodPlay.help()

        elif (chance == 2):
            rodPlay.flash()

        elif (chance == 3):
            rodPlay.sing()

        else:
            print("Jarod overheated! Jarod took 30 damage!")
            damage = 30
            return damage

    #Sing Move

    def sing():
        melodies = ["🎤Shawty's like a melody in my head", "🎤I crumble completely when you cry", "🔊**Brazilian Phonk started playing!**"]
        melody = random.choice(melodies)
        damage = 0

        print("Jarod used sing!")
        turn = input()
        

        if (melody == melodies[0]):
            damage = random.randint(5,15)
            print(melody)
            print("Jarod dealt " + str(damage) + " damage!")

            return damage
        
        elif (melody == melodies[1]):
            damage = random.randint(12,26)
            print(melody)
            print("Jarod dealt " + str(damage) + " damage!")
            
            return damage

        elif (melody == melodies[2]):
            damage = random.randint(30,45)
            print(melody)
            print("Jarod dealt " + str(damage) + " damage!")

            return damage  



Bryan.foresight()
Bryan.supernova()
Bryan.brokenRecord()
Bryan.alexaGoodnight()

player = Dilan

player.criticize()
player.fast9() 
player.hotWheels()
player.chugJug()


rodPlay = Jarod
enemy = Jarod

rodPlay.help()
rodPlay.flash()
rodPlay.overheat()
rodPlay.sing()

JordOUT = Jordan            

#Jordan.dynamic() -- NEEDS REWORK
Jordan.hardHatHazard()
Jordan.tarnished()
Jordan.bedtime()



#create a combat loop where stat debuffs get decremented by 1 every turn and debuff boolean determines boolean turn eligbility