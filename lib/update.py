import json, requests
from lib.menu import pyVer, clear, menu

def update():
    print (' Internet access verification...', end='')
    url = "https://raw.githubusercontent.com/Gumbraise/HXYA/master/package.json"
    try:
        print (' Good!')
        r = requests.get(url)
        verOnline = r.json()
        print (' HXYA files verification...', end='')
        try:
            verInstall = "package.json"
            verInstalledOpen = open(verInstall)
            verInstalled = json.load(verInstalledOpen)
            verInstalledOpen.close()
            print (' Good!')
        except (FileNotFoundError):
            print(' package.json is missing. Reinstall HXYA here : https://github.com/gumbraise/HXYA')
            input(' Type ENTER to exit')
            exit()

        try:
            print (' HXYA stable version verification...', end='')
            if (verOnline['version']['stable'] == verInstalled['version']['stable']):
                print (' Good!')
                pass
            else:
                vers = """ Your version:
     %s
 New version:
     %s""" % (
                    verInstalled['version']['stable'],
                    verOnline['version']['stable']
                )
                print (' Your version of HXYA is out of date. Please update the new stable version quickly on https://github.com/gumbraise/HXYA')
                print (vers)
                input(' Type ENTER to pass')
                pass
        except:
            print (' Your version of HXYA has been out to date too long. Please download the new version on https://github.com/gumbraise/HXYA')
            input(' Type ENTER to exit')
            exit()
    except:
        print (' HXYA need a stable Internet connection. Launch HXYA when you get your machine connected to Internet')
        input(' Type ENTER to exit')
        exit()