import os
import requests
import json
import time
import sys
import datetime
import getpass

try:
    js = "path/youtube/keys.json"
    jsonFile = open(js)
    keys = json.load(jsonFile)
    jsonFile.close()
except (FileNotFoundError):
    sys.exit('keys.json is missing. Reinstall HXYA here : https://github.com/gumbraise/HXYA')

s = str(datetime.datetime.now())
snew = s.replace(" ", "")
stwo = s.replace(":", "-")

logsfile = open("logs/"+stwo+".log","w+")
logsfile.write("STARTED YOUTUBE PROGRAM AT " + str(datetime.datetime.now()) + ", " + getpass.getuser() + "\n")

API_KEY = keys["API_KEY"]
ChannelId = keys["ChannelId"]

def video(one):
    logs("client", "info", "Choose Youtube "+str(one)+"\n")
    if(keys['VideoId'] == "0"):
        VideoId = str(input("Paste the VideoId here: "))
        logs("hxya", "info", "Paste the VideoId here: \n")
        logs("client", "info", "Used: " + str(VideoId)+"\n")
        if not VideoId:
            video(one)
        else:
            keys["VideoId"] = VideoId
            jsonFile = open(js, "w")
            jsonFile.write(json.dumps(keys))
            jsonFile.close()
            logs("hxya", "info", "Changed videoId to: " + str(VideoId) + "\n")

    else:
        video_ask = str(input("Do you want change the VideoId => "+keys["VideoId"]+" ? (y/n) "))
        logs("hxya", "info", "Do you want change the VideoId => "+keys["VideoId"]+" ? (y/n)\n")
        logs("client", "info", "Used: " + str(video_ask) + "\n")
        if (video_ask == 'y'):
            VideoId = input("Paste the VideoId here: ")
            logs("hxya", "info", "Paste the VideoId here:\n")
            logs("client", "info", "Used: " + str(VideoId)+"\n")
            if not VideoId:
                video(one)
            else:
                keys["VideoId"] = VideoId
                jsonFile = open(js, "w")
                jsonFile.write(json.dumps(keys))
                jsonFile.close()
                logs("hxya", "warn", "keys.json successful opened\n")
                logs("hxya", "info", "Changed videoId to: " + str(VideoId) + "\n")

        elif (video_ask == 'n'):
            VideoId = keys['VideoId']
            logs("client", "info", "Used videoId: " + str(VideoId) + "\n")
        else:
            video(one)

    #Do not change:
    url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id='+VideoId+'&key='+API_KEY
    #-------------
    number_limit = int(input('How many '+one+' do you want to close OBS ?: '))
    logs("hxya", "info", "How many "+one+" do you want to close OBS ?:\n")
    logs("client", "info", "Used: " + str(number_limit)+"\n")
    print ('If the software doesn\'t lauch after 15 seconds restart the software and modify your YouTube API V3 Key')
    logs("hxya", "info", 'If the software doesn\'t lauch after 15 seconds restart the software and modify your YouTube API V3 Key\n')
    while True:
        response = requests.get(url)
        respJSON = response.json()
        try:
            number = int( respJSON['items'][0].get("statistics").get(one.lower()+"Count") )
            print(str(datetime.datetime.now()) + " >>> " + str(number) + " " + one.lower())
            logs("hxya", "info", str(datetime.datetime.now()) + " >>> " + str(number) + " " + one.lower() + "\n")

            if (number >= number_limit):
                os.system("taskkill /im obs64.exe")
                logs("hxya", "warn", "Taskkilled OBS\n")
                print(">>>OBS is taskkilled")
                logs("hxya", "info", ">>>OBS is taskkilled\n")
                sys.path.append("../../")
                logs("hxya", "warn", "System path updated to *root*\n")
                import hxya
                logs("hxya", "warn", "Imported hxya\n")
                hxya.youtubemenu()
                logs("hxya", "warn", "FINISHED BY BREAK\n")
                break
        except (KeyError):
            keyerror = str( respJSON['error'].get("message") )
            logs("hxya", "error", "Fatal error JSON\n")

            crash("fatal", stwo, str(datetime.datetime.now()), keyerror)

            print("An error as occured. A crash report has been created in the crash-reports folder. A copy of the file is sending to our team.")
            logs("hxya", "info", "An error as occured. A crash report has been created in the /crash-reports folder. A copy of the file is sending to our team.\n")

            break

        time.sleep(60)

def channel(one):
    logs("client", "info", "Choose Youtube " + str(one) + "\n")
    #Do not change:
    url = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id='+ChannelId+'&key='+API_KEY
    #-------------
    number_limit = int(input('How many subs do you want to close OBS ?: '))
    logs("hxya", "info", "How many subs do you want to close OBS ?: \n")
    logs("client", "info", "Used: " + str(number_limit) + "\n")

    print ('If the software doesn\'t lauch after 15 seconds restart the software and modify your YouTube API V3 Key')
    logs("hxya", "info", "If the software doesn\'t lauch after 15 seconds restart the software and modify your YouTube API V3 Key\n")
    while True:
        response = requests.get(url)
        respJSON = response.json()
        try:
            number = int( respJSON['items'][0].get("statistics").get(one.lower()+"Count") )
            print(str(datetime.datetime.now()) + " >>> " + str(number) + " " + one.lower())
            logs("hxya", "info", str(datetime.datetime.now()) + " >>> " + str(number) + " " + one.lower() + "\n")

            if (number >= number_limit):
                os.system("taskkill /im obs64.exe")
                logs("hxya", "warn", "Taskkilled OBS\n")
                print(">>>OBS is taskkilled")
                logs("hxya", "info", ">>>OBS is taskkilled\n")
                sys.path.append("../../")
                logs("hxya", "warn", "System path updated to *root*\n")
                import hxya
                logs("hxya", "warn", "Imported hxya\n")
                hxya.youtubemenu()
                logs("hxya", "warn", "FINISHED BY BREAK\n")
                break

        except (KeyError):
            keyerror = str( respJSON['error'].get("message") )
            logs("hxya", "error", "Fatal error JSON\n")

            crash("fatal", stwo, str(datetime.datetime.now()), keyerror)

            print("An error as occured. A crash report has been created in the crash-reports folder. A copy of the file is sending to our team.")
            logs("hxya", "info", "An error as occured. A crash report has been created in the /crash-reports folder. A copy of the file is sending to our team.\n")

            break


        time.sleep(60)

def change():
    print('1) API Key')
    print('2) ChannelId')
    print('3) Go back')
    which_key = int(input("HXYA>YouTube>Change keys> "))
    if (which_key == 1):
        print("Paste your new YouTube API V3 Key here: ")
        API_KEY = input("HXYA>YouTube>Change keys>API Key> ")
        if not API_KEY:
            change()
        else:
            tmp_api_key = keys["API_KEY"]
            keys["API_KEY"] = API_KEY
            jsonFile = open(js, "w")
            jsonFile.write(json.dumps(keys))
            jsonFile.close()
            print('>>>UPDATED!')
            change()
    elif (which_key == 2):
        print('Paste your YouTube Channel Id here: ')
        ChannelId = input("HXYA>YouTube>Change keys>ChannelId> ")
        if not ChannelId:
            change()
        else:
            tmp_channelid = keys["ChannelId"]
            keys["ChannelId"] = ChannelId
            jsonFile = open(js, "w")
            jsonFile.write(json.dumps(keys))
            jsonFile.close()
            print('>>>UPDATED!')
            change()
    elif (which_key == 3):
        sys.path.append("../../")
        import hxya
        hxya.youtubemenu()


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
    crash.write("   package: youtube\n")
    crash.write("   version: "+package['version']+"\n")
    crash.write("   time: "+time+"\n")
    crash.write("   reason: "+reason+"\n")

def logs(who, what, text):
    date = str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)+":"+str(datetime.datetime.now().second)
    logsfile.write("["+date+"] ["+who.upper()+"/"+what.upper()+"]: "+text)
