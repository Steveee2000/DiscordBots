import discord

TOKEN = "OTQwNzg0MzM0MDc4NjExNTU2.YgMbsA.TIGjhkyGc7lB03uTFWupm47oYiA"

client = discord.Client()

@client.event
async def on_ready():
    print("{1,574.user} is now online!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Xin Chào Dốc Cơ!')

client.run(TOKEN)
