from selenium import webdriver
from time import sleep
import re
import csv
from dbConfiguration import DbConfig
import os
import sys

# Database configuration
db = DbConfig('172.16.130.23', 'TPLMaps', 5432, 'qgis.plugin', 'assigncity')
conn = db.ConnectDb()

# Function to extract latitude and longitude from URL
def extract_lat_lon(url):
    pattern = r'points/%7C(-?\d+\.\d+)%2C(-?\d+\.\d+)'
    match = re.search(pattern, url)
    if match:
        lat = float(match.group(1))
        lon = float(match.group(2))
        return lat, lon
    else:
        return None

# Initialize Firefox webdriver
driver = webdriver.Firefox()

urls = []
with open('2gis_export1.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        urls.append(row[0])

print("*" * 25)
print("Total URLs:", len(urls))
print("*" * 25)

for u in urls:
    try:
        driver.get(u)
        sleep(5)

        try:
            main = driver.find_element_by_class_name("_1tfwnxl")
            makani = driver.find_elements_by_class_name("_1p8iqzw")
            name = main.find_element_by_tag_name("h1").text
            name = name.replace("'", " ")
            name = name.replace('"', ' ')
            name = name.replace(",", " ")
            name = name.replace(";", " ")
            name = name.replace(":", " ")
            name = name.replace(".", " ")
            Name = name
            print("Name:", Name)
        except Exception as e:
            print("An exception occurred while extracting name:", str(e))
            Name = "None"
            pass

        try:
            address = driver.find_element_by_class_name("_er2xx9").text
            address = address.replace("'", " ")
            address = address.replace('"', ' ')
            address = address.replace(",", " ")
            address = address.replace(";", " ")
            address = address.replace(":", " ")
            address = address.replace(".", " ")
            Address = address + " " + makani[1].text
            if "It’s my company " in Address:
                Address = Address.replace("It’s my company ", "")
            print("Address:", Address)
        except Exception as e:
            print("An exception occurred while extracting address:", str(e))
            Address = "None"
            pass

        try:
            makani = driver.find_elements_by_class_name("_1p8iqzw")
            Makani = makani[0].text
            if "°" in Makani:
                Makani = "None"
            print("Makani No:", Makani)
        except Exception as e:
            print("An exception occurred while extracting Makani No:", str(e))
            Makani = "None"
        
        try:
            category = driver.find_element_by_class_name("_1idnaau").text
            category = category.replace("'", " ")
            category = category.replace('"', ' ')
            category = category.replace(",", " ")
            category = category.replace(";", " ")
            category = category.replace(":", " ")
            category = category.replace(".", " ")
            Category = category
            print("Category:", Category)
        except Exception as e:
            print("An exception occurred while extracting category:", str(e))
            Category = "None"
            pass

        try:
            phone = driver.find_element_by_class_name("_b0ke8")
            ph = phone.find_element_by_tag_name("a").get_attribute("href")
            Phone = ph
            print("Phone No:", Phone)
        except Exception as e:
            print("An exception occurred while extracting phone number:", str(e))
            Phone = "None"
            pass

        try:
            coord_dr = driver.find_elements_by_class_name("_vaj62s")
            coord = coord_dr[2].find_element_by_tag_name("a")
            print("URL:", coord.get_attribute("href"))
            latitude, longitude = extract_lat_lon(coord.get_attribute("href"))
            print("Latitude:", longitude)
            print("Longitude:", latitude)
            Coordinate = coord.get_attribute("href")
        except Exception as e:
            print("An exception occurred while extracting coordinates:", str(e))
            latitude = "None"
            longitude = "None"
            Coordinate = "None"
            pass

        print("1", Name, "2", Address, "3", Makani, "4", Category, "5", Phone, "6", Coordinate, "7", longitude, "8", latitude)
        print("=" * 50)
        print("query", """INSERT INTO two_gis (name, address, makni, cat, phone, url, lat, lng) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')""".format(Name, Address, Makani, Category, Phone, Coordinate, longitude, latitude))
        print("=" * 50)
        try:
            db.DbModifyQuery("""INSERT INTO two_gis (name, address, makni, cat, phone, url, lat, lng) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')""".format(Name, Address, Makani, Category, Phone, Coordinate, longitude, latitude))
            print("=" * 50)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            pass

    except Exception as e:
        print("An exception occurred while processing the URL:", u)
        with open('not.csv', 'a', encoding="utf-8", newline='') as files:
            writer = csv.writer(files)
            writer.writerow([u])
            pass

driver.quit()
