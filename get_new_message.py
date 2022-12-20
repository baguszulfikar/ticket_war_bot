from telethon import TelegramClient, events
from refresh_bot import refresh
import requests

api_id = '23686234'
api_hash = '387e4e5cbbaf01807ba972155c7f0c0f'
client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage(chats = [544657065]))
async def handler(event):
    # print("Event Occured")
    # print(event.raw_text)
    message = str(refresh(event.raw_text))
    # print(message)
    url = "https://api.telegram.org/bot5420850636:AAFYY3IdGAUNtVH1WN_vAokk3BEyHWG6iyY/sendMessage?chat_id=-544657065&text={messages}".format(messages=message)
    print(requests.post(url)) # this sends the message


client.start()
client.run_until_disconnected()