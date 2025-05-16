import discord
import asyncio
from discord.ext import commands
from discord import SelectOption, SelectMenu, Interaction

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

allergy_symptoms = ["sneezing", "runny nose", "congestion", "cough", "wheezing", "shortness of breath", "itchy eyes", "hives", "rash", "itchiness"]
conjunctivitis_symptoms = ["redness", "discharge", "sensitivity to light", "swelling", "blurred vision"]
diarrhea_symptoms = ["stomach cramps", "stomach pain", "nausea", "vomiting", "blood in the stool", "mucus in the stool"]
fever_symptoms = ["elevated body temperature", "sweating", "chills", "muscle aches", "loss of appetite"]
headache_symptoms = ["sharp pain in the head", "throbbing sensation in the head", "dull ache", "head pain"]
pain_symptoms = ["pain", "pain in a specific area of the body"]
visceral_pain = ["visceral", "visceral pain" "organ", "organs", "heart", "stomach", "pancreas", "liver", "vessel", "vessels", "blood vessels", "chest", "abs", "abdomen"]
somatic_pain = ["somatic", "somatic pain", "head", "skin", "muscle", "muscles", "bone", "bones"]

def refine_list(list, input):
    char_remove_list = [word for word in list if word not in input]
    cap_list = [s.capitalize() for s in char_remove_list]

    for index, item in enumerate(cap_list):
        cap_list[index] = "-" + item
    return cap_list

@bot.event
async def on_ready():
    print(f'Client has logged on as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! Latency: {round(bot.latency * 1000)}ms')

#Allergy diagnosis embed results
@bot.command()
async def allergy_diagnosis(ctx):
    embed = discord.Embed(title = "Allergies", url = "https://www.mayoclinic.org/diseases-conditions/allergies/symptoms-causes/syc-20351497", 
                        description = "R.E.M.E.D.Y. Bot has diagnosed you with allergies.")
    embed.set_thumbnail(url = "https://i.ibb.co/wrbnVBh7/R-E-M-E-D-Y-Bot-Allergy-Diagnose-Thumbnail.jpg")
    embed.add_field(name = 'What are allergies?', value = 'Allergies are a reaction from the immune system to a foreign substance that gets inside the body.')
    await ctx.send(embed = embed)

#Allergy remedy results
@bot.command()
async def allergy_remedy(ctx):
    embed = discord.Embed(title = "Allergy Remedy - Zyrtec/Ceritizine", description = """
                        **Dosage**
                        __Adults under 65 and children 6 years and older__ - 10 miligrams (mg) every day
                        __Children under 6 years of age__ - Ask a doctor
                        __Adults 65 and older__ - Ask a doctor
                        __Consumers with liver or kidney disease__ - Ask a doctor""", url = "https://www.zyrtec.com/products/zyrtec-dosage-guide")
    embed.set_thumbnail(url = "https://i.ibb.co/xS97F6bz/R-E-M-E-D-Y-Bot-Thumbnail-Allergy-Remedy.jpg")
    await ctx.send(embed = embed)

#Conjunctivitis Diagnosis Results
@bot.command()
async def conjunctivitis_diagnosis(ctx):
    embed = discord.Embed(title = "Conjunctivitis", url = "https://www.mayoclinic.org/diseases-conditions/pink-eye/symptoms-causes/syc-20376355",
                        description = "R.E.M.E.D.Y. Bot has diagnosed you with conjunctivitis")
    embed.set_thumbnail(url = "https://i.ibb.co/wFMBxn84/R-E-M-E-D-Y-Bot-Thumbnail-Conjunctivitis-Diagnosis.jpg")
    embed.add_field(name = 'What is conjunctivitis?', value = "Conjunctivitis, also known as pink eye, is a redness in the conjunctiva [the white part of the eye].")
    await ctx.send(embed = embed)

#Conjunctivitis Remedy Results
@bot.command()
async def conjunctivitis_remedy(ctx):
    embed = discord.Embed(title = "Conjunctivitis Remedy - Pataday/Olopatadine", description = """
                        **Dosage**
                        __Adults and children 2 years and older__ - Instill 1 drop in each affected eye two times a day, at least 6 to 8 hours apart
                          
                        **Stop use and see a doctor if you experience any of the following:**
                        -Blurred vision
                        -Burning, dryness, or stinging of the eye
                        -Eye redness, irritation, or pain
                        -Swelling of the eyelid, face, lips, or feet'
                        -Trouble breathing""", 
                        url = "https://www.mayoclinic.org/drugs-supplements/olopatadine-ophthalmic-route/description/drg-20067387")
    embed.set_thumbnail(url = "https://i.ibb.co/TDgsDTCn/R-E-M-E-D-Y-Bot-Thumbnail-Conjunctivitis-Remedy.webp")
    await ctx.send(embed = embed)

#Diarrhea Diagnosis Results
@bot.command()
async def diarrhea_diagnosis(ctx):
    embed = discord.Embed(title = "Diarrhea", url = "https://www.mayoclinic.org/diseases-conditions/diarrhea/symptoms-causes/syc-20352241",
                        description = "R.E.M.E.D.Y. Bot has diagnosed you with diarrhea")
    embed.set_thumbnail(url = "https://i.ibb.co/209fH4Nh/R-E-M-E-D-Y-Bot-Thumbnail-Diarrhea-Diagnosis.jpg")
    embed.add_field(name = 'What is diarrhea?', value = "Diarrhea is the concept of loose, watery and possibly more frequent passage of stool.")
    await ctx.send(embed = embed)

#Diarrhea Remedy Results
@bot.command()
async def diarrhea_remedy(ctx):
    embed = discord.Embed(title = "Diarrhea Remedy - Imodium/Loperamide", description = """
                        **Dosage**
                        Dosing For Acute Diarrhea
                        __Adults and children 13 years of age or older__ - At first, 4 miligrams (mg) after the first loose bowel movement, then 2 miligram (mg)
                        after each loose bowel movement after the first dose has been taken. No more than 16 miligrams (mg).
                        __Children 8 to 12 years of age weighing more than 30 kilograms (kg)__ - 2 miligrams (mg) 3 times a day.
                        __Children 6 to 8 years of age weighing 20 to 30 kg__ — 2 miligrams (mg) 2 times a day.
                        __Children 2 to 5 years of age weighing 20 kg or less__ — Use the oral solution.
                        __Children younger than 2 years of age__ — Use is not recommended.

                        Dosing For Oral Solution
                        __Children 8 to 12 years of age weighing more than 30 kilograms__ (kg) — 2 teaspoonfuls (2 mg) 3 times a day.
                        __Children 6 to 8 years of age weighing 20 to 30 kg — 2 teaspoonfuls__ (2 mg) 3 times a day.
                        __Children 2 to 5 years of age weighing 13 to 20 kg — 1 teaspoonful__ (1 mg) 3 times a day.
                        __Children younger than 2 years of age__ — Use is not recommended.

                        Dosing for Oral Tablets
                        __Adults and teenagers__ - The usual dose is 4 miligrams (mg) after the first loose bowel movement, and 2 miligrams (mg) 
                        after each loose bowel movement after the first dose has been taken. No more than 8 miligrams (mg) should be taken in any 24-hour period.
                        __Children 9 to 11 years of age__ — The usual dose is 2 miligrams (mg) after the first loose bowel movement, and 1 miligram (mg) 
                        after each loose bowel movement after the first dose has been taken. No more than 6 miligrams (mg) should be taken in any 24-hour period.
                        __Children 6 to 8 years of age__ — The usual dose is 2 miligrams (1 tablet) after the first loose bowel movement, and 1 miligram (mg) 
                        after each loose bowel movement after the first dose has been taken. No more than 4 miligrams (mg) should be taken in any 24-hour period.
                        __Children up to 6 years of age__ — Use is not recommended unless directed by your doctor.""", 
                        url = "https://www.mayoclinic.org/drugs-supplements/loperamide-oral-route/description/drg-20064573")
    embed.set_thumbnail(url = "https://i.ibb.co/yF48B1zq/R-E-M-E-D-Y-Bot-Thumbnail-Diarrhea-Remedy.jpg")
    await ctx.send(embed = embed)

#Fever Diagnosis Results
@bot.command()
async def fever_diagnosis(ctx):
    embed = discord.Embed(title = "Fever", url = "https://www.mayoclinic.org/diseases-conditions/fever/symptoms-causes/syc-20352759",
                        description = "R.E.M.E.D.Y. Bot has diagnosed you with a fever")
    embed.set_thumbnail(url = "https://i.ibb.co/KzjJqKZ9/R-E-M-E-D-Y-Bot-Results-Thumbnail-1.jpg")
    embed.add_field(name = 'What is a fever?', value = "A fever is a rise in body temperature above the normal range (98.6°F/37°C)")
    await ctx.send(embed = embed)

#Fever Remedy Results
@bot.command()
async def fever_remedy(ctx):
    embed = discord.Embed(title = "Fever Remedy - Tylenol/Acetaminophen", description = """
                        **Dosage**
                        __Adults and teenagers__ - 650 to 1000 miligrams (mg) every 4 to 6 hours as needed
                        __Children 11 to 12 years__ - 320 to 480 miligrams (mg) every 4 to 6 hours as needed
                        __Children 9 to 11 years__ - 320 to 400 miligrams (mg)
                        __Children 6 to 9 years__ - 320 miligrams (mg) every 4 to 6 hours as needed
                        __Children 4 to 6 years__ - 240 miligrams (mg) every 4 to 6 hours as needed
                        __Children 2 to 4 years__ 160 miligrams (mg) every 4 to 6 hours as needed
                        __Children under 2 years of age__ - Use and dose must be determined by your doctor""", 
                        url = "https://www.mayoclinic.org/drugs-supplements/acetaminophen-oral-route-rectal-route/description/drg-20068480")
    embed.set_thumbnail(url = "https://i.ibb.co/84cDD23H/R-E-M-E-D-Y-Bot-Thumbnail-Fever-Remedy.jpg")
    await ctx.send(embed = embed)



#Headache Diagnosis Results
@bot.command()
async def headache_diagnosis(ctx):
    embed = discord.Embed(title = "Headache", url = "https://www.mayoclinic.org/departments-centers/headache-subspecialty-group/overview/ovc-20443693",
                        description = "R.E.M.E.D.Y. Bot has diagnosed you with a headache")
    embed.set_thumbnail(url = "https://i.ibb.co/rKtnYpnV/R-E-M-E-D-Y-Bot-Thumbnail-Headache-Diagnosis.jpg")
    embed.add_field(name = 'What is a headache', value = "A headache is a pain in any region of the head.")
    await ctx.send(embed = embed)

#Headache Remedy Results
@bot.command()
async def headache_remedy(ctx):
    embed = discord.Embed(title = "Headache Remedy - Bayer/Aspirin", description = """
                        **Dosage**
                        __Adults and children 12 years and over__ - 325 miligrams (mg) to 650 miligrams (mg) every 4 hours. Do not exceed 12 tablets in 24 hours.
                        __Children under 12 years__ - Consult a doctor""", 
                        url = "https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=f7a5d612-443c-4701-ad3b-8eb53c87bece")
    embed.set_thumbnail(url = "https://i.ibb.co/mrB00XtF/R-E-M-E-D-Y-Bot-Thumbnail-Headache-Remedy.jpg")
    await ctx.send(embed = embed)

#Pain Diagnosis Results
@bot.command()
async def pain_diagnosis(ctx):
    embed = discord.Embed(title = "Pain", url = "https://medlineplus.gov/pain.html#:~:text=Pain%20is%20a%20signal%20in,may%20be%20mild%20or%20severe.",
                          description = "R.E.M.E.D.Y. Bot has diagnosed you with pain")
    embed.set_thumbnail(url = "https://i.ibb.co/jZfQMzR8/R-E-M-E-D-Y-Bot-Thumbnail-Pain-Diagnosis.jpg")
    embed.add_field(name = 'What is pain?', value = "Pain is a signal in your nervous system that something may be wrong. " \
    "It is an unpleasant feeling, such as a prick, tingle, sting, burn, or ache")
    await ctx.send(embed = embed)

#Pain Remedy Results
@bot.command()
async def pain_remedy(ctx):
    embed = discord.Embed(title = "Remedy - Motrin/Ibuprofen", description = """
                        **Dosage**
                        For mild to moderate pain:
                        __Adults and teenagers__ — 400 milligrams (mg) every four to six hours, as needed.
                        __Children over 6 months of age__ — Dose is based on body weight and must be determined by your doctor. 
                        __The dose usually is 10 milligrams__ (mg) per kilogram (kg) of body weight every six to eight hours, as needed, up to 40 mg per kg per day.
                        __Infants younger than 6 months of age__ — Use and dose must be determined by your doctor.
                          
                        For menstrual cramps:
                        __Adults__ — 400 milligrams (mg) every four hours, as needed
                        __Children__ — Use and dose must be determined by your doctor""",
                        url = "https://www.mayoclinic.org/drugs-supplements/ibuprofen-oral-route/description/drg-20070602")
    embed.set_thumbnail(url = "https://i.ibb.co/Z6rZ2mk9/R-E-M-E-D-Y-Bot-Thumbnail-Pain-Remedy.jpg")
    await ctx.send(embed = embed)



#The diagnose command will summon the bot to begin diagnosing based off patient symptoms
@bot.command()
async def diagnose(ctx):
    await ctx.send(f'Hello, I am the R.E.M.E.D.Y. Bot. I can assist you with a diagnosis and recommend a remedy for it.'
                   'What symptom are you mainly experiencing?')
    
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel 

    try:
        message = await bot.wait_for('message', check = check)
    except asyncio.TimeoutError:
        await ctx.send("You took too long to respond. The command has closed.")
    
    #Allergy condition
    if any(item in str(message.content.lower()) for item in allergy_symptoms):
        await ctx.send("Thank you for sharing your symptoms. To help me with your diagnosis, please tell me if you've experienced any of the following symptoms below:")

        allergy_list_refined = refine_list(allergy_symptoms, message.content)
   
        await ctx.send('\n'.join(allergy_list_refined))

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        
        try:
            message = await bot.wait_for('message', check = check)
        except asyncio.TimeoutError:
            await ctx.send("You took too long to respond. The command has closed.")

        if message.content.lower() == "yes":
            await ctx.invoke(bot.get_command('allergy_diagnosis'))
            await ctx.invoke(bot.get_command('allergy_remedy'))
        
        else:
            await ctx.send("It seems that R.E.M.E.D.Y. Bot was unable to diagnose you. Please reach out to your primary care provider for support. Feel better.")

    #Conjunctivitis condition
    elif any(item in str(message.content) for item in conjunctivitis_symptoms):
        await ctx.send("Thank you for sharing your symptoms. To help me with your diagnosis, please tell me if you've experienced any of the following symptoms below:")

        conjunctivitis_list_refined = refine_list(conjunctivitis_symptoms, message.content)

        await ctx.send('\n'.join(conjunctivitis_list_refined))

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
    
        try:
            message = await bot.wait_for('message', check = check)
        except asyncio.TimeoutError:
            await ctx.send("You took too long to respond. The command has closed.")

        if message.content.lower() == "yes":
            await ctx.invoke(bot.get_command('conjunctivitis_diagnosis'))
            await ctx.invoke(bot.get_command('conjunctivitis_remedy'))

        else:
            await ctx.send("It seems that R.E.M.E.D.Y. Bot was unable to diagnose you. Please reach out to your primary care provider for support. Feel better.")

    #Diarrhea Condition
    elif any(item in str(message.content) for item in diarrhea_symptoms):
        await ctx.send("Thank you for sharing your symptoms. To help me with your diagnosis, please tell me if you've experienced any of the following symptoms below:")

        diarrhea_list_refined = refine_list(diarrhea_symptoms, message.content)

        await ctx.send('\n'.join(diarrhea_list_refined))

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
    
        try:
            message = await bot.wait_for('message', check = check)
        except asyncio.TimeoutError:
            await ctx.send("You took too long to respond. The command has closed.")

        if message.content.lower() == "yes":
            await ctx.invoke(bot.get_command('diarrhea_diagnosis'))
            await ctx.invoke(bot.get_command('diarrhea_remedy'))

        else:
            await ctx.send("It seems that R.E.M.E.D.Y. Bot was unable to diagnose you. Please reach out to your primary care provider for support. Feel better.")

    #Fever condition
    elif any(item in str(message.content) for item in fever_symptoms):
        await ctx.send("Thank you for sharing your symptoms. To help me with your diagnosis, please tell me if you've experienced any of the following symptoms below:")

        fever_list_refined = refine_list(fever_symptoms, message.content)

        await ctx.send('\n'.join(fever_list_refined))

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
    
        try:
            message = await bot.wait_for('message', check = check)
        except asyncio.TimeoutError:
            await ctx.send("You took too long to respond. The command has closed.")

        if message.content.lower() == "yes":
            await ctx.invoke(bot.get_command('fever_diagnosis'))
            await ctx.invoke(bot.get_command('fever_remedy'))

        else:
            await ctx.send("It seems that R.E.M.E.D.Y. Bot was unable to diagnose you. Please reach out to your primary care provider for support. Feel better.")

    #Headache condition
    elif any(item in str(message.content) for item in headache_symptoms):
        await ctx.send("Thank you for sharing your symptoms. To help me with your diagnosis, please tell me if you've experienced any of the following symptoms below:")

        headache_list_refined = refine_list(headache_symptoms, message.content)

        await ctx.send('\n'.join(headache_list_refined))

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
    
        try:
            message = await bot.wait_for('message', check = check)
        except asyncio.TimeoutError:
            await ctx.send("You took too long to respond. The command has closed.")

        if message.content.lower() == "yes":
            await ctx.invoke(bot.get_command('headache_diagnosis'))
            await ctx.invoke(bot.get_command('headache_remedy'))

        else:
            await ctx.send("It seems that R.E.M.E.D.Y. Bot was unable to diagnose you. Please reach out to your primary care provider for support. Feel better.")

    #Pain condition
    elif any(item in str(message.content) for item in pain_symptoms):
        await ctx.send("Thank you for sharing your symptoms. Is your pain somatic(skin, muscles, bones, and joints) or is it visceral(internal organs)?")

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel

        try:
            message = await bot.wait_for('message', check = check)
        except asyncio.TimeoutError:
            await ctx.send("You took too long to respond. The command has closed.")

        if any(item in str(message.content) for item in somatic_pain):   
            await ctx.send("Are you experiencing any symptoms of head pain?")

            headache_list_refined = refine_list(headache_symptoms, message.content)

            await ctx.send('\n'.join(headache_list_refined))

            def check(message):
                return message.author == ctx.author and message.channel == ctx.channel
            
            try:
                message = await bot.wait_for('message', check = check)
            except asyncio.TimeoutError:
                await ctx.send("You took too long to respond. The command has closed.")

            if message.content.lower() == "yes":
                await ctx.invoke(bot.get_command('headache_diagnosis'))
                await ctx.invoke(bot.get_command('headache_remedy'))

            else:
                await ctx.send("It seems that R.E.M.E.D.Y. Bot was unable to diagnose you. Please reach out to your primary care provider for support. Feel better.")
        
        elif any(item in str(message.content) for item in visceral_pain):
            await ctx.send("Are you experiencing any stomach pain?")

            def check(message):
                return message.author == ctx.author and message.channel == ctx.channel

            try:
                message = await bot.wait_for('message', check = check)
            except asyncio.TimeoutError:
                await ctx.send("You took too long to respond. The command has closed.")

            if message.content.lower() == "yes":
                await ctx.send("Are you experiencing any of the other symptoms that can relate to stomach pain presented below?:")

                diarrhea_list_refined = refine_list(diarrhea_symptoms, message.content)

                await ctx.send('\n'.join(diarrhea_list_refined))

                def check(message):
                    return message.author == ctx.author and message.channel == ctx.channel
            
                try:
                    message = await bot.wait_for('message', check = check)
                except asyncio.TimeoutError:
                    await ctx.send("You took too long to respond. The command has closed.")

                if message.content.lower() == "yes":
                    await ctx.invoke(bot.get_command('diarrhea_diagnosis'))
                    await ctx.invoke(bot.get_command('diarrhea_remedy'))
                    return

                else:
                    await ctx.send("It seems that R.E.M.E.D.Y. Bot was unable to diagnose you. Please reach out to your primary care provider for support. Feel better.")
                    return
            
            else:
                await ctx.invoke(bot.get_command('pain_diagnosis'))
                await ctx.invoke(bot.get_command('pain_remedy'))

        else:
            await ctx.send("It seems that R.E.M.E.D.Y. Bot was unable to diagnose you. Please reach out to your primary care provider for support. Feel better.")

    else:
        await ctx.send("It seems that R.E.M.E.D.Y. Bot was unable to diagnose you. Please reach out to your primary care provider for support. Feel better.")

bot.run('')