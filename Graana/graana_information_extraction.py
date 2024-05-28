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
import json

mod_urls=[]
# with open("graana_information.csv", "w", newline='') as csv_file:
#      writer = csv.writer(csv_file)
#      writer.writerow("URLs")
#driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver=webdriver.Chrome()
# Load the URL
url = "https://www.graana.com/"
driver.get(url)


#####################____________GET BUILD ID_______________######################

# Get the page source
html = driver.page_source

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find the script tag containing the buildId
script_tag = soup.find('script', string=lambda text: 'buildId' in str(text))

# Extract the buildId value
build_id = None
if script_tag:
    script_content = script_tag.string
    if script_content:
        start_index = script_content.find('"buildId":"') + len('"buildId":"')
        end_index = script_content.find('"', start_index)
        build_id = script_content[start_index:end_index]

print("Build ID:", build_id)

#####################____________BUILD JSON URL_______________######################


df = pd.read_csv('graana_karachi_urls_complete.csv',usecols=['id'])
print("Total Number of URLs:",len(df))
for index, row in df.iterrows():
	dum=row['id']
	#print("Orignal URL:", dum)
	parts=dum.split('/')
	extracted_text=parts[4]
	mod=f"https://www.graana.com/_next/data/{build_id}/property/{extracted_text}.json?id={extracted_text}"
	mod_urls.append(mod)
	# print("Modified URL:",mod)
	# print("*"*50)
print("URLs Modified")
#####################____________OPEN NEW TAB OF THE JSON RESPONSE AND EXTRACT DATA_______________######################

data_list=[]

total_count=len(df)
counter=1

for i in mod_urls:
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(i)
    sleep(5)
    json_dum = driver.find_element_by_tag_name("pre")
    json_data = json.loads(json_dum.text)

    data = {
        "id": json_data["pageProps"]["data"]["id"],
        "name": json_data["pageProps"]["data"]["name"],
        "purpose": json_data["pageProps"]["data"]["purpose"],
        "type": json_data["pageProps"]["data"]["type"],
        "customTitleGenerated": json_data["pageProps"]["data"]["customTitleGenerated"],
        "subtype": json_data["pageProps"]["data"]["subtype"],
        "areaId": json_data["pageProps"]["data"]["areaId"],
        "cityId": json_data["pageProps"]["data"]["cityId"],
        "price": json_data["pageProps"]["data"]["price"],
        "size": json_data["pageProps"]["data"]["size"],
        "sizeUnit": json_data["pageProps"]["data"]["sizeUnit"],
        "status": json_data["pageProps"]["data"]["status"],
        "address": json_data["pageProps"]["data"]["address"],
        "description": json_data["pageProps"]["data"]["description"],
        "condition": json_data["pageProps"]["data"]["condition"],
        "countryCode": json_data["pageProps"]["data"]["countryCode"],
        "phone": json_data["pageProps"]["data"]["phone"],
        "primaryFeatures": json_data["pageProps"]["data"]["primaryFeatures"],
        "utilityFeatures": json_data["pageProps"]["data"]["utilityFeatures"],
        "nearByFeatures": json_data["pageProps"]["data"]["nearByFeatures"],
        "expiresAt": json_data["pageProps"]["data"]["expiresAt"],
        "userId": json_data["pageProps"]["data"]["userId"],
        "createdAt": json_data["pageProps"]["data"]["createdAt"],
        "lat": json_data["pageProps"]["data"]["lat"],
        "lng": json_data["pageProps"]["data"]["lng"],
        "area.id": json_data["pageProps"]["data"]["area.id"],
        "area.name": json_data["pageProps"]["data"]["area.name"],
        "city.id": json_data["pageProps"]["data"]["city.id"],
        "city.name": json_data["pageProps"]["data"]["city.name"]
    }

    #data_list.append(data)
    print("="*50)
    print(data)
    print("="*50)
    print("URLS Completed:",counter,"out of",total_count)
    print("Last URL Done:",i)
    print("="*50)
    counter=counter+1
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    sleep(5)

    # Writing data to CSV file in each iteration
    csv_file_name = "graana.csv"
    keys = data.keys()

    with open(csv_file_name, 'a', encoding="utf-8", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        if file.tell() == 0:  # Check if file is empty
            writer.writeheader()
        writer.writerow(data)