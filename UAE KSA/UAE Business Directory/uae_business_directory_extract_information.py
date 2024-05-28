import csv
import requests
from bs4 import BeautifulSoup

# Read URLs from the CSV file
urls = []
with open('business_urls.csv', 'r', encoding="utf-8") as url_file:
    reader_url = csv.reader(url_file)
    for row in reader_url:
        urls.append(row[0])
print("Total links:", len(urls))

# Function to extract data from a single URL
def extract_data(url):
    # Fetch the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Function to extract text based on itemprop
        def extract_itemprop(soup, itemprop):
            tag = soup.find('span', itemprop=itemprop)
            return tag.text.strip() if tag else None
        
        # Function to extract content attribute based on itemprop
        def extract_itemprop_content(soup, itemprop):
            tag = soup.find('span', itemprop=itemprop)
            return tag['content'].strip() if tag and 'content' in tag.attrs else None
        
        # Extract the required information
        street_address = extract_itemprop(soup, 'streetAddress')
        postal_code_raw = extract_itemprop(soup, 'postalCode')
        postal_code = ''.join(filter(str.isdigit, postal_code_raw)) if postal_code_raw else None
        address_country = extract_itemprop(soup, 'addressCountry')
        telephone = extract_itemprop(soup, 'telephone')
        fax_number = extract_itemprop(soup, 'faxNumber')
        
        # Extract latitude and longitude from the content attribute
        latitude = extract_itemprop_content(soup, 'latitude')
        longitude = extract_itemprop_content(soup, 'longitude')
        print("Address:", street_address)
        print("Postal Code:", postal_code)
        print("Country:", address_country)
        print("Telephone:", telephone)
        print("Fax Number:", fax_number)
        print("Latitude:", latitude)
        print("Longitude", longitude)
        
        # Return the extracted information as a dictionary
        return {
            'URL': url,
            'Street Address': street_address,
            'Postal Code': postal_code,
            'Address Country': address_country,
            'Telephone': telephone,
            'Fax Number': fax_number,
            'Latitude': latitude,
            'Longitude': longitude
        }
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

# Prepare to write the data to a new CSV file
output_file = 'extracted_business_data.csv'
fieldnames = ['URL', 'Street Address', 'Postal Code', 'Address Country', 'Telephone', 'Fax Number', 'Latitude', 'Longitude']

# Open the output CSV file for writing
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Loop over the URLs and extract data
    for url in urls:
        try:
            print("-" * 50)
            data = extract_data(url)
            print("-" * 50)
            if data:
                writer.writerow(data)
                # Print the extracted information
        except Exception as e:
            print("An Exception occurred while processing the URL:", url)
            with open('failed.csv', 'a', encoding="utf-8", newline='') as files:
                writer_failed = csv.writer(files)
                writer_failed.writerow([url])

print(f"Data extraction complete. Extracted data saved to {output_file}.")
import csv
import requests
from bs4 import BeautifulSoup

# Read URLs from the CSV file
urls = []
with open('business_urls.csv', 'r', encoding="utf-8") as url_file:
    reader_url = csv.reader(url_file)
    for row in reader_url:
        urls.append(row[0])
print("Total links:", len(urls))

# Function to extract data from a single URL
def extract_data(url):
    # Fetch the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Function to extract text based on itemprop
        def extract_itemprop(soup, itemprop):
            try:
                tag = soup.find('span', itemprop=itemprop)
                return tag.text.strip() if tag else None
            except Exception as e:
                return None
        
        # Function to extract content attribute based on itemprop
        def extract_itemprop_content(soup, itemprop):
            try:
                tag = soup.find('span', itemprop=itemprop)
                return tag['content'].strip() if tag and 'content' in tag.attrs else None
            except Exception as e:
                return None
        
        # Extract the required information
        name = extract_itemprop(soup, "name")
        street_address = extract_itemprop(soup, 'streetAddress')
        postal_code_raw = extract_itemprop(soup, 'postalCode')
        postal_code = ''.join(filter(str.isdigit, postal_code_raw)) if postal_code_raw else None
        address_country = extract_itemprop(soup, 'addressCountry')
        telephone_raw = extract_itemprop(soup, 'telephone')
        telephone = telephone_raw.replace("-", " ") if telephone_raw else None
        fax_number_raw = extract_itemprop(soup, 'faxNumber')
        fax_number = fax_number_raw.replace("-", " ") if fax_number_raw else None
        
        # Extract latitude and longitude from the content attribute
        latitude = extract_itemprop_content(soup, 'latitude')
        longitude = extract_itemprop_content(soup, 'longitude')
        print("Name:", name)
        print("Address:", street_address)
        print("Postal Code:", postal_code)
        print("Country:", address_country)
        print("Telephone:", telephone)
        print("Fax Number:", fax_number)
        print("Latitude:", latitude)
        print("Longitude:", longitude)
        
        # Return the extracted information as a dictionary
        return {
            'URL': url,
            'Name': name,
            'Street Address': street_address,
            'Postal Code': postal_code,
            'Address Country': address_country,
            'Telephone': telephone,
            'Fax Number': fax_number,
            'Latitude': latitude,
            'Longitude': longitude
        }
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

# Prepare to write the data to a new CSV file
output_file = 'extracted_business_data.csv'
fieldnames = ['URL', 'Name', 'Street Address', 'Postal Code', 'Address Country', 'Telephone', 'Fax Number', 'Latitude', 'Longitude']
count = len(urls)

# Open the output CSV file for writing
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Loop over the URLs and extract data
    for url in urls:
        try:
            print("-" * 50)
            data = extract_data(url)
            print("-" * 50)
            print(count, "URLs left")
            if data:
                writer.writerow(data)
        except Exception as e:
            print(f"An exception occurred while processing the URL: {url}. Error: {str(e)}")
            with open('failed.csv', 'a', encoding="utf-8", newline='') as files:
                writer_failed = csv.writer(files)
                writer_failed.writerow([url])
            pass
        count = count - 1
print(f"Data extraction complete. Extracted data saved to {output_file}.")
