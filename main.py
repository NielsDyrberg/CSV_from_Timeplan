#!/usr/bin/env python
# -*- coding: utf-8 -*-

#By Niels Dyrberg
#Brug under eget ansvar!


import sys
import os

from checkOS import get_platform
from credentials import get_timeplan_credentials, get_google_credentials
from download import download_data
from file_mash import mashing
#from upload import upload_csv


def main ():
    platform = get_platform()

    if platform == "Darwin":
        reload(sys)
        sys.setdefaultencoding('utf8')

    credential = get_timeplan_credentials(platform)
    download_data(credential[0],credential[1],credential[2])
    mashing()

    #credential = get_google_credentials()
    #upload_csv(credential[0], credential[1], credential[2])

    exit(0)

main()