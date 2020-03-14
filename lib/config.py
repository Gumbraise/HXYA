from colorama import init, Fore, Back, Style
import json, sys
from lib.menu import clear, menu

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
        instagramMenu = """
 ╔════════════════Instagram════════════════╗               %s.-----...........---. %s
 ║                                         ║               %s/`  ;:%s           `/ / %s
 ║   %s1%s. Available Pseudos                  ║          %s/`       ::%s        `/     :`%s
 ║                                         ║      %s/`           ;:%s     /;        :`%s
 ║   Options:                              ║   %s/`              :;%s`/             :`%s
 ║   %s2%s. Configure keys...                  ║  %s:                %s;:              -/%s
 ║                                         ║  %s:            /:  %s::           -/ %s
 ║   Window Options:                       ║  %s:      /:        %s;:        -/     %s
 ║   %sC%s. Clear                              ║   %s/ ;/            %s::    ./        %s
 ║   %sB%s. Back                               ║  %s.------.......------%s./             %s
 ║   %sQ%s. Quit                               ║
 ║                                         ║
 ║                                         ║
 ║                                         ║
 ║                                         ║
 ╚══════════GitHub.com/Gumbraise═══════════╝
    """ % (
        Fore.BLACK, Fore.RESET,
        Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Fore.BLUE, Fore.RED, Fore.RESET,
        Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Fore.BLUE, Fore.RED, Fore.RESET,
        Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLACK, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL
    )

        configInstagram = """
 ╔════════════════Instagram════════════════╗               %s.-----...........---. %s
 ║                                         ║               %s/`  ;:%s           `/ / %s
 ║   %s1%s. Username                           ║          %s/`       ::%s        `/     :`%s
 ║   %s2%s. Password                           ║      %s/`           ;:%s     /;        :`%s
 ║                                         ║   %s/`              :;%s`/             :`%s
 ║   Window Options:                       ║  %s:                %s;:              -/%s
 ║   %sC%s. Clear                              ║  %s:            /:  %s::           -/ %s
 ║   %sB%s. Back                               ║  %s:      /:        %s;:        -/     %s
 ║   %sQ%s. Quit                               ║   %s/ ;/            %s::    ./        %s
 ║                                         ║  %s.------.......------%s./             %s
 ║                                         ║
 ║                                         ║
 ║                                         ║
 ╚══════════GitHub.com/Gumbraise═══════════╝
        """ % (
                Fore.BLACK, Fore.RESET,
                Fore.BLUE, Fore.RED, Fore.RESET,
                Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
                Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
                Fore.BLUE, Fore.RED, Fore.RESET,
                Fore.BLUE, Fore.RED, Fore.RESET,
                Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
                Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
                Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
                Fore.BLACK, Fore.RED, Fore.RESET
            )

        print (configInstagram)
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
                print(configInstagram)
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
                print(configInstagram)
                print(' Updated!')
            elif (which_key == 'c'):
                clear()
                menu()
                print(configInstagram)
            elif (which_key == 'b'):
                pass
                clear()
                menu()
                print(instagramMenu)
                break
            elif (which_key == 'q'):
                sys.exit(" Please consider donating. Good bye")
    elif e == 'youtube':
        print('youtube')
    else:
        mainMenu = """
 ╔═════════════Welcome to HXYA═════════════╗               %s.-----...........---. %s
 ║                                         ║               %s/`  ;:%s           `/ / %s
 ║   %s1%s. Instagram                          ║          %s/`       ::%s        `/     :`%s
 ║   %s2%s. YouTube                            ║      %s/`           ;:%s     /;        :`%s
 ║   %s3%s. CCG                                ║   %s/`              :;%s`/             :`%s
 ║                                         ║  %s:                %s;:              -/%s
 ║   Options:                              ║  %s:            /:  %s::           -/ %s
 ║   %s4%s. Configure keys...                  ║  %s:      /:        %s;:        -/     %s
 ║   %s5%s. Clear Cache                        ║   %s/ ;/            %s::    ./        %s
 ║                                         ║  %s.------.......------%s./             %s
 ║   Window Options:                       ║
 ║   %sC%s. Clear                              ║
 ║   %sQ%s. Quit                               ║
 ║                                         ║
 ║                                         ║
 ║                                         ║
 ║                                         ║
 ╚══════════GitHub.com/Gumbraise═══════════╝
    """ % (
        Fore.BLACK, Fore.RESET,
        Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Fore.BLUE, Fore.RED, Fore.RESET,
        Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Fore.BLACK, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, 
        Style.BRIGHT, Style.RESET_ALL
    )

        configMenu = """
 ╔════════════════Instagram════════════════╗               %s.-----...........---. %s
 ║                                         ║               %s/`  ;:%s           `/ / %s
 ║   %s1%s. Instagram                          ║          %s/`       ::%s        `/     :`%s
 ║   %s2%s. YouTube                            ║      %s/`           ;:%s     /;        :`%s
 ║                                         ║   %s/`              :;%s`/             :`%s
 ║   Window Options:                       ║  %s:                %s;:              -/%s
 ║   %sC%s. Clear                              ║  %s:            /:  %s::           -/ %s
 ║   %sB%s. Back                               ║  %s:      /:        %s;:        -/     %s
 ║   %sQ%s. Quit                               ║   %s/ ;/            %s::    ./        %s
 ║                                         ║  %s.------.......------%s./             %s
 ║                                         ║
 ║                                         ║
 ║                                         ║
 ║                                         ║
 ║                                         ║
 ╚══════════GitHub.com/Gumbraise═══════════╝
        """ % (
                Fore.BLACK, Fore.RESET,
                Fore.BLUE, Fore.RED, Fore.RESET,
                Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
                Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
                Fore.BLUE, Fore.RED, Fore.RESET,
                Fore.BLUE, Fore.RED, Fore.RESET,
                Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
                Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
                Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
                Fore.BLACK, Fore.RED, Fore.RESET
            )

        print (configMenu)
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
                print(configMenu)
            elif (which_key == 'b'):
                pass
                clear()
                menu()
                print(mainMenu)
                break
            elif (which_key == 'q'):
                sys.exit(" Please consider donating. Good bye")