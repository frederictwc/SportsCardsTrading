# python package
import csv
import time
import random
import sys
import os
import numpy as np

import bs4 as bs

# selenium package
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import StaleElementReferenceException


# identifiants
email_address = "frederictwc@live.com"
password = "SBaVAmdB!L7iRvh"

# fonction pause
def pause():
    time_break = random.randint(3,5)
    # print "Pause de " + str(time_break) + " seconde(s)."
    return time.sleep(time_break)

# options
options = webdriver.ChromeOptions()
options.add_argument("--kiosk")

capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(desired_capabilities=capa, chrome_options=options)
wait = WebDriverWait(driver, 30)
pause()
print ("Driver 1 open")

# url de depart
url = "https://app.cardladder.com/card/a81mteoQzRV9WTNHdxg9/sales"

# aller sur linkedin
driver.get(url) #1 : page principale
try:
    wait.until(EC.presence_of_element_located(
                    (By.ID, "email"))
                )
except (TimeoutException):
    sys.exit("Error message - loading page")
pause()
print ("Connected to cardladder")

# s'identifier
driver.find_element_by_id("email").send_keys(email_address)
pause()
driver.find_element_by_id("password").send_keys(password)
pause()
#driver.find_element_by_id("login-submit").click()
button = driver.find_element_by_xpath('//button[@class="btn block"]').click()
pause()
#wait.until(EC.element_to_be_clickable(
#    (By.ID, "nav-typeahead-wormhole"))
#)
pause()
print ("logged in")
driver.get(url)

time.sleep(5)
#print( driver.find_elements_by_xpath('//*[@div="data-v-d79dcbc6"]'))
#working
#get_div = driver.find_element_by_class_name('light').text
#get_div = driver.find_element_by_class_name('table-container').text
get_div = driver.find_element_by_class_name('table-container')

html = get_div.get_attribute('innerHTML')
soup = bs.BeautifulSoup(html)
rows = soup.find_all('tr')
data = []
for row in rows:
	data.append([row.find_all("td")[0].text,row.find_all("td")[2].text])
data = np.array([data])
data = data.reshape((-1,2)).astype(str)
name_of_card = "ronaldinho_bla_bla"
np.savetxt(f"{name_of_card}.txt",data,fmt="%s")



















