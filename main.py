import requests
import threading
import json
import sys


class colors:
    red="\033[01;31m"
    green="\033[01;32m"
    end="\033[00m"


wallet = sys.argv[1]
threads = sys.argv[2]

def run():
    try:
        while True:
            data = requests.get(f"http://econcoin.pythonanywhere.com/mine/{wallet}")
            binary = data.content
            json_data = json.loads(binary)
            print(f"{colors.green}========================================================={colors.end}")
            print(f"{colors.green}You Mined A New Block!{colors.end}")
            print(f"{colors.green}Block Number: {json_data[0]['index']}{colors.end}")
            print(f"{colors.green}Previous Block Hash: {json_data[0]['previous_hash']}{colors.end}")
            print(f"{colors.green}Block Proof Of Work Number: {json_data[0]['proof']}{colors.end}")
            print(f"{colors.green}Block Mining Reward: {json_data[0]['transactions'][0]['amount']}{colors.end}")
            print(f"{colors.green}Block Mining Reward Recipient: {json_data[0]['transactions'][0]['recient']}{colors.end}")
            print(f"{colors.green}Block Mining Reward Sender: {json_data[0]['transactions'][0]['sender']}{colors.end}")
    except Exception as e:
        print(e)

for _ in range(int(threads)):
    x = threading.Thread(target=run)
    x.start()
