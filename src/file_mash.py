#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import platform

platform = platform.system()

if platform == "Darwin":
    reload(sys)
    sys.setdefaultencoding('utf8')

def delete_dub():
    lines_seen = set()  # holds lines already seen

    lines_seen.add('Ingen arbejdstider\n')
    lines_seen.add('Aalborg\n')
    lines_seen.add('Vikar\n')
    lines_seen.add('Hele dagen\n')
    lines_seen.add('Ferie\n')

    outfile = open("output.txt", "w+")
    for line in open("shifts.txt", "r"):
        if not 'Uge' in line and not 'Timer' in line:
            if line not in lines_seen:  # not a duplicate
                outfile.write(line)
                if not '-' in line:
                    lines_seen.add(line)
    outfile.close()


def delete_empty():
    that_line = 'm'

    letters = {
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    }

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

def delete_day():
    delete_list = ["mandag ", "tirsdag ", "onsdag ",
                   "torsdag ", "fredag ", "lørdag ",
                   "søndag ", ".", " -"]
    outfile = open("output3.txt", "w+")
    for line in open("output2.txt", "r"):
        for word in delete_list:
            line = line.replace(word, "")
        outfile.write(line)
    outfile.close()

def replace_month():
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
    outfile = open("output4.txt", "w+")
    i=0
    for line in open("output3.txt", "r"):
        for word in month2:
            line = line.replace(word, month2[word])

        outfile.write(line)
        i = +1
    outfile.close()


def make_file():
    id = 1
    lineNum = 0

    now = datetime.datetime.now()

    outfile = open("../vagter.csv", "w+")

    tmpString = str('Subject, Start Date, Start Time, End Date, End Time\n')
    tmpString2 = ''

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

            tmpString2 = str(line[3])
            tmpString2 += str(line[4])
            tmpString2 += str('/')
            tmpString2 += str(line[0])
            tmpString2 += str(line[1])
            tmpString2 += str('/')
            tmpString2 += str(now.year)
            tmpString2 += str(',')
            id += 1

        else:
            tmpString += str(line[0])
            tmpString += str(line[1])
            tmpString += str(line[2])
            tmpString += str(line[3])
            tmpString += str(line[4])
            tmpString += str(',')

            tmpString += tmpString2

            tmpString += str(line[6])
            tmpString += str(line[7])
            tmpString += str(line[8])
            tmpString += str(line[9])
            tmpString += str(line[10])

            tmpString += str('\n')
    tmpString = tmpString[:-1]

    outfile.write(str(tmpString))
    outfile.close()


def clean_up():
    os.remove('output.txt')
    os.remove('output2.txt')
    os.remove('output3.txt')
    os.remove('output4.txt')
    os.remove('shifts.txt')


def mashing():
    delete_dub()
    delete_empty()
    delete_day()
    replace_month()
    make_file()
    clean_up()