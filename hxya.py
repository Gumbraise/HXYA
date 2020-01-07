import os
import requests
import json
import time
import sys

def main():
    print('1) YouTube')
    print('2) Instagram')
    print('3) Quit')
    choice(1)

def choice(cw):
    if(cw == 1):
        c1 = int(input("HXYA>"))
        if (c1 == 1):
            youtubemenu()
        elif (c1 == 2):
            instagram()
        elif (c1 == 3):
            sys.exit("Please consider donating. Good bye")
        else:
            print('>>>Please use 1, 2 or 3')
            choice(cw)
    elif(cw == 2):
        c2 = int(input("HXYA>YouTube>"))
        sys.path.append("path/youtube/")
        import hxya_youtube
        if (c2 == 1):
            hxya_youtube.like()
        elif (c2 == 2):
            hxya_youtube.dislike()
        elif (c2 == 3):
            hxya_youtube.sub()
        elif (c2 == 4):
            hxya_youtube.comment()
        elif (c2 == 5):
            hxya_youtube.view()
        elif (c2 == 6):
            hxya_youtube.change()
        elif (c2 == 7):
            main()
        elif (c2 == 8):
            sys.exit(">>>Please consider donating. Good bye")
        else:
            print('>>>Please use 1, 2, 3, 4, 5, 6, 7 or 8')
            choice(cw)
    else:
        sys.exit("Error #1. Please report your error to https://github.com/Gumbraise/HXYA/issues with a screenshot of the console")
def instagram():
    print('>>>In building ;)')
    main()
def youtubemenu():
    js = "path/youtube/keys.json"
    jsonFile = open(js)
    keys = json.load(jsonFile)
    jsonFile.close()
    if (keys['perso'] == "none"):
        print("Paste your new YouTube API V3 Key here: ")
        API_KEY = input("HXYA>YouTube>Change keys>API Key>")
        if not API_KEY:
            youtubemenu()
        else:
            print('Paste your YouTube Channel Id here: ')
            ChannelId = input("HXYA>YouTube>Change keys>ChannelId>")
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
print('Welcome to HXYA')
print('If you find a bug, please report it to https://github.com/Gumbraise/HXYA/issues')
print('Please review the README at https://github.com/Gumbraise/HXYA/README.md before proceeding')
print('')

main()

"""
jsonFile = open('path/youtube/donttouch.json')
keys = json.load(jsonFile)
jsonFile.close()
"""