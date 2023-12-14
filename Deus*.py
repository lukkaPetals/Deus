import discord
import json


with open('a.json') as f:
    # Carrega os dados do JSON
    dados = json.load(f)

token = dados['TOKEN']


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logou como {self.user}!')

    async def on_message(self, message):
        if 'deus' in message.content:
            await message.reply ("Deus*")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
