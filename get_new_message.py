from telethon import TelegramClient, events
from refresh_bot import refresh
import requests
import config

client = TelegramClient('anon', config.api_id, config.api_hash)

@client.on(events.NewMessage(chats = [544657065]))
async def handler(event):
    # print("Event Occured")
    # print(event.raw_text)
    message = str(refresh(event.raw_text))
    # print(message)
    try:
        url = "https://api.telegram.org/bot5420850636:AAFYY3IdGAUNtVH1WN_vAokk3BEyHWG6iyY/sendMessage?chat_id=-544657065&text={messages}".format(messages=message)
        requests.post(url) # this sends the message
    except:
        print('invalid ticket url')


client.start()
client.run_until_disconnected()