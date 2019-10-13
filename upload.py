
from selenium import webdriver

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import sys
import time

delay = 4

def upload_csv(user, myPass, path):
    print("ee")

    browser = webdriver.Chrome(path)

    browser.get('https://calendar.google.com/')

    time.sleep(1)

    userField = browser.find_element_by_id('identifierId')
    userField.send_keys(username)
    userField.send_keys(Keys.RETURN)

    time.sleep(1)

    passField = browser.find_element_by_name("password")
    passField.send_keys(myPass)
    passField.send_keys(Keys.RETURN)

    browser.get('https://calendar.google.com/calendar/r/settings/export')

    fileField = browser.find_element_by_name("filename")
    #fileField.send_keys(myPass)
    #fileField.send_keys(Keys.RETURN)