#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.menu import pyVer, clear, menu
from lib.youtube import inity
from lib.instagram import initi
from lib.ccg import initcc
from lib.config import initco
from lib.cache import initca

import os, requests, json, time, sys, datetime
from colorama import init, Fore, Back, Style

pyVer()

mainMenu = """
 ╔═════════════Welcome to HXYA═════════════╗               %s.-----...........---. %s
 ║                                         ║               %s/`  ;:%s           `/ / %s
 ║   %s1%s. Instagram                          ║          %s/`       ::%s        `/     :`%s
 ║   %s2%s. YouTube                            ║      %s/`           ;:%s     /;        :`%s
 ║   %s3%s. CCG                                ║   %s/`              :;%s`/             :`%s
 ║                                         ║  %s:                %s;:              -/%s
 ║   Options:                              ║  %s:            /:  %s::           -/ %s
 ║   %s4%s. Configure keys...                  ║  %s:      /:        %s;:        -/     %s
 ║   %s5%s. Clear Cache                        ║   %s/ ;/            %s::    ./        %s
 ║                                         ║  %s.------.......------%s./             %s
 ║   Window Options:                       ║
 ║   %s6%s. Clear                              ║
 ║   %s7%s. Quit                               ║
 ║                                         ║
 ║                                         ║
 ║                                         ║
 ║                                         ║
 ╚══════════GitHub.com/Gumbraise═══════════╝
""" % (
        Fore.BLACK, Fore.RESET,
        Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Fore.BLUE, Fore.RED, Fore.RESET,
        Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Fore.BLACK, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, 
        Style.BRIGHT, Style.RESET_ALL
    )

youtubeMenu = """
 ╔═════════════════YouTube═════════════════╗               %s.-----...........---. %s
 ║                                         ║               %s/`  ;:%s           `/ / %s
 ║   %s1%s. LikeClose                          ║          %s/`       ::%s        `/     :`%s
 ║   %s2%s. DislikeClose                       ║      %s/`           ;:%s     /;        :`%s
 ║   %s3%s. SubClose                           ║   %s/`              :;%s`/             :`%s
 ║   %s4%s. CommentClose                       ║  %s:                %s;:              -/%s
 ║   %s5%s. SubClose                           ║  %s:            /:  %s::           -/ %s
 ║                                         ║  %s:      /:        %s;:        -/     %s
 ║   Options:                              ║   %s/ ;/            %s::    ./        %s
 ║   %s6%s. Configure keys...                  ║  %s.------.......------%s./             %s
 ║                                         ║
 ║   Window Options:                       ║
 ║   %s7%s. Clear                              ║
 ║   %s8%s. Quit                               ║
 ║                                         ║
 ║                                         ║
 ║                                         ║
 ║                                         ║
 ╚══════════GitHub.com/Gumbraise═══════════╝
""" % (
        Fore.BLACK, Fore.RESET,
        Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Fore.BLUE, Fore.RED, Fore.RESET,
        Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLACK, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, 
        Style.BRIGHT, Style.RESET_ALL
    )
instagramMenu = """
 ╔════════════════Instagram════════════════╗               %s.-----...........---. %s
 ║                                         ║               %s/`  ;:%s           `/ / %s
 ║   %s1%s. Available Pseudos                  ║          %s/`       ::%s        `/     :`%s
 ║                                         ║      %s/`           ;:%s     /;        :`%s
 ║   Options:                              ║   %s/`              :;%s`/             :`%s
 ║   %s2%s. Configure keys...                  ║  %s:                %s;:              -/%s
 ║                                         ║  %s:            /:  %s::           -/ %s
 ║   Window Options:                       ║  %s:      /:        %s;:        -/     %s
 ║   %s3%s. Clear                              ║   %s/ ;/            %s::    ./        %s
 ║   %s4%s. Quit                               ║  %s.------.......------%s./             %s
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
    )

clear()
menu()
print (mainMenu)

try:
    while True:
        try:
            c = int(input (" HXYA>"))
            if (c == 1):
                clear()
                print (instagramMenu)
            elif (c == 2):
                clear()
                print (youtubeMenu)
            elif (c == 3):
                initcc()
            elif (c == 4):
                initco()
            elif (c == 5):
                c = input (" Are you sure to clear the totality of the cache ? (y/n) ")
                if c == "y":
                    initca()
                else:
                    print (" Cancelled")
            elif (c == 6):
                print (" Soon...")
            elif (c == 7):
                sys.exit(" Please consider donating. Good bye")
            else:
                print(' Please use an integer which is between 1 and 7')
        except ValueError:
            print(' Please use an integer')
        except EOFError:
            print(' Please use an integer')

except KeyboardInterrupt:
    sys.exit("\n Please consider donating. Good bye")

def instagrammenu():
    try:
        try:
            js = "path/instagram/keys.json"
            jsonFile = open(js)
            keys = json.load(jsonFile)
            jsonFile.close()
        except (FileNotFoundError):
            sys.exit('keys.json is missing. Reinstall HXYA here : https://github.com/gumbraise/HXYA')
        if (keys['perso'] == "none"):
            print("Paste your Instagram Username here: ")
            username = input("HXYA>Instagram>Change keys>Username>")
            if not username:
                instagrammenu()
            else:
                print('Paste your Instagram Password here: ')
                password = input("HXYA>Instgram>Change keys>Password>")
                if not password:
                    instagrammenu()
                else:
                    tmp_perso = keys["perso"]
                    keys["perso"] = "True"
                    tmp_username = keys["username"]
                    keys["username"] = username
                    tmp_password = keys["password"]
                    keys["password"] = password
                    jsonFile = open(js, "w")
                    jsonFile.write(json.dumps(keys))
                    jsonFile.close()
                    instagrammenu()
        else:
            import InstagramAPI
            print('1) AvailablePseudo         4) Quit')
            print('2) Change keys')
            print('3) Go back')
            choice(3)
    except (ModuleNotFoundError):
        try:
            import subprocess
            subprocess.call([r'C:\Users\kelli\Desktop\YOUTUBE_py\path\instagram\instagramapi.bat'])
        except (FileNotFoundError):
            sys.exit('instagramapi.bat is missing. Reinstall HXYA here : https://github.com/gumbraise/HXYA')

def youtubemenu():

    try:
        js = "path/youtube/keys.json"
        jsonFile = open(js)
        keys = json.load(jsonFile)
        jsonFile.close()
    except (FileNotFoundError):
        sys.exit('keys.json is missing. Reinstall HXYA here : https://github.com/gumbraise/HXYA')
    if (keys['perso'] == "none"):
        print("Paste your YouTube API V3 Key here: ")
        API_KEY = input("HXYA>YouTube>Change keys>API Key> ")
        if not API_KEY:
            youtubemenu()
        else:
            print('Paste your YouTube Channel Id here: ')
            ChannelId = input("HXYA>YouTube>Change keys>ChannelId> ")
            if not ChannelId:
                youtubemenu()
            else:
                tmp_perso = keys["perso"]
                keys["perso"] = "True"
                tmp_api_key = keys["API_KEY"]
                keys["API_KEY"] = API_KEY
                tmp_channelid = keys["ChannelId"]
                keys["ChannelId"] = ChannelId
                jsonFile = open(js, "w")
                jsonFile.write(json.dumps(keys))
                jsonFile.close()
                youtubemenu()
    else:
        API_KEY = keys["API_KEY"]
        ChannelId = keys["ChannelId"]
        print('1) LikeClose               6) Change keys')
        print('2) DislikeClose            7) Go back')
        print('3) SubClose                8) Quit')
        print('4) CommentClose')
        print('5) ViewClose')
        choice(2)
