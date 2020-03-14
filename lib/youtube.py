from colorama import init, Fore, Back, Style
from InstagramAPI import InstagramAPI
from lib.menu import clear, menu

import os, requests, json, time, sys, datetime

try:
    js = "file/youtube.json"
    jsonFile = open(js)
    keys = json.load(jsonFile)
    jsonFile.close()
except (FileNotFoundError):
    sys.exit(' youtube.json is missing. Reinstall HXYA here : https://github.com/gumbraise/HXYA')

s = str(datetime.datetime.now())
stwo = s.replace(":", "-")

API_KEY = keys["API_KEY"]

youtubeMenu = """
 ╔═════════════════YouTube═════════════════╗               %s.-----...........---. %s
 ║                                         ║               %s/`  ;:%s           `/ / %s
 ║   %s1%s. LikeClose                          ║          %s/`       ::%s        `/     :`%s
 ║   %s2%s. DislikeClose                       ║      %s/`           ;:%s     /;        :`%s
 ║   %s3%s. SubClose                           ║   %s/`              :;%s`/             :`%s
 ║   %s4%s. CommentClose                       ║  %s:                %s;:              -/%s
 ║   %s5%s. ViewClose                          ║  %s:            /:  %s::           -/ %s
 ║                                         ║  %s:      /:        %s;:        -/     %s
 ║   Options:                              ║   %s/ ;/            %s::    ./        %s
 ║   %s6%s. Configure keys...                  ║  %s.------.......------%s./             %s
 ║                                         ║
 ║   Window Options:                       ║
 ║   %sC%s. Clear                              ║
 ║   %sB%s. Back                               ║
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
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Fore.BLUE, Fore.RED, Fore.RESET,
        Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLACK, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, 
        Style.BRIGHT, Style.RESET_ALL, 
        Style.BRIGHT, Style.RESET_ALL
    )


def likClo():
    VideoId = str(input(" Paste the VideoId here: "))
    url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id='+VideoId+'&key='+API_KEY
    number_limit = int(input(' How many likes do you want to close OBS ?: '))
    while True:
        response = requests.get(url)
        respJSON = response.json()
        try:
            number = int( respJSON['items'][0].get("statistics").get("likeCount") )
            print(' '+str(datetime.datetime.now()) + " >>> " + str(number) + " like")
            if (number >= number_limit):
                os.system("taskkill /im obs64.exe")
                print(" OBS is taskkilled")
                input(' Please type ENTER')
                clear()
                menu()
                print(youtubeMenu)
                break
        except:
            print(" An error as occured. Verify your API_KEY and update it")
            input(' Please type ENTER')
            clear()
            menu()
            print(youtubeMenu)
            break

        time.sleep(60)

def disClo():
    VideoId = str(input(" Paste the VideoId here: "))
    url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id='+VideoId+'&key='+API_KEY
    number_limit = int(input(' How many dislikes do you want to close OBS ?: '))
    while True:
        response = requests.get(url)
        respJSON = response.json()
        try:
            number = int( respJSON['items'][0].get("statistics").get("dislikeCount") )
            print(' '+str(datetime.datetime.now()) + " >>> " + str(number) + " dislike")
            if (number >= number_limit):
                os.system("taskkill /im obs64.exe")
                print(" OBS is taskkilled")
                input(' Please type ENTER')
                clear()
                menu()
                print(youtubeMenu)
                break
        except:
            print(" An error as occured. Verify your API_KEY and update it")
            input(' Please type ENTER')
            clear()
            menu()
            print(youtubeMenu)
            break

        time.sleep(60)

def vieClo():
    VideoId = str(input(" Paste the VideoId here: "))
    url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id='+VideoId+'&key='+API_KEY
    number_limit = int(input(' How many likes do you want to close OBS ?: '))
    while True:
        response = requests.get(url)
        respJSON = response.json()
        try:
            number = int( respJSON['items'][0].get("statistics").get("viewCount") )
            print(' '+str(datetime.datetime.now()) + " >>> " + str(number) + " view")
            if (number >= number_limit):
                os.system("taskkill /im obs64.exe")
                print(" OBS is taskkilled")
                input(' Please type ENTER')
                clear()
                menu()
                print(youtubeMenu)
                break
        except:
            print(" An error as occured. Verify your API_KEY and update it")
            input(' Please type ENTER')
            clear()
            menu()
            print(youtubeMenu)
            break

        time.sleep(60)

def comClo():
    VideoId = str(input(" Paste the VideoId here: "))
    url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id='+VideoId+'&key='+API_KEY
    number_limit = int(input(' How many likes do you want to close OBS ?: '))
    while True:
        response = requests.get(url)
        respJSON = response.json()
        try:
            number = int( respJSON['items'][0].get("statistics").get("commentCount") )
            print(' '+str(datetime.datetime.now()) + " >>> " + str(number) + " comments")
            if (number >= number_limit):
                os.system("taskkill /im obs64.exe")
                print(" OBS is taskkilled")
                input(' Please type ENTER')
                clear()
                menu()
                print(youtubeMenu)
                break
        except:
            print(" An error as occured. Verify your API_KEY and update it")
            input(' Please type ENTER')
            clear()
            menu()
            print(youtubeMenu)
            break

        time.sleep(60)

def subClo():
    ChannelId = int(input(' Paste the ChannelID here: '))
    url = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id='+ChannelId+'&key='+API_KEY
    number_limit = int(input(' How many subs do you want to close OBS ?: '))
    while True:
        response = requests.get(url)
        respJSON = response.json()
        try:
            number = int( respJSON['items'][0].get("statistics").get("subCount") )
            print(' '+str(datetime.datetime.now()) + " >>> " + str(number) + " subscribers")
            if (number >= number_limit):
                os.system("taskkill /im obs64.exe")
                print(" OBS is taskkilled")
                input(' Please type ENTER')
                clear()
                menu()
                print(youtubeMenu)
                break
        except:
            print(" An error as occured. Verify your API_KEY and update it")
            input(' Please type ENTER')
            clear()
            menu()
            print(youtubeMenu)
            break

        time.sleep(60)