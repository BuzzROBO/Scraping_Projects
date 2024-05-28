from urllib.parse import urlparse, parse_qs
import csv

def save_to_csv(links):
    with open('ids.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        for link in links:
            writer.writerow([link])

# Function to read URLs from a CSV file into a list
def read_urls_from_csv(file_name):
    urls = []
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            urls.extend(row)
    return urls

# File name containing the URLs
file_name = "links.csv"
ids=[]
# Call the function to read URLs from the CSV file
urls = read_urls_from_csv(file_name)

for url in urls:
    parsed_url = urlparse(url)
    path_segments = parsed_url.path.split('/')
    code_before_question_mark = path_segments[-2].split('-')[-1]
    code_after_dash = path_segments[-1].split('-')[-1].split('?')[0]
    #print("Code before '?':", code_before_question_mark)
    print("Code after '-':", code_after_dash)
    ids.append(code_after_dash)

with open("ids.csv",mode='a',newline='') as file:
	writer=csv.writer(file)
	for i in ids:
		writer.writerow([i])