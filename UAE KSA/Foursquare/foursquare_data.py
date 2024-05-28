from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv
import datetime

# Initialize the webdriver
driver = webdriver.Firefox()

# URLs to scrape
urls = []

with open('foursquare_listings.csv', newline='') as csvfile:
    # Create a csv reader object
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if row:
            urls.append(row[0])

# Initialize lists to store data
names = []
categories = []
addresses = []
cities = []
ratings = []
total_ratings_list = []
phones = []
websites = []
social_fbs = []
social_twis = []
social_inss = []
directions_links = []
latitudes = []
longitudes = []

for url in urls:
    print("-" * 100)
    print("Current URL:", url)
    print("-" * 100)
    try:
        driver.get(url)

        # Scraping logic...
        try:
            section = driver.find_element_by_class_name("primaryInfo")
            try:
                name_block = section.find_element_by_class_name("venueName")
                name = name_block.text
            except:
                name = None

            try:
                cat_block = section.find_element_by_class_name("categories")
                category = cat_block.text.replace("$", '')
            except:
                category = None

            try:
                location_block = section.find_element_by_class_name("locationInfo")
                address = location_block.text
            except:
                address = None

            try:
                city_block = section.find_element_by_class_name("venueCity")
                city = city_block.text
            except:
                city = None
        except:
            pass

        try:
            rating_block = driver.find_element_by_css_selector("span.venueScore.positive")
            rating = rating_block.text  # Modify as per actual structure

            total_rating_block = driver.find_element_by_class_name("numRatings")
            total_ratings = total_rating_block.text
        except:
            rating = None
            total_ratings = None

        try:
            more_info_block = driver.find_element_by_class_name("venueDetails")

            try:
                href_directions_block = more_info_block.find_element_by_class_name("venueDirections")
                href_directions_tag = href_directions_block.find_element_by_tag_name("a")
                href_directions_link = href_directions_tag.get_attribute("href")
                coordinates = href_directions_link.split('daddr=')[1]
                latitude, longitude = coordinates.split(',')
            except:
                href_directions_link = None
                latitude = None
                longitude = None

            try:
                phone_block = more_info_block.find_element_by_class_name('tel')
                phone = phone_block.text
            except:
                phone = None

            try:
                web_block = more_info_block.find_element_by_class_name('url')
                website = web_block.get_attribute("href")
            except:
                website = None

            try:
                facebook_block = more_info_block.find_element_by_class_name("facebookPageLink")
                social_fb = facebook_block.get_attribute("href")
            except:
                social_fb = None

            try:
                twitter_block = more_info_block.find_element_by_class_name("twitterPageLink")
                social_twi = twitter_block.get_attribute("href")
            except:
                social_twi = None

            try:
                instagram_block = more_info_block.find_element_by_class_name("instagramPageLink")
                social_ins = instagram_block.get_attribute("href")
            except:
                social_ins = None

            names.append(name)
            categories.append(category)
            addresses.append(address)
            cities.append(city)
            ratings.append(rating)
            total_ratings_list.append(total_ratings)
            phones.append(phone)
            websites.append(website)
            social_fbs.append(social_fb)
            social_twis.append(social_twi)
            social_inss.append(social_ins)
            directions_links.append(href_directions_link)
            latitudes.append(latitude)
            longitudes.append(longitude)

            # Append data to CSV
            with open("Foursquare.csv", mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                # Write headers if file is empty
                if file.tell() == 0:
                    writer.writerow([
                        "Name", "Category", "Address", "City", "Rating", "Total Ratings",
                        "Phone", "Website", "Facebook URL", "Twitter URL", "Instagram URL",
                        "Directions Link", "Latitude", "Longitude"
                    ])

                # Write data for current URL
                writer.writerow([
                    name, category, address, city, rating, total_ratings, phone, website,
                    social_fb, social_twi, social_ins, href_directions_link, latitude, longitude
                ])

        except Exception as e:
            print(e)
            pass

    except Exception as e:
        print(e)
        pass

# Close the webdriver
driver.quit()
