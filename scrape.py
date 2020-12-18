import csv
import sys
import os
from selenium import webdriver
from utils import pause,load_config,get_table,login,open_url

CONFIG = load_config("configuration.yml")
email_address = CONFIG["CREDENTIALS"]["USERNAME"]
password = CONFIG["CREDENTIALS"]["PASSWORD"]
url = CONFIG["URL"]

driver = webdriver.Chrome()

open_url(driver,url)
login(driver,email_address,password)
open_url(driver,url)
get_table(driver)



















