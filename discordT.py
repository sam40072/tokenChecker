import requests
import time
import os
import sys

def setup():
    if (not os.path.exists("settings/")):
        print('setting up...')
        print('making settigns folder')
        os.mkdir('settings/')
        print('making tokens.txt')
        open('settings/tokens.txt', 'a').close()
        print('making workingTokens.txt')
        open('settings/workingTokens.txt', 'a').close()
        time.sleep(1)
        os.system('clear')
    

def checkAccount(token: str):
    link = "https://discord.com/api/v9/users/@me"
    headerss = {'Authorization': token}
    file = open('settings/workingTokens.txt', 'a+')
    try:
        check = requests.get(link, headers=headerss).status_code
        if (check == 200):
            print(f'\033[32m[valid] - {token}')
            file.write(f'{token}\n')
        else:
            print(f'\033[31m[invalid] - {token}')
            
    except Exception as e:
        print(e)
    file.close()

def printMenu():
    print('\033[35m[1] check from tokens.txt\n[2] quit')    


setup()
while(1):
    printMenu()
    choice = input(' > ')
    if (choice == '1'):
        for token in open('settings/tokens.txt', 'r+').readlines():
            checkAccount(str(token).strip())
    if (choice == '2'):
        print('bye bye ;D')
        time.sleep(1)
        exit()





