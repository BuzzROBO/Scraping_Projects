from time import sleep
from selenium import webdriver
import csv
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import datetime

# Initialize the list to store all links
all_links = []

# Initialize the Firefox driver
driver = webdriver.Firefox()

# Function to save links to CSV
def save_to_csv(links):
    with open('links.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        for link in links:
            writer.writerow([link])

# Initialize page count
page_count = 1

while True:
    mod_url = f'https://www.viamichelin.com/maps/united_arab_emirates/dubai/_/dubai-_?page={page_count}'
    print("-" * 100)
    print("Fetching URL:", mod_url)
    print("-" * 100)
    driver.get(mod_url)
   # sleep(10)
    # scroll_location=driver.find_element_by_class_name("mb-1")
    # driver.execute_script("arguments[0].scrollIntoView()",scroll_location)
    # print("Scrolled!")
    sleep(3)
    # Increase the page count for the next iteration
    page_count += 1
    
    # Get the page source and parse it with BeautifulSoup
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    
    # Check if no listings are found
    if soup.find(text="This page couldn’t be loaded"):
        print("No Listing Found!")
        break
    
    try:
        # Find the listing block and all listings within it
        listing_block = driver.find_element_by_class_name("mt-4")
        page_listings = listing_block.find_elements_by_tag_name("li")
        page_links = []
        for index, p in enumerate(page_listings):
            if index==2:
                print("*"*10)
                print("Google Ad link")
                print("*"*10)
                continue
            sel = p.find_element_by_tag_name("a")
            link = sel.get_attribute("href")
            print(link)
            print(p.text)
            all_links.append(link)
            page_links.append(link)
        
        # Save the links to CSV
        save_to_csv(page_links)
        
    except Exception as e:
        print("Error Occured:", e)
        pass

# Close the driver after the loop
driver.quit()

print("Scraping finished. All links have been saved to links.csv.")
