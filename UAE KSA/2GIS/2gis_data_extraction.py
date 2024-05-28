from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

import csv

# Initialize Firefox webdriver
driver = webdriver.Firefox()

# Read URLs from the CSV file
df = pd.read_csv("2gis_urls_all.csv")
urls = df['url'].tolist()
total_urls = len(urls)
print("*" * 25)
print("Total URLs:", total_urls)
print("*" * 25)

# Failed URLs list to store URLs that failed to process
failed_urls = []
all_json_data=[]
# Loop through each URL
for url in urls:
    print("Current URL:", url)
    driver.get(url)
    sleep(15)
    dum = 0
    dum_1 = 0
    while True:
        sleep(5)
        try:
            button = driver.find_element_by_class_name("_n5hmn94")
            driver.execute_script("arguments[0].scrollIntoView()", button)
            print("SCROLL!")
        except:
            print("NO NAV BAR!")
        try:
            sleep(5)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            if soup.find(text="Мы заметили подозрительную") is not None:
                print("Captcha URL")
                break
            dum = driver.find_elements_by_class_name("_zjunba")
            for d in dum:
                hold = d.find_element_by_tag_name("a")
                url_to_append = hold.get_attribute("href")
                all_json_data.append({'url': url_to_append})
                print(url_to_append)
                # Append the URL to the CSV file
                with open('2gis_export.csv', 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([url_to_append])
        except Exception as e:
            print("An error occurred while processing the URL:", url)
            print("Error message:", str(e))
            # Add the failed URL to the list
            failed_urls.append(url)
            break
        buttons = driver.find_elements_by_class_name("_n5hmn94")
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        if soup.find(text="Add company") is not None:
            print("Signal found!")
            break
        else:
            if len(buttons) == 2:
                buttons[1].click()
            else:
                buttons[0].click()

# Close the webdriver
driver.quit()

# Print failed URLs, if any
if failed_urls:
    print("Failed URLs:")
    for failed_url in failed_urls:
        print(failed_url)
