#imports Discord to join the python code with the bot
import typing
import discord 
from discord.ext import commands
import sqlite3


intents = discord.Intents.default()
intents.members = True

#Used to summon the Discord Bot
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("The bot is now ready for use")
    print("----------------------------")


#Response command for !hello
@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am the Haramemes bot")

@client.command()
async def goodbye(ctx):
    await ctx.send("Goodbye")

@client.command()
async def characters(ctx):
    await ctx.send("""What character would you like to know about?
                   1. Bryan
                   2. Dilan
                   3. Giana
                   4. Jarod
                   5. Jayson
                   6. Jordan
                   7. Yassine""")
    

    
@client.command()
async def BryanInfo(ctx):
    await ctx.send("""Bryan is a mental fighter, using his mind to distribute attacks that deal 
heavy damage. However, he is very susceptible to critical hits. While he may
be less likely to be critically hit, these kinds of attacks will one-hit K.O. him.

                   
--Stats--
HP: 50
Fighter Type: Mental
Strength: Pyrokinetic attacks that can have status effects, less prone to crit. attacks
Weakness: Gets one-hit K.O.'d to critical attacks
                   
--Moves--
Foresight - Majority chance to predict your opponent's next move. If successful,
negate their turn and deal damage
Supernova - Fire a concussive blast at the opponent that never misses. A small
chance to cause concussion
Broken Record - Engage in a symphony, dealing damage up to 2-6 times
Alexa - Summon Alexa. She will obscure light, healing Bryan for a random amount of health""")
    
                
    
@client.command()
async def DilanInfo(ctx):
    await ctx.send("""Dilan is an all-around fighter. He has above average attack damage and attack power and
will always strike first in combat. However, he is void of the ability to strike critically.
                   
--Stats--
HP: 65
Fighter Type: All-Arounder
Strength: Above Average Stats
Weakness: Inability to critically strike
                   
                   
--Moves--
Criticize - Summon Yassine to yell at him. The sound from the blast will cause
an audio wave to hit the opponent. This attack varies in power.
Fast 9 - Fire a deck of cards at your opponent. There is a chance to 2-star and 3-star the move,
which will add a multiplyer to damage.
Hot Wheels - Ride a motorcycle at full speed into the opponent. A small chance to cause
concussion.
Chug - Drink a bottle of alcohol. This will increase stats for the rest of combat, but
will cost half of your HP. Dilan can no longer strike first upon use.""")
    
@client.command()
async def GianaInfo(ctx):
    await ctx.send("""Giana is a status effect fighter. While she may have lackluster health and attack stats,
she thrives on emitting status effects. Taking advantage of her great moveset with a 
bit of luck can ensure a strategic victory.

--Stats--
HP: 25
Fighter Type: Status Inflictor
Strength: High probability and armament of status effects
Weakness: Low HP and attack stats

--Moves--
@ everyone - Spam your opponents cell phone by tagging everyone in their contacts.
This concusses your opponent for 2-4 rounds. It may backfire.
Ramble - Blather your opponent into oblivion. Has a chance to cause confusion. 
Party Time! - Summon a rave, trampling your opponent. Attacks received are halved until
the party ends
Minimize - Shrink by a considerable amount. Sneak behind the opponent to deal a 
sneak attack. Causes damage equal to HP amount.
""")
    
@client.command()
async def JarodInfo(ctx):
    await ctx.send("""Jarod is an all-around fighter. He starts off strong with decent health stats
and good moves. He is susceptible to Air Lock, which makes him severely prone to status effects.

--Stats--
HP: 70
Fighter Type: All-Arounder
Strength: Above Average Stats
Weakness: Prone to Air Lock and status effects
Crit Rate: 25%

--Moves--
Help!!! - Randomly pick 1 of 3 gifts, containing Ginger Ale which heals HP,
an oatmeal-raisin cookie which heals status effects, or a pandora's box which
traps Jarod in a bunny farm, negating his turn.
Victimize - Prey upon your opponent, distributing any status effects from Jarod to them
Overheat - Strike two times. The first hit is a fixed damage attack. The second allows Jarod a chance
to use another random move or take recoil damage instead.
Sing - Sing a random melody.
""")
    
@client.command()
async def JaysonInfo(ctx):
    await ctx.send("""Jayson is a physical fighter. While his attack stats aren't the highest at the start
of combat, they start to scale the longer the battle goes on. Jayson also has increased
durability, taking less damage per attack.

--Stats--
HP: 80
Fighter Type: Physical
Strength: Durability, scaling fighting stats
Weakness: Weak Starting Stats

--Moves--
Sarcasm - Demean the damage of your oppnent's attacks. Take less damage
from all attacks for the remainder of combat.
Picky Eater - The move most recently used on Jayson is now disabled for
the rest of combat. Can only be used once per combat.
Knife Onslaught - Equip a butterfly knife and perform a random move. The more times its used,
the more times it can strike.
MMMMMMM - Use one move tha can vary from every character's moveset. The move chosen
is completely random.
""")
    
@client.command()
async def JordanInfo(ctx):
    await ctx.send("""JJordan is a physical fighter. He deals a lot of attack damage
through critical hit strikes. Unfortunately, Jordan is affected by copium,
causing severe inaccuracy when landing attacks.

--Stats--
HP: 85
Fighter Type: Physical
Strength: Great critical hit rate
Weakness: Prone to copium and inaccuracy 
Crit Rate: 50%

--Moves--
Dynamic- Blasts your opponent with dynamic microphone sound. Using the move
more boosts its power
Hard Hat Hazard - Put on a hard hat and ram head-first into your opponent
Tarnished - A two part move that deals weak damage on the first hit, but deals
heavy damage on the second hit if it doesn't miss
Go To Bed - Tell your opponent to sleep. If successful, the opponent will
be put to sleep. If the move fails, Jordan will be put to sleep.
""")
    

@client.command()
async def SviatInfo(ctx):
    await ctx.send("""Sviat is a physical fighter. His moves have the capability to
maintain a high ceiling damage output. However, they are matched with a low damage floor
output if your opponent uses the right moves or if luck isn't on your side.

--Stats--
HP: 75
Fighter Type: Physical
Strength: High Damage Ceiling
Weakness: Low Damage Ceiling

--Moves--
Bench Press - Lift your opponent into the air, bench pressing them before slamming
them into the ground.
Pharmaceutical - Ingest a random drug. Testosterone gel increases attack damage, ketamine will 
incapacitate Sviat for one round, naloxone will nullify any status effects on Sviat,
sertraline will heal Sviat for a random amount, vicodin will nullify a majority portion of damage taken for 2 rounds
AFK - Forfeit your current and next turn to scroll on TikTok. Any damage taken between 2 rounds will be dealt
back to your opponent with a damage multiplier
Zrada - Wait for your opponent to strike. There is a chance to either counter any damage taken while receiving
half the output, a chance to prevent the move used against you to be used for the rest of combat, or a chance
for the move to fail.
""")
    
@client.command()
async def YassineInfo(ctx):
    await ctx.send("""Yassine is a copper fighter. While he doesn't have any apparent strenghts
in combat, his copper status will affect combat negatively. Yassine is the 
"Hard Difficulty" character.

--Stats--
HP: 60
Fighter Type: Copper
Strength: None
Weakness: Copper status, which may inflict self-damage,
stat weakening, or turn skipping 
Crit Rate: 20%

--Moves--
Tilt - Unleash a fit of rage, damaging your opponent's mental state.
Has a chance to self-inflict damage.
Lock-In - Enter a trance, where you attack your opponent in another realm.
Has a high chance of missing.
Camera Shy - Use a webcam to project images of Yassine, reducing 
opponent accuracy.
Carcinogen - Smoke a cloud that your opponent breathes in. Use of this
move inflicts poison on both Yassine and his opponent.  
""")


#@client.command()
#async def help(ctx):
    #await ctx.send("""This bot is created to emulate an RPG for Haramemes. You may select from a series of Haramemes members, each with unique
                  # fighting capabilities and weaknesses. You must win 3 rounds against random opponents to claim your title as The Almighty.
                   #If your HP reaches 0 at any point, you lose and must restart from the beginning.""")

#Discord Events

@client.event
async def on_member_join(member):
    channel = client.get_channel("CHANNEL ID")
    await channel.send("Welcome")

@client.event
async def on_member_remove(member):
    channel = client.get_channel("CHANNEL ID")
    await channel.send(member + "has been removed")


client.run('TOKEN')


