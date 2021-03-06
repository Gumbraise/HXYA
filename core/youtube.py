from lib.menu import clear, menu

import os, requests, json, time, sys, datetime
import lib.print as printMenu

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


def likClo():
    VideoId = str(input(" Paste the VideoId here: "))
    url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id='+VideoId+'&key='+API_KEY
    while True:
        try:
            number_limit = int(input(' How many likes do you want to close OBS ?: '))
            break;
        except:
            print(" Please type a real number")
    while True:
        response = requests.get(url)
        respJSON = response.json()
        try:
            number = int( respJSON['items'][0].get("statistics").get("likeCount") )
            print(' '+str(datetime.datetime.now()) + " >>> " + str(number) + " likes")
            if (number >= number_limit):
                os.system("taskkill /im obs64.exe")
                print(" OBS is taskkilled")
                input(' Please type ENTER')
                clear()
                menu()
                print(printMenu.youtubeMenu)
                break
        except:
            try:
                number = str( respJSON['error'].get("error").get("code") )
                clear()
                menu()
                print(" An error as occured. Verify your API_KEY and update it")
                input(' Please type ENTER')
                clear()
                menu()
                print(printMenu.youtubeMenu)
                break
            except:
                clear()
                menu()
                print(" An error as occured. The owner of this video desactivated likes")
                input(' Please type ENTER')
                clear()
                menu()
                print(printMenu.youtubeMenu)
                break

        time.sleep(60)

def disClo():
    VideoId = str(input(" Paste the VideoId here: "))
    url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id='+VideoId+'&key='+API_KEY
    while True:
        try:
            number_limit = int(input(' How many dislikes do you want to close OBS ?: '))
            break;
        except:
            print(" Please type a real number")
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
                print(printMenu.youtubeMenu)
                break
        except:
            try:
                number = str( respJSON['error'].get("error").get("code") )
                clear()
                menu()
                print(" An error as occured. Verify your API_KEY and update it")
                input(' Please type ENTER')
                clear()
                menu()
                print(printMenu.youtubeMenu)
                break
            except:
                clear()
                menu()
                print(" An error as occured. The owner of this video desactivated dislikes")
                input(' Please type ENTER')
                clear()
                menu()
                print(printMenu.youtubeMenu)
                break

        time.sleep(60)

def vieClo():
    VideoId = str(input(" Paste the VideoId here: "))
    url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id='+VideoId+'&key='+API_KEY
    while True:
        try:
            number_limit = int(input(' How many views do you want to close OBS ?: '))
            break;
        except:
            print(" Please type a real number")
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
                print(printMenu.youtubeMenu)
                break
        except:
            try:
                number = str( respJSON['error'].get("error").get("code") )
                clear()
                menu()
                print(" An error as occured. Verify your API_KEY and update it")
                input(' Please type ENTER')
                clear()
                menu()
                print(printMenu.youtubeMenu)
                break
            except:
                clear()
                menu()
                print(" An error as occured. The owner of this video desactivated views")
                input(' Please type ENTER')
                clear()
                menu()
                print(printMenu.youtubeMenu)
                break

        time.sleep(60)

def comClo():
    VideoId = str(input(" Paste the VideoId here: "))
    url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id='+VideoId+'&key='+API_KEY
    while True:
        try:
            number_limit = int(input(' How many comments do you want to close OBS ?: '))
            break;
        except:
            print(" Please type a real number")
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
                print(printMenu.youtubeMenu)
                break
        except:
            try:
                number = str( respJSON['error'].get("error").get("code") )
                clear()
                menu()
                print(" An error as occured. Verify your API_KEY and update it")
                input(' Please type ENTER')
                clear()
                menu()
                print(printMenu.youtubeMenu)
                break
            except:
                clear()
                menu()
                print(" An error as occured. The owner of this video desactivated comments")
                input(' Please type ENTER')
                clear()
                menu()
                print(printMenu.youtubeMenu)
                break

        time.sleep(60)

def subClo():
    ChannelId = str(input(' Paste the ChannelID here: '))
    url = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id='+ChannelId+'&key='+API_KEY
    while True:
        try:
            number_limit = int(input(' How many subscribers do you want to close OBS ?: '))
            break;
        except:
            print(" Please type a real number")
    while True:
        response = requests.get(url)
        respJSON = response.json()
        try:
            number = int( respJSON['items'][0].get("statistics").get("subscriberCount") )
            print(' '+str(datetime.datetime.now()) + " >>> " + str(number) + " subscribers")
            if (number >= number_limit):
                os.system("taskkill /im obs64.exe")
                print(" OBS is taskkilled")
                input(' Please type ENTER')
                clear()
                menu()
                print(printMenu.youtubeMenu)
                break
        except:
            try:
                number = str( respJSON['error'].get("error").get("code") )
                clear()
                menu()
                print(" An error as occured. Verify your API_KEY and update it")
                input(' Please type ENTER')
                clear()
                menu()
                print(printMenu.youtubeMenu)
                break
            except:
                clear()
                menu()
                print(" An error as occured. The owner of this channel desactivated subscribers")
                input(' Please type ENTER')
                clear()
                menu()
                print(printMenu.youtubeMenu)
                break

 
        time.sleep(60)