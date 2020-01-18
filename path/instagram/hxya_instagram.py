import os
import requests
import json
import time
import sys
import datetime
import getpass
from InstagramAPI import InstagramAPI

try:
    js = "path/instagram/keys.json"
    jsonFile = open(js)
    keys = json.load(jsonFile)
    jsonFile.close()
except (FileNotFoundError):
    sys.exit('keys.json is missing. Reinstall HXYA here : https://github.com/gumbraise/HXYA')


s = str(datetime.datetime.now())
snew = s.replace(" ", "")
stwo = s.replace(":", "-")

logsfile = open("logs/"+stwo+".log","w+")
logsfile.write("STARTED INSTAGRAM PROGRAM AT " + str(datetime.datetime.now()) + ", " + getpass.getuser() + "\n")

username = keys["username"]
password = keys["password"]

def availablePseudo():  
    logs("client", "info", "Choose Instagram AvailablePseudo\n")
    list_ask = input ("Do you want to use 'pseudo.txt' ? (y/Enter) ")
    logs("hxya", "info", "Do you want to use 'pseudo.txt' ? (y/Enter) \n")
    if not list_ask:
        logs("client", "info", "Used: Enter \n")
        liner = input("Paste a Instagram Username here: ")
        logs("hxya", "info", "Paste a Instagram Username here: \n")
        logs("client", "info", "Used: " + str(liner)+"\n")
        url = 'https://instagram.com/'+liner+'/?__a=1'
        response = requests.get(url)
        try:
            availablepseudosfile = open("path/instagram/AvailablePseudos/"+stwo+".txt","w+")
            logs("hxya", "warn", stwo+".txt successful created and opened\n")
            try:
                respJSON = response.json()
                user_id = str( respJSON['graphql'].get("user").get("id") )
                print (liner + ' >> ❌')
            except (json.decoder.JSONDecodeError):
                print (liner + ' >> ✅')
                availablepseudosfile.write(liner + "\n")
        except (FileNotFoundError):
            sys.exit('Folder is missing. Reinstall HXYA here : https://github.com/gumbraise/HXYA')
    elif (list_ask == 'y'):
        logs("client", "info", "Used: " + str(list_ask)+"\n")
        try:
            availablepseudosfile = open("path/instagram/AvailablePseudos/"+stwo+".txt","w+")
            logs("hxya", "warn", stwo+".txt successful created and opened\n")
            try:
                logs("hxya", "warn", "pseudos.txt successful opened\n")
                with open("path/instagram/pseudos.txt") as s:
                    for line in s:
                        liner = line.replace('\n', ' ').replace('\r', '').replace(' ', '')
                        url = 'https://instagram.com/'+liner+'/?__a=1'
                        response = requests.get(url)
                        try:
                            respJSON = response.json()
                            user_id = str( respJSON['graphql'].get("user").get("id") )
                            print (liner + ' >> ❌')
                        except (json.decoder.JSONDecodeError):
                            print (liner + ' >> ✅')
                            availablepseudosfile.write(liner + "\n")

            except (FileNotFoundError):
                logs("hxya", "error", "Missing pseudos.txt\n")
                logs("hxya", "error", "Creating pseudos.txt\n")
                f = open("path/instagram/pseudos.txt","w+")
                logs("hxya", "info", "pseudos.txt created\n")
                import hxya
                hxya.instagrammenu()
        except (FileNotFoundError):
            sys.exit('Folder is missing. Reinstall HXYA here : https://github.com/gumbraise/HXYA')
    else:
        availablePseudo()


def change():
    print('1) Username')
    print('2) Password')
    print('3) Go back')
    which_key = int(input("HXYA>Instagram>Change keys>"))
    if (which_key == 1):
        print("Paste your new Instagram Username here: ")
        username = input("HXYA>Instagram>Change keys>Username> ")
        if not username:
            change()
        else:
            tmp_username = keys["username"]
            keys["username"] = username
            jsonFile = open(js, "w")
            jsonFile.write(json.dumps(keys))
            jsonFile.close()
            print('>>>UPDATED!')
            change()
    elif (which_key == 2):
        print('Paste your new Instagram Password here: ')
        password = input("HXYA>Instagram>Change keys>Password> ")
        if not password:
            change()
        else:
            tmp_password = keys["password"]
            keys["password"] = password
            jsonFile = open(js, "w")
            jsonFile.write(json.dumps(keys))
            jsonFile.close()
            print('>>>UPDATED!')
            change()
    elif (which_key == 3):
        sys.path.append("../../")
        import hxya
        hxya.instagrammenu()

def crash(type, date, time, reason):
    try:
        jsonFile = open("package.json")
        package = json.load(jsonFile)
        jsonFile.close()
    except (FileNotFoundError):
        sys.exit('package.json is missing. Reinstall HXYA here : https://github.com/gumbraise/HXYA')


    crash = open("crash-reports/"+ type +"crash-"+date+"-client.yml","w+")
    crash.write("error: "+type+"\n")
    crash.write("items:\n")
    crash.write("   package: instagram\n")
    crash.write("   version: "+package['version']+"\n")
    crash.write("   time: "+time+"\n")
    crash.write("   reason: "+reason+"\n")

def logs(who, what, text):
    date = str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)+":"+str(datetime.datetime.now().second)
    logsfile.write("["+date+"] ["+who.upper()+"/"+what.upper()+"]: "+text)
