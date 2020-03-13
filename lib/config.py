from colorama import init, Fore, Back, Style

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

        which_key = input(" What do you want to change")
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
    elif e == 'youtube':
        print('youtube')
    else:
        print('rien')