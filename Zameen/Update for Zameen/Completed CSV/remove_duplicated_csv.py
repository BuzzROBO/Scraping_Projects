import csv

# Open the CSV file
with open('All_links.csv', 'r') as file:
    reader = csv.reader(file)
    # Assuming the URLs are in the first column
    urls = set(row[0] for row in reader)

# Now urls contains unique URLs
print(urls)
print(len(urls))