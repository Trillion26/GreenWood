from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://<Competitor-Website>/ProductPage1')
price = browser.find_element_by_id('price')
price.text
#You will get the price of RM 89.39
#store it into a data frame
import numpy as np
import pandas as pd
df = pd.DataFrame([["Product A", price.text]], columns=["Product","Price"])
#Repeat the step for Product Page 2
browser.get('https://<Competitor-Website>/ProductPage2')
price = browser.find_element_by_id('price')
#Put in the product B price into the table
df2 = pd.DataFrame([["Product B", price.text]], columns=["Product","Price"])
df.append(df2)
#Save into Excel
df.to_csv(r'PriceList.csv', index = False)