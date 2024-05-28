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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

list_links=[]
# with open("zameen_karachi_urls.csv", "w", newline='') as csv_file:
#      writer = csv.writer(csv_file)
driver = webdriver.Firefox(executable_path="geckodriver.exe")
adblockfile = r"C:\\Users\\Administrator\\Desktop\\Office Work\\Zameen\\Update for Zameen\\adblock.xpi"
driver.install_addon(adblockfile, temporary=True)
sleep(5)
fail=[]
fail_main=[]
# href_attributes=[]
all_areas=[]
urls='https://www.zameen.com/'
df=pd.read_csv("all_areas.csv")
temp=len(df)
hold=1
for index, row in df.iterrows():
	driver.get(urls)
	sleep(5)
	rent_classes=driver.find_elements_by_class_name("_34ca7e49")
	rent_button=rent_classes[1]
	print(rent_button.text)
	rent_button.click()
	sleep(10)
	bars=driver.find_elements_by_class_name("f41f950f")
	bar=bars[0].find_element_by_class_name("_8f6046d1")
	inputt=bar.find_element_by_tag_name("input")
	counter=1
	inputt.clear()  # Clear the input field
	inputt.send_keys(row['Areas'])  # Send the value from the 'name_displ' column
	sleep(1)
	inputt.send_keys(Keys.ENTER)
	sleep(5)
	while True:
		url=driver.current_url
		parts=url.split("-")
		parts[-1]=str(counter)+".html"
		new_url="-".join(parts)
		counter=counter+1
		print("Navigating to:",new_url)
		try:
			driver.get(new_url)
			WebDriverWait(driver,10).until(EC.presence_of_element_located((By.TAG_NAME,'body')))
			print("*****WAITING******")
		except TimeoutException:
			print("URL FAILED!")
			fail.append(new_url)
			with open("Failed_urls_pagination.csv","w",newline='') as csvfile:
				csvwriter=csv.writer(csvfile)
				for jam in fail:
					csvwriter.writerow([jam])
			print("Timeout Occured")
			pass
		sleep(3)
		page_source=driver.page_source
		soup=BeautifulSoup(page_source,'html.parser')
		if soup.find(text="Sorry, there are no active properties matching your criteria."):
			print("No Properties!")
			break
		try:
			target_block = driver.find_element_by_class_name("bbfbe3d2")
			target_block_new = target_block.find_element_by_class_name("_357a9937")
			targets = target_block_new.find_elements_by_class_name("ef447dde")
			for target in targets:
				dum=target.find_element_by_class_name("f74e80f3")
				tag_name=dum.find_element_by_tag_name("a")
				print(tag_name.get_attribute("href"))
				list_links.append(tag_name.get_attribute("href"))
			print("Total Links Collected:",len(list_links))
			with open("new_links.csv",'w',newline='') as csvfile:
				csvwriter=csv.writer(csvfile)
				csvwriter.writerow(['URL'])
				for link in list_links:
					csvwriter.writerow([link])
		except Exception as e:
			print("Error:",e)
			pass
	print(hold,f"out of {temp} Areas Done.")
	hold=hold+1

driver.quit()
#     all_locations = bar.find_elements_by_tag_name("span")
#     for index, value in enumerate(all_locations):
#         if index % 2 == 0:  # Check if the index is even
#             print(value.text)
#             all_areas.append(value.text)
# print(all_areas)

# # Convert the list to a pandas DataFrame
# df_areas = pd.DataFrame(all_areas, columns=['Area'])

# # Specify the file path for the CSV file
# csv_file_path = "all_areas.csv"

# # Export the DataFrame to a CSV file
# df_areas.to_csv(csv_file_path, index=False)

# print("CSV file exported successfully.")