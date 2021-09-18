from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import csv
import schedule, time

api_id = XXXXXXX
api_hash = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
phone = '+34600000000'
client = TelegramClient(phone, api_id, api_hash)

def pole_canaria():
    print("Pole Canaria 1")
    client.send_message(entity=0000000, message="pole canaria")
    time.sleep(1)
    print("Pole Canaria 2")
    client.send_message(entity=0000000, message="pole canaria")

def pole():
    print("Pole 1")
    client.send_message(entity=0000000, message="pole")
    time.sleep(0.5)
    print("Pole 2")
    client.send_message(entity=0000000, message="pole")
    time.sleep(1)
    print("Subpole")
    client.send_message(entity=0000000, message="subpole")
    time.sleep(1)
    print("Fail")
    client.send_message(entity=0000000, message="fail")

def pole_andaluza():
    print("Pole Andaluza 1")
    client.send_message(entity=0000000, message="pole andaluza")
    time.sleep(1)
    print("Pole Andaluza 2")
    client.send_message(entity=0000000, message="pole andaluza")

print("PoleBOT Launched. Loading credentials and connecting to the Telegram API to POLE EVERYONE")
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

print("PoleBOT loaded successfully")
schedule.every().day.at("01:00").do(pole_canaria)
schedule.every().day.at("00:00").do(pole)
schedule.every().day.at("12:00").do(pole_andaluza)

while True:
    schedule.run_pending()
    time.sleep(0.1)
