import discord
import asyncio
import random
from random import choice
from discord.ext.commands import Bot
from discord.ext import commands
import os
client = discord.Client()

# Liste de mots interdits
ban_words = ['motInterdit1', 'motInterdit2', 'motInterdit3']

# Première liste -> dans le fichier
list1 = []
# Deuxième liste -> liens dans le code
list2 = ['https://i.goopics.net/lvPRx.png', 'https://i.goopics.net/lvPRx.png', 'https://i.goopics.net/lvPRx.png', 'https://i.goopics.net/lvPRx.png', 'https://i.goopics.net/lvPRx.png']

# Fonction qui ouvre le fichier 
with open('img_list.txt', 'r') as f:
  content = f.readlines()
  for x in content:
    row = x.split()
    list1.append((row[0]))


# Fonction de sélection d'image random
def selectRandom(img):
    return random.choice(img)

@client.event
# Fonction pour le démarrage du bot
async def on_ready ():
    # Écrit dans la console
    print( "Programme lancé !" )
    # Il n'est pas obligatoire d'indiquer que le bot est lancé
    # Sélection d'un salon sur Discord (identifiant du salon)
    channelMe = client.get_channel(IdentifiantDuSalon)
    # Envoie le message dans le salon sélectionné
    await channelMe.send("Je suis lancé !")
    # Définit l'activité
    activity = discord.Game(name="Activité quelconque", type=3)
    # Définit le status
    await client.change_presence(status=discord.Status.online, activity=activity)


client.event
# Fonction de réponse aux messages
async def on_message (message):
    print(message.content)

@client.event
async def on_message (message):
    # Si le message est +bonjour, le bot répondra par "Bonjour"
    if message.content == "+bonjour":
        await message.channel.send("Bonjour")
    # Si le message est +img1, le bot répondra par une image random dans le fichier
    if message.content == "+img1":
        await message.channel.send(selectRandom(list1))
    # Si le message est +img2, le bot répondra par une image dans la liste
    if message.content == "+img2":
        await message.channel.send(selectRandom(list2))


# Détectes un mot interdit et le supprime
if message.author != client.user :
        for word in ban_words:
            if word in message.content.lower():
                await message.delete()
                await message.author.send("L'utilisation de ce mot (" + word + ") est interdit.")

                break

# Indiquer le token de votre bot pour qu'il fonctionne
client.run('VotreToken')
