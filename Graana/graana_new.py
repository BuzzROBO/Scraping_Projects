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


with open("graana_all_urls_commercial_residential.csv", "w", newline='') as csv_file:
     writer = csv.writer(csv_file)
     writer.writerow("URLs")

driver = webdriver.Firefox(executable_path="geckodriver.exe")
urls=["https://www.graana.com/rent/residential-properties-rent-Rawalpindi-3/", "https://www.graana.com/rent/residential-properties-rent-Islamabad-1/", "https://www.graana.com/rent/residential-properties-rent-Lahore-2/",  "https://www.graana.com/rent/commercial-properties-rent-Islamabad-1/", "https://www.graana.com/rent/commercial-properties-rent-Rawalpindi-3/", "https://www.graana.com/rent/commercial-properties-rent-Lahore-2/", "https://www.graana.com/rent/commercial-properties-rent-Karachi-169/","https://www.graana.com/rent/residential-properties-rent-Karachi-169/"]
append="/?pageSize=30&page="
counter=0
sleep(5)
hold_urls=[]
for row in urls:
	while True:
		#print(row)
		url=row+f"/?pageSize=30&page={counter}"
		print("Navigating to:",url)
		try:
			driver.get(url)
			sleep(10)
			counter=counter+1
			page_source=driver.page_source
			soup=BeautifulSoup(page_source,'html.parser')
			if soup.find(text="No Property Found"):
				print("No Property Found")
				counter=1
				break
			try:
				main=driver.find_elements_by_css_selector("div.MuiBox-root.mui-style-17zbhp0")
				for j in main:
					href=j.find_element_by_tag_name("a")
					hold=href.get_attribute("href")
					print(href.get_attribute("href"))
					hold_urls.append(hold)
				print("Length of Links File:", len(hold_urls))
				with open("graana_all_urls_commercial_residential.csv", "w", newline='') as csvfile:
					csvwriter=csv.writer(csvfile)
					for ur in hold_urls:
						csvwriter.writerow([ur])
			except Exception as e:
				print("Error Occurred:", str(e))
				pass
		except Exception as e:
			print("Error:",e)
			print("Last URL:",url)
			break

driver.quit()

		