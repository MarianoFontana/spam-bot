import constants
from stats import message as message_stats


def prepare_client_on_message(client):

    @client.event
    async def on_message(message):
        if message.content.startswith(constants.SPAM_BOT_ID):
            await _handle_active_message(message)
        else:
            _handle_passive_message(message)


ACTIONS = {
    'word-count': message_stats.show_word_count,
}


async def _handle_active_message(message):
    await message.channel.send('AYE SIR!')
    await ACTIONS[_get_message_action(message)](message)


def _handle_passive_message(message):
    message_stats.update_word_count(message)


def _get_message_action(message):
    return message.content.split(' ')[1]
