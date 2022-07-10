import requests
import os
import time

token = input("Account Token  >  ")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
    'Content-Type': 'application/json',
    'Authorization': token,
}


get_friends = requests.get("https://discord.com/api/v8/users/@me/relationships", headers=headers).json()

for friends in get_friends:
    try:
        with open("Friend_Usernames.txt", 'a') as f:
            f.write(f"{friends['user']['username']}#{friends['user']['discriminator']}\n")
            print(f"[+] Scraped Friend: {friends['user']['username']}#{friends['user']['discriminator']}")
            time.sleep(.20)

        with open("Friend_IDs.txt", 'a') as f:
            f.write(f"{friends['user']['id']}\n")
            print(f"[+] Scraped Friend: {friends['user']['id']}")
            time.sleep(.20)

    except Exception as e:
        print(f'[*] Error: {e}')
        time.sleep(.20)
