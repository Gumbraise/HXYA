from lib.InstagramAPI.InstagramAPI import InstagramAPI
from lib.menu import clear, menu

import lib.print as printMenu

import os, requests, json, time, sys, datetime

try:
    instaOpen = "file/instagram.json"
    instaFile = open(instaOpen)
    insta = json.load(instaFile)
    instaFile.close()
except (FileNotFoundError):
    sys.exit(' instagram.json is missing. Reinstall HXYA here : https://github.com/gumbraise/HXYA')

s = str(datetime.datetime.now())
stwo = s.replace(":", "-")

username = insta["username"]
password = insta["password"]

api = InstagramAPI(username, password)
api.login()

if username == "0":
    username = input(' Type your Instagram Username here: ')
    insta["username"] = username
    instaFile = open(instaOpen, "w")
    instaFile.write(json.dumps(insta))
    instaFile.close()
if password == "0":
    password = input(' Type your Instagram Password here: ')
    insta["password"] = password
    instaFile = open(instaOpen, "w")
    instaFile.write(json.dumps(insta))
    instaFile.close()

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
            print(printMenu.instagramMenu)
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
                    print(printMenu.instagramMenu)
            except (FileNotFoundError):
                f = open("path/instagram/pseudos.txt","w+")
                print(' Error, retest now please')
        except (FileNotFoundError):
            sys.exit(' Folder is missing. Reinstall HXYA here : https://github.com/gumbraise/HXYA')

def bomber():
    nostop = 0

    while True:
        try:
            user = input(" Enter the victim's IG Username then press ENTER: ")
            url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+user+"&rank_token=0.3953592318270893&count=1"
            response = requests.get(url)
            respJSON = response.json()
            user_id = str( respJSON['users'][0].get("user").get("pk") )
            break
        except:
            print(' Please type real Instagram username')


    message = input(" Put the message you want the software send and press ENTER: ")

    times = int(input(" How many messages do you want to send? "))

    print(" You are gonna STRESS", times,"times", user_id, "with the message: ", message, ".")
    input(" Are you sure?")

    try:
        while times > nostop:
            nostop = nostop + 1
            try:
                api.sendMessage(user_id,message)
            except:
                clear()
                menu()
                print (" An error occurred. Be sure that your Instagram creditentials are true. Else, modify them into the Config Menu")
                clear()
                menu()
                print (printMenu.instagramMenu)

            print(" "+str(nostop), ">> Sent to", user, ": ", message)
        input(" Please type ENTER")
        clear()
        menu()
        print(printMenu.instagramMenu)
    except:
        clear()
        menu()
        print(" An error occurred. You probably didn't install InstagramAPI correctly")
        input(" Please type ENTER")
        clear()
        menu()
        print(printMenu.instagramMenu)

def unfollow():
    
    try:
        following = insta.api.getSelfUsersFollowing()
    except:
        clear()
        menu()
        print (" An error occurred. Be sure that your Instagram creditentials are true. Else, modify them into the Config Menu")
        input(" Please type ENTER")
        clear()
        menu()
        print (printMenu.instagramMenu)

    try:
        for item in following["users"]:
            user = item["pk"]
            username = item["username"]

            insta.api.unfollow(user)
            print(" "+username + " is now unfollowed")
    except:
        clear()
        menu()
        print(" An error occurred. You probably didn't install InstagramAPI correctly")
        input(" Please type ENTER")
        clear()
        menu()
        print (printMenu.instagramMenu)

def wdnfm():
    following_list = []
    followers_list = []

    try:
        following = insta.api.getSelfUsersFollowing()
        followers = insta.api.getSelfUserFollowers()
    except:
        clear()
        menu()
        print (" An error occurred. Be sure that your Instagram credentials are true. Else, modify them into the Config Menu")
        input(" Please type ENTER")
        clear()
        menu()
        print (printMenu.instagramMenu)

    try:
        for item in following["users"]:
            following_list.append(item["username"])
        for item2 in followers["users"]:
            followers_list.append(item2["username"])
        
        print ((set(following_list) - set(followers_list)))
        input (" Please type ENTER")
        clear()
        menu()
        print(printMenu.instagramMenu)
    except:
        clear()
        menu()
        print(" An error occurred. You probably didn't install InstagramAPI correctly")
        input(" Please type ENTER")
        clear()
        menu()
        print (printMenu.instagramMenu)
