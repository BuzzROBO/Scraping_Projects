from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import csv
city=[]
title=[]
location_href=[]
lat=[]
lon=[]
work_day=[]
work_hour=[]

driver = webdriver.Firefox(executable_path="geckodriver.exe")
url="https://www.aljfinance.com/en/contact-us/branch-locator"
driver.get(url)
sleep(5)
main=driver.find_element_by_id("block-aljuf-content")
locator_Block=main.find_element_by_class_name("node__content")
all_blocks=locator_Block.find_elements_by_class_name("views-row")
counter=0
for i in all_blocks:
    print("***********************************")
    city_block=i.find_element_by_class_name("field--name-field-city")
    title_block=i.find_element_by_class_name("field--name-node-title")
    work_days=i.find_element_by_class_name("field--name-field-postition")
    work_hours=i.find_element_by_class_name("field--name-field-working-hours")
    print(city_block.text)
    city.append(city_block.text)
    print(title_block.text)
    title.append(title_block.text)
    print(work_days.text)
    work_day.append(work_days.text)
    print(work_hours.text)
    work_hour.append(work_hours.text)
    href_link=i.find_element_by_tag_name("a")
    location_href.append(href_link.get_attribute("href"))
    print(href_link.get_attribute("href"))
    link=href_link.get_attribute("href")
    try:
    	lat_lon_str=link.split('=')[1]
    	latitude,longitude=lat_lon_str.split(',')
    except:
    	print("URL ERROR")
    print(latitude)
    lat.append(latitude)
    print(longitude)
    lon.append(longitude)
        

# print(city)
# print(title)
# print(work_days)
# print(work_hours)
# print(location_href)
# print(lat)
# print(lon)
print("Total Count:", len(city))
driver.quit()

# Exporting data to CSV
with open('aljuf.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['City', 'Title', 'Work Day', 'Work Hour', 'Location Href', 'Latitude', 'Longitude'])
    for i in range(len(city)):
        writer.writerow([city[i], title[i], work_day[i], work_hour[i], location_href[i], lat[i], lon[i]])