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
#options = webdriver.ChromeOptions()

# Create a new instance of Firefox driver
driver = webdriver.Firefox()

subrubric_urls=[]
data_urls=[]



'''+++++++++++++++++++++++++++++++++++++++++++++++++++++______GETTING LEFT BLOCK DATA___________++++++++++++++++++++++++++++++++++++++++++++++'''

url="https://2gis.ae/dubai/rubrics/subrubrics/110623"

driver.get(url)

sleep(5)

main=driver.find_elements_by_class_name("_r47nf")
first_block=main[0].find_elements_by_class_name("_mq2eit")
total_iterations = len(first_block)
for index, first in enumerate(first_block):
    # If it's the last iteration, break out of the loop
    if index == total_iterations - 1:
        break
    a_tags = first.find_elements_by_tag_name("a")
    for a in a_tags:
    	#print(a.get_attribute("href"))
    	subrubric_urls.append(a.get_attribute("href"))

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++______GETTING RIGHT BLOCK DATA___________++++++++++++++++++++++++++++++++++++++++++++++'''

second_block=driver.find_elements_by_class_name("_13w22bi")
for i in second_block:
	aa_tags=i.find_elements_by_tag_name("a")
	for aa in aa_tags:
		print(aa.get_attribute("href"))
		data_urls.append(aa.get_attribute("href"))

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++______GETTING "MORE" BLOCK DATA___________++++++++++++++++++++++++++++++++++++++++++++++'''
for u in subrubric_urls:
    driver.get(u)
    main=driver.find_elements_by_class_name("_r47nf")
    block=main[1].find_element_by_class_name("_guxkefv")
    dum=block.find_elements_by_class_name("_mq2eit")
    for b in dum:
    	if b.text=="More":
    		b.click()
    		sleep(2)
    		blo=driver.find_elements_by_class_name("_13w22bi")
    		for bl in blo:
    			blooo=bl.find_elements_by_tag_name("a")
    			for m in blooo:
    				print(m.get_attribute("href"))
    				data_urls.append(m.get_attribute("href"))
    	else:
    		b_tags=b.find_elements_by_tag_name("a")
    		for bb in b_tags:
    			print(b.text)
    			print(bb.get_attribute("href"))
    			data_urls.append(bb.get_attribute("href"))
    sleep(2)
    print("Total URLS:",len(data_urls))


# Define the file name for the CSV
csv_file = "data_urls.csv"

# Open the CSV file in write mode
with open(csv_file, 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)
    
    # Iterate through the URLs and write each one to the CSV file
    for url in data_urls:
        if "https://2gis.ae/dubai/rubrics/subrubrics/" not in url:
            writer.writerow([url])

print("CSV file created successfully:", csv_file)