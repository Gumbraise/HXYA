import os
import requests
import json
import time
import sys
import getpass
import datetime
import shutil

def main():
    print('1) YouTube')
    print('2) Instagram')
    print('3) Clear Cache')
    print('4) Quit')
    choice(1)

def choice(cw):
    if(cw == 1):
        c1 = int(input("HXYA>"))
        if (c1 == 1):
            youtubemenu()
        elif (c1 == 2):
            instagrammenu()
        elif (c1 == 3):
            sure = input("Are you sure to clear the totality of the cache ? (y/n) ")
            if sure == "y":
                folderl = 'logs'
                for filenamel in os.listdir(folderl):
                    file_pathl = os.path.join(folderl, filenamel)
                    try:
                        if os.path.isfile(file_pathl) or os.path.islink(file_pathl):
                            os.unlink(file_pathl)
                        elif os.path.isdir(file_pathl):
                            shutil.rmtree(file_pathl)
                    except:
                        sys.exit("Error #2. Please report your error to https://github.com/Gumbraise/HXYA/issues with a screenshot of the console")
                logsrecreate = open("logs/README.md","w+")
                logsrecreate.write("# HXYA/logs\n\n")
                logsrecreate.write("Here you're gonna find all your logs after have launched the software")
                logsrecreate.close()

                foldercr = 'crash-reports'
                for filenamecr in os.listdir(foldercr):
                    file_pathcr = os.path.join(foldercr, filenamecr)
                    try:
                        if os.path.isfile(file_pathcr) or os.path.islink(file_pathcr):
                            os.unlink(file_pathcr)
                        elif os.path.isdir(file_pathcr):
                            shutil.rmtree(file_pathcr)
                    except:
                        sys.exit("Error #2. Please report your error to https://github.com/Gumbraise/HXYA/issues with a screenshot of the console")
                crashrecreate = open("crash-reports/README.md","w+")
                crashrecreate.write("# HXYA/crash-reports\n\n")
                crashrecreate.write("Here you're gonna find all your crashes after have launched the software and got errors")
                crashrecreate.close()

                foldera = 'path/instagram/AvailablePseudos'
                for filenamea in os.listdir(foldera):
                    file_patha = os.path.join(foldera, filenamea)
                    try:
                        if os.path.isfile(file_patha) or os.path.islink(file_patha):
                            os.unlink(file_patha)
                        elif os.path.isdir(file_patha):
                            shutil.rmtree(file_patha)
                    except:
                        sys.exit("Error #2. Please report your error to https://github.com/Gumbraise/HXYA/issues with a screenshot of the console")
                pseudosrecreate = open("path/instagram/AvailablePseudos/README.md","w+")
                pseudosrecreate.write("# HXYA/path/instagram/AvailablePseudos\n\n")
                pseudosrecreate.write("Here you're gonna find all your Instagram available pseudos that you trieds")
                pseudosrecreate.close()
                
                print('Cache cleared')
                main()
            else:
                main()
        elif (c1 == 4):
            sys.exit("Please consider donating. Good bye")
        else:
            print('>>>Please use 1, 2 or 3')
            choice(cw)
    elif(cw == 2):
        c2 = int(input("HXYA>YouTube>"))
        sys.path.append("path/youtube/")
        import hxya_youtube
        if (c2 == 1):
            hxya_youtube.video("like")
        elif (c2 == 2):
            hxya_youtube.video("dislike")
        elif (c2 == 3):
            hxya_youtube.channel("sub")
        elif (c2 == 4):
            hxya_youtube.video("comment")
        elif (c2 == 5):
            hxya_youtube.video("view")
        elif (c2 == 6):
            hxya_youtube.change()
        elif (c2 == 7):
            main()
        elif (c2 == 8):
            sys.exit(">>>Please consider donating. Good bye")
        else:
            print('>>>Please use 1, 2, 3, 4, 5, 6, 7 or 8')
            choice(cw)
    elif(cw == 3):
        c3 = int(input("HXYA>Instagram>"))
        sys.path.append("path/instagram/")
        import hxya_instagram
        if (c3 == 1):
            hxya_instagram.availablePseudo()
        elif (c3 == 2):
            hxya_instagram.change()
        elif (c3 == 3):
            main()
        elif (c3 == 4):
            sys.exit(">>>Please consider donating. Good bye")
        else:
            print('>>>Please use 1')
            choice(cw)
    else:
        sys.exit("Error #1. Please report your error to https://github.com/Gumbraise/HXYA/issues with a screenshot of the console")
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
            API_KEY = input("HXYA>Instagram>Change keys>Username>")
            if not API_KEY:
                youtubemenu()
            else:
                print('Paste your YouTube Channel Id here: ')
                ChannelId = input("HXYA>Instgram>Change keys>Password>")
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

print('                             _____  ')
print('|\     /||\     /||\     /| / ___ \ ')
print('| |   | || \   / || \   / || |   | |')
print('| |___| | \ \_/ /  \ \_/ / | |___| |')
print('|  ___  |  | _ |    \   /  |  ___  |')
print('| |   | | / / \ \    | |   | |   | |')
print('| |   | || /   \ |   | |   | |   | |')
print('|/     \||/     \|   \_/   |/     \|')
print('Gumbraise©2020  GitHub.com/gumbraise')
print('')
print('Welcome to HXYA ' + getpass.getuser())
print('It is ' + str(datetime.datetime.now()))
print('If you find a bug, please report it to https://github.com/Gumbraise/HXYA/issues')
print('Please review the README at https://github.com/Gumbraise/HXYA/README.md before proceeding')
print('')

main()