from time import sleep
from selenium import webdriver
import csv
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.service import Service
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# from more_itertools import unique_everseen
import csv
import sys, os
import traceback
import datetime
from bs4 import BeautifulSoup
import requests
import openpyxl
import re

header = ['Branch Code',"Location Address","Contact Details","Latitude","Longitude"]

with open("ajk.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(header)



url="https://bankajk.com/branches.php"
driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get(url)
sleep(5)
codes=[]
location=[]
contact=[]
location_urls=[]
lat=[]
lon=[]

main=driver.find_element_by_id("main")
table=main.find_element_by_class_name("table-branch")
all_data=table.find_elements_by_tag_name("tr")

for i in all_data:
    counter = 0
    all_dataa = i.find_elements_by_tag_name("td")
    for j in all_dataa:
        if counter == 0:
            codes.append(j.text)
        elif counter == 1:
            location_text = j.text
            location_link = j.find_element_by_tag_name("a")
            location_url = location_link.get_attribute("href")
           # if 'https://bankajk.com/branches.php#' not in location_url:
            location.append(location_text)
            location_urls.append(location_url)
        elif counter == 2:
            contact.append(j.text)
        counter = counter + 1



print(codes)
print(location)
print(contact)
print(location_urls)


data = zip(codes, location, contact, location_urls)

# Writing the data to a CSV file
with open('ajk.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write the header
    writer.writerow(['Code', 'Location', 'Contact', 'Location URL'])
    
    # Write the data rows
    writer.writerows(data)

sleep(10)



