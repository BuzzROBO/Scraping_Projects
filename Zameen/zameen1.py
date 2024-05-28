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
from datetime import datetime
# Read all the data from the CSV file into a list
url_data = []
links=[]

adblocker_extension_path = 'adblocker.crx'

extension_path = "adblocker_ultimate-3.8.21.xpi"

with open("href_attributes.csv", "r", newline="") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        url_data.append(row)

# Initialize counter
counter = 1
driver = webdriver.Firefox(executable_path="geckodriver.exe")

sleep(10)
# Process each URL
for row in url_data:
    # Extract the URL from the row
    while True:
        url = row[0]
        
        # Split the URL by "-"
        parts = url.split("-")
        
        # Replace the last part with the counter value
        parts[-1] = str(counter) + ".html"
        
        # Join the parts back to form the new URL
        new_url = "-".join(parts)
        
        # Increment counter for the next URL
        counter += 1
        
        # Now you can navigate to the new_url using Selenium
        print("Navigating to:", new_url)
        
        # Retrieve page content
        driver.get(new_url)
        sleep(5)
        page_source = driver.page_source
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')
        
        # Find the text "Sorry, there are no active properties matching your criteria."
        if soup.find(text="Sorry, there are no active properties matching your criteria."):
            print("No Property Found")
            counter=1
            break  # Break the loop if the text is found
        
        try:
            target_block = driver.find_element_by_class_name("bbfbe3d2")
            target_block_new = target_block.find_element_by_class_name("_357a9937")
            targets = target_block_new.find_elements_by_class_name("ef447dde")
            for target in targets:
            	dum=target.find_element_by_class_name("f74e80f3")
            	tag_name=dum.find_element_by_tag_name("a")
            	print(tag_name.get_attribute("href"))
            	links.append(tag_name.get_attribute("href"))
            print("Length of Links FIle:",len(links))

            # Write links to CSV file
            with open('zameen_links.csv', 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(['URL'])
                for link in links:
                    csvwriter.writerow([link])
                
        except Exception as e:
            print("Error occurred:", str(e))
            pass

# Close the WebDriver
driver.quit()