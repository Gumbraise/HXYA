import sys, os, getpass, json
from InstagramAPI import InstagramAPI
from colorama import Fore, Style
from datetime import date

def insta():
	try:
		instaOpen = "file/instagram.json"
		instaFile = open(instaOpen)
		insta = json.load(instaFile)
		instaFile.close()
	except (FileNotFoundError):
		sys.exit(' instagram.json is missing. Reinstall HXYA here : https://github.com/gumbraise/HXYA')

	username = insta["username"]
	password = insta["password"]

	api = InstagramAPI(username, password)
	api.login()


def pyVer():
	version = sys.version[:1]
	if int(version) == 3:
		pass
	else:
		print("Veuillez lancer la version 3 de python...")
		input("Appuyez sur ENTER pour quitter le programme")
		sys.exit()

def clear():
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')

def menu():
    menu = """%s
                              _____            Welcome to HXYA %s 
 |\     /||\     /||\     /| / ___ \           We are the %s
 | |   | || \   / || \   / || |   | |          
 | |___| | \ \_/ /  \ \_/ / | |___| |          If you find a bug, please report it to
 |  ___  |  | _ |    \   /  |  ___  |          https://github.com/Gumbraise/HXYA/issues
 | |   | | / / \ \    | |   | |   | |          
 | |   | || /   \ |   | |   | |   | |          Please review the README at 
 |/     \||/     \|   \_/   |/     \|          https://github.com/Gumbraise/HXYA/README.md before proceeding
    %s""" % (
        Style.DIM,
        str(getpass.getuser()), 
        str(date.today()),
		Style.RESET_ALL
        )

    print (menu)