import discord
import os
from datetime import datetime
from keep_alive import keep_alive
from commands import *

class MyClient(discord.Client):

    async def on_ready(self):
        print('----------------------------------------------')
        print(f'Logged in as {self.user}, id = {self.user.id}')
        print('----------------------------------------------')

    async def on_message(self, message):
        # Para o bot não se auto responder
        if message.author.id == self.user.id:
            return

        if message.content == message.content:
          await say_hello(message)
          await reply_embed(message)
          await say_ping(message, client)


keep_alive()

client = MyClient()
my_secret = os.environ['$token']
client.run(my_secret)

