import datetime
from helper import check_status, sent_Telegram
flat = 0
x = datetime.datetime.now()
while True:
    if (check_status() == True):
        if (flat == 0):
            sent_Telegram("Đèn cửa trước đang hoạt động")
            flat = 3
    elif (check_status() == False):
            if (flat == 3):
                sent_Telegram("Đèn cửa trước đã tắt lúc "+ x.strftime("%c"))
                flat = 0