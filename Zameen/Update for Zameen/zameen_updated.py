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
import pandas as pd


# with open("zameen_karachi_urls.csv", "w", newline='') as csv_file:
#      writer = csv.writer(csv_file)
driver = webdriver.Firefox(executable_path="geckodriver.exe")
adblockfile = r"C:\\Users\\Administrator\\Desktop\\Office Work\\Zameen\\Update for Zameen\\adblock.xpi"
driver.install_addon(adblockfile, temporary=True)
sleep(5)
# href_attributes=[]
all_areas=[]
url='https://www.zameen.com/'
df=pd.read_csv("karachi_zameen_areas.csv")
driver.get(url)
sleep(5)
rent_classes=driver.find_elements_by_class_name("_34ca7e49")
rent_button=rent_classes[1]
print(rent_button.text)
rent_button.click()
sleep(2)
bars=driver.find_elements_by_class_name("f41f950f")
bar=bars[0].find_element_by_class_name("_8f6046d1")
inputt=bar.find_element_by_tag_name("input")
for index, row in df.iterrows():
    inputt.clear()  # Clear the input field
    inputt.send_keys(row['name_displ'])  # Send the value from the 'name_displ' column
    sleep(5)
    all_locations = bar.find_elements_by_tag_name("span")
    for index, value in enumerate(all_locations):
        if index % 2 == 0:  # Check if the index is even
            print(value.text)
            all_areas.append(value.text)
print(all_areas)

# Convert the list to a pandas DataFrame
df_areas = pd.DataFrame(all_areas, columns=['Area'])

# Specify the file path for the CSV file
csv_file_path = "all_areas_original.csv"

# Export the DataFrame to a CSV file
df_areas.to_csv(csv_file_path, index=False)

print("CSV file exported successfully.")