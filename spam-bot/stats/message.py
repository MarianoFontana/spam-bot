WORD_COUNT = {}


def update_word_count(message):
    user_word_count = WORD_COUNT.setdefault(message.author, {})
    for word in message.content.split(' '):
        user_word_count[word] = user_word_count.get(word, 0) + 1


async def show_word_count(message):
    user_word_count = WORD_COUNT.setdefault(message.author, {})
    await message.channel.send(str(user_word_count))
