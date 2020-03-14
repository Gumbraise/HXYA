from colorama import init, Fore, Back, Style
import json, sys
from lib.menu import clear, menu
import lib.print as printMenu

try:
    instaOpen = "file/instagram.json"
    instaFile = open(instaOpen)
    insta = json.load(instaFile)
    instaFile.close()
except (FileNotFoundError):
    sys.exit('instagram.json is missing. Reinstall HXYA here : https://github.com/gumbraise/HXYA')
try:
    youtubeOpen = "file/youtube.json"
    youtubeFile = open(youtubeOpen)
    youtube = json.load(youtubeFile)
    youtubeFile.close()
except (FileNotFoundError):
    sys.exit('youtube.json is missing. Reinstall HXYA here : https://github.com/gumbraise/HXYA')


def config(e):
    if e == 'instagram':
        print (printMenu.configInstagram)
        while True:
            which_key = input(" HXYA>Config>").lower()
            if (which_key == '1'):
                print(" Paste your new Instagram Username here: ")
                username = input(" HXYA>Config>Instagram>")
                insta["username"] = username
                instaFile = open(instaOpen, "w")
                instaFile.write(json.dumps(insta))
                instaFile.close()
                clear()
                menu()
                print(printMenu.configInstagram)
                print(' Updated!')
            elif (which_key == '2'):
                print(' Paste your new Instagram Password here: ')
                password = input(" HXYA>Config>Instagram>")
                insta["password"] = password
                instaFile = open(instaOpen, "w")
                instaFile.write(json.dumps(insta))
                instaFile.close()
                clear()
                menu()
                print(printMenu.configInstagram)
                print(' Updated!')
            elif (which_key == 'c'):
                clear()
                menu()
                print(printMenu.configInstagram)
            elif (which_key == 'b'):
                pass
                clear()
                menu()
                print(printMenu.instagramMenu)
                break
            elif (which_key == 'q'):
                sys.exit(" Please consider donating. Good bye")
    elif e == 'youtube':
        print (printMenu.configYoutube)
        while True:
            which_key = input(" HXYA>Config>").lower()
            if (which_key == '1'):
                print(" Paste your new API_KEY here: ")
                API_KEY = input(" HXYA>Config>YouTube>")
                youtube["API_KEY"] = API_KEY
                youtubeFile = open(youtubeOpen, "w")
                youtubeFile.write(json.dumps(youtube))
                youtubeFile.close()
                clear()
                menu()
                print(printMenu.configYoutube)
                print(' Updated!')
            elif (which_key == 'c'):
                clear()
                menu()
                print(printMenu.configYoutube)
            elif (which_key == 'b'):
                pass
                clear()
                menu()
                print(printMenu.youtubeMenu)
                break
            elif (which_key == 'q'):
                sys.exit(" Please consider donating. Good bye")
    else:
        print (printMenu.configMenu)
        while True:
            which_key = input(" HXYA>Config>").lower()
            if (which_key == '1'):
                clear()
                menu()
                config('instagram')
            elif (which_key == '2'):
                clear()
                menu()
                config('youtube')
            elif (which_key == 'c'):
                clear()
                menu()
                print(printMenu.configMenu)
            elif (which_key == 'b'):
                pass
                clear()
                menu()
                print(printMenu.mainMenu)
                break
            elif (which_key == 'q'):
                sys.exit(" Please consider donating. Good bye")