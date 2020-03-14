#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.menu import pyVer, clear, menu
from lib.youtube import likClo, disClo, subClo, comClo, vieClo
from lib.instagram import avaPse
from lib.ccg import ccg
from lib.config import config
from lib.cache import initca

import os, requests, json, time, sys, datetime
from colorama import init, Fore, Back, Style

pyVer()

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

youtubeMenu = """
 ╔═════════════════YouTube═════════════════╗               %s.-----...........---. %s
 ║                                         ║               %s/`  ;:%s           `/ / %s
 ║   %s1%s. LikeClose                          ║          %s/`       ::%s        `/     :`%s
 ║   %s2%s. DislikeClose                       ║      %s/`           ;:%s     /;        :`%s
 ║   %s3%s. SubClose                           ║   %s/`              :;%s`/             :`%s
 ║   %s4%s. CommentClose                       ║  %s:                %s;:              -/%s
 ║   %s5%s. ViewClose                          ║  %s:            /:  %s::           -/ %s
 ║                                         ║  %s:      /:        %s;:        -/     %s
 ║   Options:                              ║   %s/ ;/            %s::    ./        %s
 ║   %s6%s. Configure keys...                  ║  %s.------.......------%s./             %s
 ║                                         ║
 ║   Window Options:                       ║
 ║   %sC%s. Clear                              ║
 ║   %sB%s. Back                               ║
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
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLUE, Fore.RED, Fore.RESET,
        Fore.BLUE, Fore.RED, Fore.RESET,
        Fore.BLUE, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, Fore.BLACK, Fore.RED, Fore.RESET,
        Style.BRIGHT, Style.RESET_ALL, 
        Style.BRIGHT, Style.RESET_ALL, 
        Style.BRIGHT, Style.RESET_ALL
    )

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

ccgMenu = """
 ╔═══════════════════CCG═══════════════════╗               %s.-----...........---. %s
 ║                                         ║               %s/`  ;:%s           `/ / %s
 ║   %s1%s. Visa                               ║          %s/`       ::%s        `/     :`%s
 ║   %s2%s. MasterCard                         ║      %s/`           ;:%s     /;        :`%s
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

clear()
menu()
print (mainMenu)

try:
    while True:
        try:
            c = input (" HXYA>").lower()

            if (c == '1'):
                clear()
                menu()
                print (instagramMenu)
                while True:
                    c = input (" HXYA>Instagram>").lower()
                    if c == '1':
                        clear()
                        menu()
                        avaPse()
                    elif c == '2':
                        clear()
                        menu()
                        config('instagram')
                    elif c == 'c':
                        clear()
                        menu()
                        print(instagramMenu)
                    elif c == 'b':
                        clear()
                        menu()
                        print (mainMenu)
                        break
                    elif c == 'q':
                        sys.exit(" Please consider donating. Good bye")
                    else:
                        print(' Please use a valid options')
            elif (c == '2'):
                clear()
                menu()
                print (youtubeMenu)
                while True:
                    c = input (" HXYA>YouTube>").lower()
                    if c == '1':
                        clear()
                        menu()
                        likClo()
                    if c == '2':
                        clear()
                        menu()
                        disClo()
                    if c == '3':
                        clear()
                        menu()
                        subClo()
                    if c == '4':
                        clear()
                        menu()
                        comClo()
                    if c == '5':
                        clear()
                        menu()
                        vieClo()
                    if c == '6':
                        clear()
                        menu()
                        config('youtube')
                    elif c == 'c':
                        clear()
                        menu()
                        print(ccgMenu)
                    elif c == 'b':
                        clear()
                        menu()
                        print (mainMenu)
                        break
                    elif c == 'q':
                        sys.exit(" Please consider donating. Good bye")
                    else:
                        print(' Please use a valid option')
            elif (c == '3'):
                clear()
                menu()
                print (ccgMenu)
                while True:
                    c = input (" HXYA>CCG>").lower()
                    if c == '1':
                        clear()
                        menu()
                        ccg('visa')
                    if c == '2':
                        clear()
                        menu()
                        ccg('mastercard')
                    elif c == 'c':
                        clear()
                        menu()
                        print(ccgMenu)
                    elif c == 'b':
                        clear()
                        menu()
                        print (mainMenu)
                        break
                    elif c == 'q':
                        sys.exit(" Please consider donating. Good bye")
                    else:
                        print(' Please use a valid option')
            elif (c == '4'):
                clear()
                menu()
                config('all')
            elif (c == '5'):
                c = input (" Are you sure to clear the totality of the cache ? (y/n) ")
                if c == "y":
                    initca()
                else:
                    print (" Cancelled")
            elif (c == 'c'):
                clear()
                menu()
                print (instagramMenu)
            elif (c == 'q'):
                sys.exit(" Please consider donating. Good bye")
            else:
                print(' Please use a valid option')
        except EOFError:
            print(' Please use a valid option')
except KeyboardInterrupt:
    sys.exit("\n Please consider donating. Good bye")