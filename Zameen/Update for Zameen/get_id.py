from selenium import webdriver
import urllib.request, json 
from time import sleep
import requests
import json
import urllib.request
import csv
import sys, os
import csv
import os
import pandas as pd
import requests
from pandas.io.json import json_normalize
import ast
import re
header = ["id"]
with open("All_new1.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(header)

df = pd.read_csv('All_new.csv', usecols=['URL'])

for url in zip(df['URL']):
	# print(url)
	urll = url[0]
	ur = urll.split("_")
	urrr = ur[-1]
	print(urrr)
	parts = urrr.split("-")
	numbers = [int(part) for part in parts if part.isdigit()]
	if numbers:
		max_number = max(numbers)
		print("Largest number in '{}': {}".format(urrr, max_number))
	else:
		print("No numerical value found in '{}'".format(urrr))
	with open('All_new1.csv', 'a', encoding="utf-8", newline='') as csv_file:
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow([max_number])	
	# # urr = urrr.split("-")
	# matches = re.findall(r'\d+', str(urrr))
	# if matches:
	#     number = matches[0]
	#     print("Extracted number:", number)
	# else:
	#     print("No numerical value found in the string.")

	
