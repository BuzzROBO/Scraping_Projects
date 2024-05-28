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
# Set up Firefox options
options = webdriver.ChromeOptions()

# Create a new instance of Firefox driver
driver = webdriver.Chrome(options=options)

href_attributes=[]

#urls = ["https://www.zameen.com/all_locations/Lahore-1-1-1.html","https://www.zameen.com/all_locations/Lahore-1-1-2.html","https://www.zameen.com/all_locations/Lahore-1-1-3.html","https://www.zameen.com/all_locations/Lahore-1-2-1.html","https://www.zameen.com/all_locations/Lahore-1-2-2.html","https://www.zameen.com/all_locations/Lahore-1-2-3.html","https://www.zameen.com/all_locations/Karachi-2-1-1.html","https://www.zameen.com/all_locations/Karachi-2-1-2.html","https://www.zameen.com/all_locations/Karachi-2-1-3.html","https://www.zameen.com/all_locations/Karachi-2-2-1.html","https://www.zameen.com/all_locations/Karachi-2-2-2.html","https://www.zameen.com/all_locations/Karachi-2-2-3.html","https://www.zameen.com/all_locations/Islamabad-3-1-1.html","https://www.zameen.com/all_locations/Islamabad-3-1-2.html","https://www.zameen.com/all_locations/Islamabad-3-1-3.html","https://www.zameen.com/all_locations/Islamabad-3-2-1.html","https://www.zameen.com/all_locations/Islamabad-3-2-2.html","https://www.zameen.com/all_locations/Islamabad-3-2-3.html","https://www.zameen.com/all_locations/Rawalpindi-41-1-1.html","https://www.zameen.com/all_locations/Rawalpindi-41-1-2.html","https://www.zameen.com/all_locations/Rawalpindi-41-1-3.html","https://www.zameen.com/all_locations/Rawalpindi-41-2-1.html","https://www.zameen.com/all_locations/Rawalpindi-41-2-2.html","https://www.zameen.com/all_locations/Rawalpindi-41-2-3.html"]
urls=["https://www.zameen.com/all_locations/Lahore-1-2-1.html",
"https://www.zameen.com/all_locations/Lahore-1-2-2.html",
"https://www.zameen.com/all_locations/Lahore-1-2-3.html",
"https://www.zameen.com/all_locations/Karachi-2-2-1.html",
"https://www.zameen.com/all_locations/Karachi-2-2-2.html",
"https://www.zameen.com/all_locations/Karachi-2-2-3.html",
"https://www.zameen.com/all_locations/Islamabad-3-2-1.html",
"https://www.zameen.com/all_locations/Islamabad-3-2-2.html",
"https://www.zameen.com/all_locations/Islamabad-3-2-3.html",
"https://www.zameen.com/all_locations/Rawalpindi-41-2-1.html",
"https://www.zameen.com/all_locations/Rawalpindi-41-2-2.html",
"https://www.zameen.com/all_locations/Rawalpindi-41-2-3.html"]
#driver.get(url)
for url in urls:
	driver.get(url)
	sleep(3)
	Homes_Block=driver.find_element_by_class_name("u-mb40")
	all_urls=Homes_Block.find_elements_by_tag_name('a')
	print("Appending href attributes!")
	for i in all_urls:

		href_attributes.append(i.get_attribute("href"))
	print(href_attributes)

with open('href_attributes_rent.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['URL'])
    for href in href_attributes:
        csvwriter.writerow([href])