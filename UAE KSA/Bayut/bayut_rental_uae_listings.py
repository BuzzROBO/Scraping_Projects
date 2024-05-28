from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import csv

csvfile = 'bayut_rental_listings.csv'
failed_csvfile = 'failed_urls.csv'  # CSV file to store failed URLs
listing_links = []

# Initialize Firefox webdriver
driver = webdriver.Firefox()
counter = 2
url = "https://www.bayut.com/to-rent/property/uae/"
driver.get(url)
sleep(5)

def is_text_present(text):
    try:
        return text in driver.page_source
    except:
        return False

target_text = "Currently there are no properties available for your search criteria"

# main_block = driver.find_element_by_class_name("bbfbe3d2 be03f78f")
# level1 = main_block.find_element_by_class_name("_459da820")
level2 = driver.find_element_by_class_name("bbfbe3d2")
only_list = level2.find_element_by_tag_name("ul")
li_tags = only_list.find_elements_by_tag_name("li")
for li in li_tags:
    href_att = li.find_elements_by_tag_name("a")
    for href in href_att:
        link = href.get_attribute("href")
        print(link)
        listing_links.append(link)
        # Export link to CSV
        with open(csvfile, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([link])

while not is_text_present(target_text):
    mod = f'page-{counter}'
    u = url + mod
    try:
        driver.get(u)
        sleep(5)
        counter += 1
        level2 = driver.find_element_by_class_name("bbfbe3d2")
        only_list = level2.find_element_by_tag_name("ul")
        li_tags = only_list.find_elements_by_tag_name("li")
        for li in li_tags:
            href_att = li.find_elements_by_tag_name("a")
            for href in href_att:
                link = href.get_attribute("href")
                print(link)
                listing_links.append(link)
                # Export link to CSV
                with open(csvfile, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([link])
    except Exception as e:
        print(f"Failed to load URL: {u}. Error: {str(e)}")
        # Export failed URL to CSV
        with open(failed_csvfile, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([u])

print("Target text found: ", target_text)

# Close the browser
driver.quit()
