from colorama import init, Fore, Back, Style
from InstagramAPI import InstagramAPI
from lib.menu import clear, menu

import os, requests, json, time, sys, datetime

try:
    js = "file/instagram.json"
    jsonFile = open(js)
    keys = json.load(jsonFile)
    jsonFile.close()
except (FileNotFoundError):
    sys.exit(' instagram.json is missing. Reinstall HXYA here : https://github.com/gumbraise/HXYA')

s = str(datetime.datetime.now())
stwo = s.replace(":", "-")

username = keys["username"]
password = keys["password"]

instagramMenu = """
 ╔════════════════Instagram════════════════╗               %s.-----...........---. %s
 ║                                         ║               %s/`  ;:%s           `/ / %s
 ║   %s1%s. Available Pseudos                  ║          %s/`       ::%s        `/     :`%s
 ║                                         ║      %s/`           ;:%s     /;        :`%s
 ║   Options:                              ║   %s/`              :;%s`/             :`%s
 ║   %s2%s. Configure keys...                  ║  %s:                %s;:              -/%s
 ║                                         ║  %s:            /:  %s::           -/ %s
 ║   Window Options:                       ║  %s:      /:        %s;:        -/     %s
 ║   %sC%s. Clear                              ║   %s/ ;/            %s::    ./        %s
 ║   %sB%s. Back                               ║  %s.------.......------%s./             %s
 ║   %sQ%s. Quit                               ║
 ║                                         ║
 ║                                         ║
 ║                                         ║
 ║                                         ║
 ╚══════════GitHub.com/Gumbraise═══════════╝
""" % (
        Fore.BLACK, Fore.RESET,
        Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Fore.BLUE, Fore.RED, Fore.RESET,
        Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Fore.BLUE, Fore.RED, Fore.RESET,
        Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLACK, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL
    )

def avaPse():
    list_ask = input (" Do you want to use 'path/Instagram/pseudo.txt' ? (y/Enter) ")
    if not list_ask:
        liner = input(" Paste a Instagram Username here: ")
        url = 'https://instagram.com/'+liner+'/?__a=1'
        response = requests.get(url)
        try:
            availablepseudosfile = open("path/instagram/AvailablePseudos/"+stwo+".txt","w+")
            clear()
            menu()
            try:
                respJSON = response.json()
                user_id = str( respJSON['graphql'].get("user").get("id") )
                print (' '+liner + ' >> X')
            except:
                print (' '+liner + ' >> V')
                availablepseudosfile.write(liner + "\n")
            input(' Please type ENTER')
            clear()
            menu()
            print(instagramMenu)
        except (FileNotFoundError):
            sys.exit(' Folder is missing. Reinstall HXYA here : https://github.com/gumbraise/HXYA')
    elif (list_ask == 'y'):
        try:
            availablepseudosfile = open("path/instagram/AvailablePseudos/"+stwo+".txt","w+")
            clear()
            menu()
            try:
                with open("path/instagram/pseudos.txt") as s:
                    for line in s:
                        liner = line.replace('\n', ' ').replace('\r', '').replace(' ', '')
                        url = 'https://instagram.com/'+liner+'/?__a=1'
                        response = requests.get(url)
                        try:
                            respJSON = response.json()
                            user_id = str( respJSON['graphql'].get("user").get("id") )
                            print (' '+liner + ' >> X')
                        except:
                            print (' '+liner + ' >> V')
                            availablepseudosfile.write(liner + "\n")
                    input(' Please type ENTER')
                    clear()
                    menu()
                    print(instagramMenu)
            except (FileNotFoundError):
                f = open("path/instagram/pseudos.txt","w+")
                print(' Error, retest now please')
        except (FileNotFoundError):
            sys.exit(' Folder is missing. Reinstall HXYA here : https://github.com/gumbraise/HXYA')

