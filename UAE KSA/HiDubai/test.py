import csv
import re

# Function to extract categories from URLs
def extract_categories(urls):
    categories = []
    for url in urls:
        match = re.search(r'/category/([^/]+)/', url)
        if match:
            category = match.group(1)
            categories.append(category)
    return categories

# Read URLs from CSV
def read_urls_from_csv(filename):
    urls = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            urls.append(row['url'])
    return urls

# Write categories to CSV
def write_categories_to_csv(categories, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['categories'])
        for category in categories:
            writer.writerow([category])

# Main function
def main():
    # Read URLs from CSV
    filename = 'links.csv'  # Assuming the CSV file is named "links.csv"
    urls = read_urls_from_csv(filename)

    # Extract categories
    categories = extract_categories(urls)

    # Write categories to CSV
    output_filename = 'categories.csv'  # Output CSV file name
    write_categories_to_csv(categories, output_filename)

if __name__ == "__main__":
    main()
