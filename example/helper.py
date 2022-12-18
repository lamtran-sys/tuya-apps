import telegram
from tuya_iot import (
    TuyaOpenAPI,
    AuthType
)
import time
ACCESS_ID = "4grcdre745am7gsgn5tr"
ACCESS_KEY = "05229cd39716471fb999443766854e77"
USERNAME = "tranlam.thkg@gmail.com"
PASSWORD = "Lamtran_12345"
ASSET_ID = "1566698371908299"
DEVICE_ID = "eb7dd6c760d1d6563dp9mh"
ENDPOINT = "https://openapi.tuyaus.com"


## check status
def check_status():
    openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY, AuthType.CUSTOM)
    openapi.connect(USERNAME, PASSWORD)
#   bot.send_message(chat_id=usr_id, text="Đèn cửa đang bật")
    return openapi.get("/v1.0/iot-03/devices/{}/status".format(DEVICE_ID))['result'][0]['value']
def time_sleep(num):
    time.sleep(num)

def sent_Telegram(hello):
    ###Telegram botinfo
    api_key = "23672589"
    usr_id = "-1001841516459"
    bot = telegram.Bot(token="5642058934:AAE6aIn9GBVJhnt8L8JpofyBPL8R3u2QodQ")
    ###Actionsent
    bot.send_message(chat_id=usr_id, text=hello)

# sent action to switch -
# commands = {'commands': [{'code': 'switch_1', 'value': False}]}
# print(commands)
# request = openapi.post(f'/v1.0/iot-03/devices/{DEVICE_ID}/commands', commands)
# importing all required libraries
# get your api_id, api_hash, token
# from telegram as described above
