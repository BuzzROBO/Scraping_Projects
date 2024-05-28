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

data_urls=[]
failed_urls=[]



'''+++++++++++++++++++++++++++++++++++++++++++++++++++++______GETTING RIGHT BLOCK DATA___________++++++++++++++++++++++++++++++++++++++++++++++'''

urls=["https://2gis.ae/dubai/rubrics/subrubrics/110669",
"https://2gis.ae/dubai/rubrics/subrubrics/110546",
"https://2gis.ae/dubai/rubrics/subrubrics/110547",
"https://2gis.ae/dubai/rubrics/subrubrics/110550",
"https://2gis.ae/dubai/rubrics/subrubrics/110553",
"https://2gis.ae/dubai/rubrics/subrubrics/110554",
"https://2gis.ae/dubai/rubrics/subrubrics/110583",
"https://2gis.ae/dubai/rubrics/subrubrics/110557",
"https://2gis.ae/dubai/rubrics/subrubrics/110558",
"https://2gis.ae/dubai/rubrics/subrubrics/110559",
"https://2gis.ae/dubai/rubrics/subrubrics/110560",
"https://2gis.ae/dubai/rubrics/subrubrics/110561",
"https://2gis.ae/dubai/rubrics/subrubrics/110562",
"https://2gis.ae/dubai/rubrics/subrubrics/110563",
"https://2gis.ae/dubai/rubrics/subrubrics/110564",
"https://2gis.ae/dubai/rubrics/subrubrics/110566",
"https://2gis.ae/dubai/rubrics/subrubrics/110567",
"https://2gis.ae/dubai/rubrics/subrubrics/110568",
"https://2gis.ae/dubai/rubrics/subrubrics/110570",
"https://2gis.ae/dubai/rubrics/subrubrics/110569",
"https://2gis.ae/dubai/rubrics/subrubrics/110572",
"https://2gis.ae/dubai/rubrics/subrubrics/110577",
"https://2gis.ae/dubai/rubrics/subrubrics/110578",
"https://2gis.ae/dubai/rubrics/subrubrics/110579",
"https://2gis.ae/dubai/rubrics/subrubrics/110580",
"https://2gis.ae/dubai/rubrics/subrubrics/110641",
"https://2gis.ae/dubai/rubrics/subrubrics/110642",
"https://2gis.ae/dubai/rubrics/subrubrics/110586",
"https://2gis.ae/dubai/rubrics/subrubrics/110644",
"https://2gis.ae/dubai/rubrics/subrubrics/110643",
"https://2gis.ae/dubai/rubrics/subrubrics/110589",
"https://2gis.ae/dubai/rubrics/subrubrics/110590",
"https://2gis.ae/dubai/rubrics/subrubrics/110591",
"https://2gis.ae/dubai/rubrics/subrubrics/110594",
"https://2gis.ae/dubai/rubrics/subrubrics/110595",
"https://2gis.ae/dubai/rubrics/subrubrics/110596",
"https://2gis.ae/dubai/rubrics/subrubrics/110599",
"https://2gis.ae/dubai/rubrics/subrubrics/110600",
"https://2gis.ae/dubai/rubrics/subrubrics/110601",
"https://2gis.ae/dubai/rubrics/subrubrics/110571",
"https://2gis.ae/dubai/rubrics/subrubrics/110604",
"https://2gis.ae/dubai/rubrics/subrubrics/110605",
"https://2gis.ae/dubai/rubrics/subrubrics/110606",
"https://2gis.ae/dubai/rubrics/subrubrics/110607",
"https://2gis.ae/dubai/rubrics/subrubrics/110608",
"https://2gis.ae/dubai/rubrics/subrubrics/110610",
"https://2gis.ae/dubai/rubrics/subrubrics/110611",
"https://2gis.ae/dubai/rubrics/subrubrics/110613",
"https://2gis.ae/dubai/rubrics/subrubrics/110614",
"https://2gis.ae/dubai/rubrics/subrubrics/110615",
"https://2gis.ae/dubai/rubrics/subrubrics/110616"]


sleep(5)

main=driver.find_elements_by_class_name("_r47nf")

for url in urls:
    try:
        driver.get(url)
        sleep(5)
        second_block=driver.find_elements_by_class_name("_13w22bi")
        for i in second_block:
            aa_tags=i.find_elements_by_tag_name("a")
            for aa in aa_tags:
                print(aa.get_attribute("href"))
                data_urls.append(aa.get_attribute("href"))
    except Exception as e:
        print("Error:",e)
        failed_urls.append(url)

    sleep(5)


print("FAILED URLS:",failed_urls)
# Writing the data to a CSV file
csv_file = "data_urls_remaining.csv"
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["url"])
    for data_url in data_urls:
        writer.writerow([data_url])

# Close the WebDriver
driver.quit()

print("CSV file generated successfully.")