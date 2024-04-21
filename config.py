import json
print("\033[1;32;40mConfiguration\033[1;34;40m")
token = input("Telegram Bot Token: ")
chatid = input("Telegram Chat ID: ")
with open('telegram.json', 'w') as file:
    json.dump({'token': token, 'chatid': chatid}, file)
print("Configuration saved.")
