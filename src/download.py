
from selenium import webdriver

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



import sys
import time

delay = 4

sys.stdout = open('shifts.txt', 'w')

def download_data(username, myPass, path):
    sys.stdout = open('shifts.txt', 'w')

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

    browser.close()
