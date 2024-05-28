# from time import sleep
# from selenium import webdriver
# import csv
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
# import datetime
# import csv

# # Initialize the list to store all links

# driver=webdriver.Firefox()
# all_listings=[]
# # categories=[]

# # parent_url='https://foursquare.com/explore?mode=url&near=Dubai%2C%20United%20Arab%20Emirates&nearGeoId=72057594038220159&q='

# # with open('categories.csv', newline='') as csvfile:
# #     # Create a csv reader object
# #     csvreader = csv.reader(csvfile)
# #     for row in csvreader:
# #     	if row:
# #     		categories.append(row[0])

# # print("Total URLs:",len(categories))
# # #url='https://foursquare.com/explore?mode=url&near=Dubai%2C%20United%20Arab%20Emirates&nearGeoId=72057594038220159&q=Food'

# # for cat in categories:
# # 	url=f'https://foursquare.com/explore?mode=url&near=Dubai%2C%20United%20Arab%20Emirates&nearGeoId=72057594038220159&q={cat}'
# # 	urls.append(url)

# # # Write the urls to a new CSV file
# # with open('urls.csv', mode='w', newline='') as csvfile:
# #     csvwriter = csv.writer(csvfile)
# #     for url in urls:
# #         csvwriter.writerow([url])

# #print("URLs have been successfully exported to urls.csv")

# urls=[]

# with open('urls.csv', newline='') as csvfile:
#     # Create a csv reader object
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#     	if row:
#     		urls.append(row[0])

# for url in urls:
# 	driver.get(url)
# 	count=0
# 	while True:
# 		try:
# 			if count==15:
# 				break
# 			button=driver.find_element_by_class_name("moreResults")
# 			driver.execute_script("arguments[0].scrollIntoView()", button)
# 			print("Found Button. Clicking...")
# 			more_results=driver.find_element_by_class_name("moreResults")
# 			if more_results.text=='':
# 				break
# 			more_results.click()
# 			count=count+1
# 			sleep(5)
# 		except:
# 			break

# 	print("Scrolling completed!")
# 	sleep(5)
# 	container=driver.find_element_by_id("container")
# 	res=container.find_element_by_id("results")
# 	listings=res.find_elements_by_tag_name("li")
# 	c=1
# 	for lis in listings:
# 		try:
# 			dum=lis.find_element_by_tag_name("a")
# 			listing_link=dum.get_attribute("href")
# 			if "https://foursquare.com/v/" in listing_link:
# 				all_listings.append(listing_link)
# 		except:
# 			print("Reached end of page!")



from time import sleep
from selenium import webdriver
import csv
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import datetime
import csv

# Initialize the list to store all links

driver = webdriver.Firefox()
all_listings = []

# Load the URLs from the CSV file
urls = []
with open('urls.csv', newline='') as csvfile:
    # Create a csv reader object
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if row:
            urls.append(row[0])

# Open the CSV file in append mode
with open('listings.csv', mode='a', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    for url in urls:
    	print("*"*100)
    	print("Current URL:",url)
    	print("*"*100)
        driver.get(url)
        count = 0
        while True:
            try:
                if count == 15:
                    break
                button = driver.find_element_by_class_name("moreResults")
                driver.execute_script("arguments[0].scrollIntoView()", button)
                print("Found Button. Clicking...")
                more_results = driver.find_element_by_class_name("moreResults")
                if more_results.text == '':
                    break
                more_results.click()
                count = count + 1
                sleep(5)
            except:
                break

        print("Scrolling completed!")
        sleep(5)
        container = driver.find_element_by_id("container")
        res = container.find_element_by_id("results")
        listings = res.find_elements_by_tag_name("li")
        
        for lis in listings:
            try:
                dum = lis.find_element_by_tag_name("a")
                listing_link = dum.get_attribute("href")
                if "https://foursquare.com/v/" in listing_link:
                	print(listing_link)
                    all_listings.append(listing_link)
                    # Write the URL to the CSV file
                    csvwriter.writerow([listing_link])
            except:
                print("Reached end of page!")
                print("-"*100)
                print("-"*100)

# Close the driver
driver.quit()