from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import csv

url = 'https://uaebusinessdirectory.com/search_results.php?keyword=&category=3412&location=&submit_search='

driver = webdriver.Firefox()
driver.get(url)

all_business_urls = []
cat = []
cat_id = []
hold_page_urls = []

# # Extract category IDs from the dropdown
# cat_id_dropdown = driver.find_element_by_id("category")
# dum = cat_id_dropdown.find_elements_by_tag_name("option")
# for i in dum:
#     print(i.get_attribute("value"), "-", i.text)
#     cat.append(i.text)
#     cat_id.append(i.get_attribute("value"))

# print("*" * 50)
# print("Total IDs Extracted:", len(cat_id))
# # Export cat_id list to CSV
# with open('category_ids.csv', 'w', encoding="utf-8", newline='') as cat_file:
#     writer_cat = csv.writer(cat_file)
#     for category_id in cat_id:
#         writer_cat.writerow([category_id])

# print(f"{len(cat_id)}Category IDs exported to category_ids.csv")
# print("*" * 50)

with open('category_ids.csv', 'r', encoding="utf-8") as cat_file:
    reader_cat = csv.reader(cat_file)
    for row in reader_cat:
        cat_id.append(row[0])
print(cat_id)
# Open the CSV file in append mode
with open('business_urls.csv', 'a', encoding="utf-8", newline='') as file:
    writer = csv.writer(file)

    for j in cat_id:
        print("ID:", str(j))
        count = 1
        while True:
            try:
                u =f'https://uaebusinessdirectory.com/search_results.php?keyword=&category={j}&page={count}'
                print("Fetching URL:", u)
                print("-" * 100)
                driver.get(u)
                sleep(5)
                
                # Get business listing URLs
                listings_divs = driver.find_elements_by_class_name("listing_results_result")
                for m in listings_divs:
                    tags = m.find_element_by_tag_name("a")
                    tag = tags.get_attribute("href")
                    print(tag)
                    all_business_urls.append(tag)
                    
                    # Write each URL to the CSV file immediately
                    writer.writerow([tag])

                print("-" * 100)
                # Check for pagination (if next page exists)
                nav_bar = driver.find_element(By.CLASS_NAME, "col-lg-8")
                next_button = nav_bar.find_elements(By.XPATH, "//a[contains(@href, 'page={0}')]".format(count + 1))
                
                if next_button:
                    count += 1
                else:
                    break  # Exit the loop if there are no more pages

            except Exception as e:
                print("An exception occurred while processing the URL:", u)
                with open('not.csv', 'a', encoding="utf-8", newline='') as files:
                    writer_not = csv.writer(files)
                    writer_not.writerow([u])
                break  # Break the loop in case of any exception

driver.quit()
