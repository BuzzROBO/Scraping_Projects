from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import csv
from urllib.parse import quote
import json

cat_list=[]
# Create a new instance of Firefox driver
driver = webdriver.Firefox()

urls=["https://maps.me/maps/country-lmrt-l-rbyw-lmtwhd/city-dubai-31248510/","https://maps.me/maps/country-lmrt-l-rbyw-lmtwhd/city-bw-zby--4479763/","https://maps.me/maps/country-lmrt-l-rbyw-lmtwhd/city-sharjah-847933749/"]

for url in urls:
	driver.get(url)
	sleep(5)
	block_categories=driver.find_element_by_class_name("block-categories")
	cat_links=block_categories.find_elements_by_tag_name("a")
	for cat in cat_links:
		print(cat.get_attribute("href"))
		cat_list.append(cat.get_attribute("href"))

# Write data to a CSV file
with open('category_links.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category Links'])
    for link in cat_list:
        writer.writerow([link])


poi_links=[]
# driver=webdriver.Firefox()
urls=[]
with open('category_links.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        urls.append(row[0])
print("Total Category URLS:",len(urls))