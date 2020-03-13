from colorama import init, Fore, Back, Style
import os, requests, json, time, sys, datetime

try:
    js = "file/instagram.json"
    jsonFile = open(js)
    keys = json.load(jsonFile)
    jsonFile.close()
except (FileNotFoundError):
    sys.exit('keys.json is missing. Reinstall HXYA here : https://github.com/gumbraise/HXYA')

s = str(datetime.datetime.now())
snew = s.replace(" ", "")
stwo = s.replace(":", "-")

username = keys["username"]
password = keys["password"]


def avaPse():
    list_ask = input (" Do you want to use 'path/Instagram/pseudo.txt' ? (y/Enter) ")
    if not list_ask:
        liner = input(" Paste a Instagram Username here: ")
        url = 'https://instagram.com/'+liner+'/?__a=1'
        response = requests.get(url)
        try:
            availablepseudosfile = open("path/instagram/AvailablePseudos/"+stwo+".txt","w+")
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
        try:
            availablepseudosfile = open("path/instagram/AvailablePseudos/"+stwo+".txt","w+")
            try:
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
                f = open("path/instagram/pseudos.txt","w+")
        except (FileNotFoundError):
            sys.exit('Folder is missing. Reinstall HXYA here : https://github.com/gumbraise/HXYA')

