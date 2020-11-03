from telethon import types
from telethon.tl.functions.messages import EditMessageRequest
from settings import api_id, api_hash, sourceChannels, destinationChannels, replacethisusername
import re
from telethon import TelegramClient, events
client = TelegramClient('session', api_id, api_hash)


@client.on(events.NewMessage(outgoing=False))
async def my_event_handler(event):
    if event.chat_id in sourceChannels:
        clipboard = str(event.raw_text)
        replaceList = []
        for item in event.get_entities_text():
            if type(item[0]) == types.MessageEntityMention or type(item[0]) == types.MessageEntityTextUrl or type(item[0]) == types.MessageEntityUrl:
                replaceList.append(item[1])
        for i in replaceList:
            if "@" in i or "t.me" in i:
                clipboard = clipboard.replace(i, replacethisusername)
        for channel in destinationChannels:
            await client.send_message(channel, clipboard)

client.start()
client.run_until_disconnected()
