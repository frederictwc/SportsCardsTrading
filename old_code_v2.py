#The output doesn't work!!!
# python package
import csv
import time
import random
import sys
import os
import yaml
import numpy as np
import bs4 as bs
import pandas as pd
import requests


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
from bs4 import BeautifulSoup

# Go to website
# Loop through 2010 seasons to 2020 seasons
driver = webdriver.Chrome()

# Add till 2020
Seasons = ["2011","2012","2013"]

for Season in Seasons:
    url = 'https://www.basketball-reference.com/players/i/irvinky01/gamelog/' + Season
    driver.get(url)
    soup = BeautifulSoup(driver.page_source,'html.parser')
    tables = soup.find_all('table',{"class":["row_summable sortable stats_table now_sortable"]})

    tabs_dic = {}
    for table in tables:
        tab_name = table['id']
        tab_data = [[cell.text for cell in row.find_all(["th","td"])] for row in table.find_all("tr")]
        df = pd.DataFrame(tab_data)
        df.columns = df.iloc[0,:]
        df.drop(index=0,inplace=True)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        tabs_dic[tab_name] = df
        print (Season)
        
#Combine tables and output to CSV
df = pd.concat(tabs_dic, ignore_index=True)
df.to_csv('output.csv')






