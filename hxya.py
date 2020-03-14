#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.menu import pyVer, clear, menu, insta
from lib.youtube import likClo, disClo, subClo, comClo, vieClo
from lib.instagram import avaPse, bomber, wdnfm, unfollow
from lib.ccg import ccg
from lib.config import config
from lib.cache import initca

import lib.print as printMenu

import os, requests, json, time, sys, datetime
from colorama import init, Fore, Back, Style

pyVer()
insta()

clear()
menu()
print (printMenu.mainMenu)

try:
    while True:
        try:
            c = input (" HXYA>").lower()

            if (c == '1'):
                clear()
                menu()
                print (printMenu.instagramMenu)
                while True:
                    c = input (" HXYA>Instagram>").lower()
                    if c == '1':
                        clear()
                        menu()
                        avaPse()
                    if c == '2':
                        clear()
                        menu()
                        bomber()
                    if c == '3':
                        clear()
                        menu()
                        wdnfm()
                    if c == '4':
                        clear()
                        menu()
                        unfollow()
                    elif c == '91':
                        clear()
                        menu()
                        config('instagram')
                    elif c == 'c':
                        clear()
                        menu()
                        print(printMenu.instagramMenu)
                    elif c == 'b':
                        clear()
                        menu()
                        print (printMenu.mainMenu)
                        break
                    elif c == 'q':
                        sys.exit(" Please consider donating. Good bye")
                    else:
                        print(' Please use a valid options')
            elif (c == '2'):
                clear()
                menu()
                print (printMenu.youtubeMenu)
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
                    if c == '91':
                        clear()
                        menu()
                        config('youtube')
                    elif c == 'c':
                        clear()
                        menu()
                        print(printMenu.ccgMenu)
                    elif c == 'b':
                        clear()
                        menu()
                        print (printMenu.mainMenu)
                        break
                    elif c == 'q':
                        sys.exit(" Please consider donating. Good bye")
                    else:
                        print(' Please use a valid option')
            elif (c == '3'):
                clear()
                menu()
                print (printMenu.ccgMenu)
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
                        print(printMenu.ccgMenu)
                    elif c == 'b':
                        clear()
                        menu()
                        print (printMenu.mainMenu)
                        break
                    elif c == 'q':
                        sys.exit(" Please consider donating. Good bye")
                    else:
                        print(' Please use a valid option')
            elif (c == '91'):
                clear()
                menu()
                config('all')
            elif (c == '92'):
                c = input (" Are you sure to clear the totality of the cache ? (y/n) ")
                if c == "y":
                    initca()
                else:
                    print (" Cancelled")
            elif (c == 'c'):
                clear()
                menu()
                print (printMenu.instagramMenu)
            elif (c == 'q'):
                sys.exit(" Please consider donating. Good bye")
            else:
                print(' Please use a valid option')
        except EOFError:
            print(' Please use a valid option')
except KeyboardInterrupt:
    sys.exit("\n Please consider donating. Good bye")