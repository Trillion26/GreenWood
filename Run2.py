from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import Tkinter

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get('https://www.boots.com/')



BootsSearch = driver.find_element(by=By.ID,value='AlgoliaSearchInput')
BootsSearch.send_keys('Selenium')

print(header.text)
