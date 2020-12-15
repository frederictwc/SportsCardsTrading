# python package
import csv
import time
import random
import sys
import os

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
email_address = "your@mail.com"
password = "your_password"
search_item = "Chief Happiness Officer"

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
print ("Driver 1 ouvert")

# url de depart
linkedin_url = "https://www.linkedin.com/"

# aller sur linkedin
driver.get(linkedin_url) #1 : page principale
try:
    wait.until(EC.presence_of_element_located(
                    (By.ID, "login-submit"))
                )
except (TimeoutException):
    sys.exit("Error message - loading page")
pause()
print ("Connecte a Linkedin - 1")

# s'identifier
driver.find_element_by_id("login-email").send_keys(email_address)
pause()
driver.find_element_by_id("login-password").send_keys(password)
pause()
driver.find_element_by_id("login-submit").click()
pause()
wait.until(EC.element_to_be_clickable(
    (By.ID, "nav-typeahead-wormhole"))
)
pause()
print ("Profil connecte a Linkedin - 1")
