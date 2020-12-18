import random
import time
import yaml
import numpy as np
import bs4 as bs

def pause():
    time_break = random.randint(3,5)
    return time.sleep(time_break)

def load_config(path_to_config):
    try:
        with open(path_to_config, 'r') as f:
            config = yaml.load(f, Loader=yaml.loader.FullLoader)
    except FileNotFoundError:
        config = None
    return config

def get_table(driver):

	pause()
	get_div = driver.find_element_by_class_name('table-container')
	html = get_div.get_attribute('innerHTML')
	soup = bs.BeautifulSoup(html,features="html.parser")
	rows = soup.find_all('tr')
	data = []
	for row in rows:
		data.append([row.find_all("td")[0].text,row.find_all("td")[2].text])
	data = np.array([data])
	data = data.reshape((-1,2)).astype(str)
	name_of_card = "ronaldinho_bla_bla"
	np.savetxt(f"{name_of_card}.txt",data,fmt="%s")
	print("saved to file")

def login(driver,email_address,password):

	pause()
	driver.find_element_by_id("email").send_keys(email_address)
	pause()
	driver.find_element_by_id("password").send_keys(password)
	pause()
	button = driver.find_element_by_xpath('//button[@class="btn block"]').click()
	print("Log in successful")

def open_url(driver,url):
    pause()
    driver.get(url)
    print(f"Opened:{url}")