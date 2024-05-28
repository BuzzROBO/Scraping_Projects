# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup
# from selenium.webdriver.chrome.options import Options
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import csv
# from urllib.parse import quote
# import json
# # Set up Firefox options
# #options = webdriver.ChromeOptions()

# # Create a new instance of Firefox driver
# driver = webdriver.Firefox()

# listing_links=[]

# urls=["https://www.olx.com.pk/karachi_g4060695/property-for-rent_c3","https://www.olx.com.pk/islamabad-capital-territory_g2003003/property-for-rent_c3","https://www.olx.com.pk/lahore_g4060673/property-for-rent_c3","https://www.olx.com.pk/rawalpindi_g4060681/property-for-rent_c3"]

# for url in urls:

# 	print("*******************************************************************************************")
# 	print("Current URL:",url)
# 	print("*******************************************************************************************")
# 	driver.get(url)
# 	sleep(2)
# 	#main=driver.find_element_by_class_name("_3513b509")
# 	sleep(5)

# 	########################################___________SCROLLING WEBPAGE____________$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 	print("Scrolling...")
# 	while True:
# 	    try:
# 	        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 	        sleep(3)
# 	        more_button = driver.find_element_by_xpath("//*[contains(text(), 'Load more')]")
# 	        actions = ActionChains(driver)
# 	        actions.move_to_element(more_button).perform()
# 	        #print(more_button.text)
# 	        more_button.click()
# 	        print("Load More Clicked!")
# 	        sleep(5)
# 	    except Exception as e:
# 	        print(e)
# 	        print("Scrolling complete. Beginning URL extraction")
# 	        break


# 	########################################___________EXTRACTING LISTING URLS____________$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 	li_tags=driver.find_elements_by_tag_name("li")
# 	with open('listing_links.csv', mode='a', newline='') as file:
# 	    writer = csv.writer(file)

# 	    for li in li_tags:
# 	        a_tags = li.find_elements_by_tag_name("a")
# 	        for a in a_tags:
# 	            link = a.get_attribute("href")
# 	            listing_links.append(link)
# 	            # Write each link to the CSV file
# 	            writer.writerow([link])


import requests
from bs4 import BeautifulSoup

url = "https://www.olx.com.pk/karachi_g4060695/property-for-rent_c3"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all anchor tags and extract the href attributes
    hrefs = [a.get("href") for a in soup.find_all("a")]
    
    # Print the hrefs
    for href in hrefs:
        print(href)
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
