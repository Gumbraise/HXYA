import os
import requests
import json
import time
import sys

js = "path/youtube/keys.json"
jsonFile = open(js)
keys = json.load(jsonFile)
jsonFile.close()

API_KEY = keys["API_KEY"]
ChannelId = keys["ChannelId"]

def like():
    if(keys['VideoId'] == "0"):
        VideoId = str(input("Paste the VideoId here: "))
        if not VideoId:
            like()
        else:
            tmp_videoid = keys["VideoId"]
            keys["VideoId"] = VideoId
            jsonFile = open(js, "w")
            jsonFile.write(json.dumps(keys))
            jsonFile.close()
    else:
        video_ask = str(input("Do you want change the VideoId => "+keys["VideoId"]+" ? (y/n) "))
        if (video_ask == 'y'):
            VideoId = input("Paste the VideoId here: ")
            if not VideoId:
                like()
            else:
                tmp_videoid = keys["VideoId"]
                keys["VideoId"] = VideoId
                jsonFile = open(js, "w")
                jsonFile.write(json.dumps(keys))
                jsonFile.close()
        elif (video_ask == 'n'):
            VideoId = keys['VideoId']
        else:
            like()

    #Do not change:
    url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id='+VideoId+'&key='+API_KEY
    #-------------
    like_number_limit = int(input('How many likes do you want to close OBS ?: '))
    print ('If the software doesn\'t lauch after 15 seconds restart the software and modify your YouTube API V3 Key')
    while True:
        try:
            response = requests.get(url)
            respJSON = response.json()
            numberOfLikes = int( respJSON['items'][0].get("statistics").get("likeCount") )
        except:
            print("Ohoh...")

        if (numberOfLikes >= like_number_limit):
            os.system("taskkill /im obs64.exe")
            print(">>>OBS is taskkilled")
            sys.path.append("../../")
            import hxya
            hxya.youtubemenu()
            break
            
        time.sleep(15)

def dislike():
    if(keys['VideoId'] == "0"):
        VideoId = str(input("Paste the VideoId here: "))
        if not VideoId:
            dislike()
        else:
            tmp_videoid = keys["VideoId"]
            keys["VideoId"] = VideoId
            jsonFile = open(js, "w")
            jsonFile.write(json.dumps(keys))
            jsonFile.close()
    else:
        video_ask = str(input("Do you want change the VideoId => "+keys["VideoId"]+" ? (y/n) "))
        if (video_ask == 'y'):
            VideoId = input("Paste the VideoId here: ")
            if not VideoId:
                dislike()
            else:
                tmp_videoid = keys["VideoId"]
                keys["VideoId"] = VideoId
                jsonFile = open(js, "w")
                jsonFile.write(json.dumps(keys))
                jsonFile.close()
        elif (video_ask == 'n'):
            VideoId = keys['VideoId']
        else:
            sys.exit('Error')

    #Do not change:
    url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id='+VideoId+'&key='+API_KEY
    #-------------
    dislike_number_limit = int(input('How many dislikes do you want to close OBS ?: '))
    print ('If the software doesn\'t lauch after 15 seconds restart the software and modify your YouTube API V3 Key')
    while True:
        try:
            response = requests.get(url)
            respJSON = response.json()
            numberOfdislike = int( respJSON['items'][0].get("statistics").get("dislikeCount") )
        except:
            print("Ohoh...")

        if (numberOfdislike >= dislike_number_limit):
            os.system("taskkill /im obs64.exe")
            print(">>>OBS is taskkilled")
            sys.path.append("../../")
            import hxya
            hxya.youtubemenu()
            break

        time.sleep(15)

def sub():
    #Do not change:
    url = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id='+ChannelId+'&key='+API_KEY

    #-------------
    sub_number_limit = int(input('How many subs do you want to close OBS ?: '))
    print ('If the software doesn\'t lauch after 15 seconds restart the software and modify your YouTube API V3 Key')
    while True:
        try:
            response = requests.get(url)
            respJSON = response.json()
            numberOfSubs = int( respJSON['items'][0].get("statistics").get("subscriberCount") )
        except:
            print("Ohoh...")

        if (numberOfSubs >= sub_number_limit):
            os.system("taskkill /im obs64.exe")
            print(">>>OBS is taskkilled")
            sys.path.append("../../")
            import hxya
            hxya.youtubemenu()
            break
        
        time.sleep(15)

def comment():
    if(keys['VideoId'] == "0"):
        VideoId = str(input("Paste the VideoId here: "))
        if not VideoId:
            comment()
        else:
            tmp_videoid = keys["VideoId"]
            keys["VideoId"] = VideoId
            jsonFile = open(js, "w")
            jsonFile.write(json.dumps(keys))
            jsonFile.close()
    else:
        video_ask = str(input("Do you want change the VideoId => "+keys["VideoId"]+" ? (y/n) "))
        if (video_ask == 'y'):
            VideoId = input("Paste the VideoId here: ")
            if not VideoId:
                comment()
            else:
                tmp_videoid = keys["VideoId"]
                keys["VideoId"] = VideoId
                jsonFile = open(js, "w")
                jsonFile.write(json.dumps(keys))
                jsonFile.close()
        elif (video_ask == 'n'):
            VideoId = keys['VideoId']
        else:
            sys.exit('Error')

    #Do not change:
    url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id='+VideoId+'&key='+API_KEY
    #-------------
    comment_number_limit = int(input('How many comments do you want to close OBS ?: '))
    print ('If the software doesn\'t lauch after 15 seconds restart the software and modify your YouTube API V3 Key')
    while True:
        try:
            response = requests.get(url)
            respJSON = response.json()
            numberOfComments = int( respJSON['items'][0].get("statistics").get("commentCount") )
        except:
            print("Ohoh...")

        if (numberOfComments >= comment_number_limit):
            os.system("taskkill /im obs64.exe")
            print(">>>OBS is taskkilled")
            sys.path.append("../../")
            import hxya
            hxya.youtubemenu()
            break

        time.sleep(15)

def view():
    if(keys['VideoId'] == "0"):
        VideoId = str(input("Paste the VideoId here: "))
        if not VideoId:
            view()
        else:
            tmp_videoid = keys["VideoId"]
            keys["VideoId"] = VideoId
            jsonFile = open(js, "w")
            jsonFile.write(json.dumps(keys))
            jsonFile.close()
    else:
        video_ask = str(input("Do you want change the VideoId => "+keys["VideoId"]+" ? (y/n) "))
        if (video_ask == 'y'):
            VideoId = input("Paste the VideoId here: ")
            if not VideoId:
                view()
            else:
                tmp_videoid = keys["VideoId"]
                keys["VideoId"] = VideoId
                jsonFile = open(js, "w")
                jsonFile.write(json.dumps(keys))
                jsonFile.close()
        elif (video_ask == 'n'):
            VideoId = keys['VideoId']
        else:
            sys.exit('Error')

    #Do not change:
    url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id='+VideoId+'&key='+API_KEY
    #-------------
    view_number_limit = int(input('How many views do you want to close OBS ?: '))
    print ('If the software doesn\'t lauch after 15 seconds restart the software and modify your YouTube API V3 Key')
    while True:
        try:
            response = requests.get(url)
            respJSON = response.json()
            numberOfviews = int( respJSON['items'][0].get("statistics").get("viewCount") )
        except:
            print("Ohoh...")

        if (numberOfviews >= view_number_limit):
            os.system("taskkill /im obs64.exe")
            print(">>>OBS is taskkilled")
            sys.path.append("../../")
            import hxya
            hxya.youtubemenu()
            break

        time.sleep(15)

def change():
    print('1) API Key')
    print('2) ChannelId')
    print('3) Go back')
    which_key = int(input("HXYA>YouTube>Change keys>"))
    if (which_key == 1):
        print("Paste your new YouTube API V3 Key here: ")
        API_KEY = input("HXYA>YouTube>Change keys>API Key>")
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
        ChannelId = input("HXYA>YouTube>Change keys>ChannelId>")
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