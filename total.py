#!/usr/bin/env python
# -*- coding: utf-8 -*-

#By Niels Dyrberg
#Brug under eget ansvar!

from selenium import webdriver

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

import sys

import os

sys.stdout = open('shifts.txt', 'w')

#Dit løn nummer
username = ''
#Dit password
myPass = ''
#Din browser driver - Skrift kun det ud mellem ''
path = r'C:\...\chromedriver.exe'

delay = 4 # seconds

browser = webdriver.Chrome(path)

browser.get('https://haraldnyborg.timeplan.dk/')

try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'username')))
    #print('Page is ready!')
except TimeoutException:
    print('Loading took too much time!')

userField = browser.find_element_by_id('username')
userField.send_keys(username)

passField = browser.find_element_by_id('password')
passField.send_keys(myPass)

loginBtn = browser.find_element_by_id('loginButton')
loginBtn.click()

time.sleep(2)

arbejdsPlan = browser.find_element_by_partial_link_text('Mine tider')
arbejdsPlan.click()

time.sleep(2)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)


dates = browser.find_elements_by_css_selector('div.col-xs-12, div.col-sm-8')

i = 0
while i < len(dates):
    print(dates[i].text)
    i += 1

sys.stdout = open('log.txt', 'w')

lines_seen = set() # holds lines already seen

lines_seen.add('Ingen arbejdstider\n')
lines_seen.add('Aalborg\n')
lines_seen.add('Vikar\n')
lines_seen.add('Hele dagen\n')
lines_seen.add('Ferie\n')

letters = {
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
    's','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J',
    'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
}


outfile = open("output.txt", "w+")
for line in open("shifts.txt", "r"):
    if not 'Uge' in line and not 'Timer' in line:
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            if not '-' in line:
                lines_seen.add(line)
outfile.close()

that_line = 'm'
outfile = open("output2.txt", "w+")
for line in open("output.txt", "r"):
    this_line = line

    if this_line[0] in letters and that_line[0] in letters:
        print('stfu')
    if not this_line[0] in letters and that_line[0] in letters:
        outfile.write(that_line)
        outfile.write(this_line)
    that_line = this_line
outfile.close()

delete_list = ["mandag ", "tirsdag ", "onsdag ",
               "torsdag ", "fredag ", "lørdag ",
               "søndag ", ".", " -"]

month2 = {
    "januar": "01",
    "februar": "02",
    "marts": "03",
    "april": "04",
    "maj": "05",
    "juli": "06",
    "juni": "07",
    "august": "08",
    "september": "09",
    "oktober": "10",
    "november": "11",
    "december": "12"
}

outfile = open("output3.txt", "w+")
for line in open("output2.txt", "r"):
    for word in delete_list:
        line = line.replace(word, "")
    outfile.write(line)
outfile.close()

outfile = open("output4.txt", "w+")
i=0
for line in open("output3.txt", "r"):
    for word in month2:
        line = line.replace(word, month2[word])

    outfile.write(line)
    i = +1
outfile.close()


id=1
lineNum=0

import datetime
now = datetime.datetime.now()

outfile = open("final.csv", "w+")

tmpString = str('Subject, Start Date, Start Time, End Time\n')

for line in open("output4.txt", "r"):
    lineNum += 1
    if not (lineNum % 2) == 0:
        tmpString += str('Harald, ')
        tmpString += str(line[3])
        tmpString += str(line[4])
        tmpString += str('/')
        tmpString += str(line[0])
        tmpString += str(line[1])
        tmpString += str('/')
        tmpString += str(now.year)
        tmpString += str(',')
        id += 1

    else:
        tmpString += str(line[0])
        tmpString += str(line[1])
        tmpString += str(line[2])
        tmpString += str(line[3])
        tmpString += str(line[4])
        tmpString += str(',')
        tmpString += str(line[6])
        tmpString += str(line[7])
        tmpString += str(line[8])
        tmpString += str(line[9])
        tmpString += str(line[10])

        tmpString += str('\n')
tmpString = tmpString[:-1]

outfile.write(str(tmpString))
outfile.close()

os.remove('output.txt')
os.remove('output2.txt')
os.remove('output3.txt')
os.remove('output4.txt')
os.remove('shifts.txt')

browser.close()
exit()