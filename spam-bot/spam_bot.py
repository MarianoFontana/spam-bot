import os

import discord

from events import message


def prepare_client():
    client = discord.Client()

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    message.prepare_client_on_message(client)

    client.run(os.getenv('DISCORD_TOKEN'))


if __name__ == '__main__':
    prepare_client()
