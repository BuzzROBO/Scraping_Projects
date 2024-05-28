from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import json
from time import sleep
import os.path
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import csv
# Initialize Firefox webdriver
driver = webdriver.Chrome()
cat_texts = []
url="https://www.hidubai.com/categories/"

driver.get(url)

for i in range(3, 46):
    main_block = driver.find_elements_by_class_name("container-fluid")
    cat_list = main_block[i].find_elements_by_tag_name("ul")
    for cat in cat_list:
        titles=cat.find_elements_by_tag_name("a")
        for title in titles:

        	cat_texts.append(title.text)
print(cat_texts)

# Export cat texts to a CSV file
with open('cat_texts.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Category Text'])  # Write header
    for cat_text in cat_texts:
        writer.writerow([cat_text])