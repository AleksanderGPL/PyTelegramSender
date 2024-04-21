import json
import http.client
global tg


def tgconfigcheck():
    try:
        with open('telegram.json', 'r') as file:
            global tg
            tg = json.load(file)
            print("\033[1;32;40mToken: " + tg['token'])
            print("Chat ID: " + tg['chatid'] + "\n")
    except:
        print("\033[1;31;40mFile telegram.json is incorrect or missing. Running configuration")
        token = input("\033[1;34;40mTelegram Bot Token: ")
        chatid = input("Telegram Chat ID: ")
        with open('telegram.json', 'w') as file:
            json.dump({'token': token, 'chatid': chatid}, file)
        print("Configuration saved.")
        tgconfigcheck()


tgconfigcheck()

message = input("Message: ").replace(" ", "+")
print("\033[1;33;40mSending message to Telegram...")
(http.client.HTTPSConnection('api.telegram.org').request
 ('GET', f'/bot{tg['token']}/sendMessage?chat_id={tg['chatid']}&text={message}'))
