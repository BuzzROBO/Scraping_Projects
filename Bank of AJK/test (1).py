from time import sleep
from selenium import webdriver

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.service import Service
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from more_itertools import unique_everseen
import csv
from selenium.webdriver.common.keys import Keys
import sys, os
import traceback
import pandas as pd
chrome_options = Options()
chrome_options.add_argument("--start-maximized")


lat=[]
lon=[]

urls=["https://bankajk.com/bajk-maps/001.php",
"https://bankajk.com/bajk-maps/002.php",
"https://bankajk.com/bajk-maps/003.php",
"https://bankajk.com/bajk-maps/004.php",
"https://bankajk.com/bajk-maps/005.php",
"https://bankajk.com/bajk-maps/006.php",
"https://bankajk.com/bajk-maps/007.php",
"https://bankajk.com/bajk-maps/008.php",
"https://bankajk.com/bajk-maps/009.php",
"https://bankajk.com/bajk-maps/010.php",
"https://bankajk.com/bajk-maps/011.php",
"https://bankajk.com/bajk-maps/012.php",
"https://bankajk.com/bajk-maps/013.php",
"https://bankajk.com/bajk-maps/014.php",
"https://bankajk.com/bajk-maps/015.php",
"https://bankajk.com/bajk-maps/016.php",
"https://bankajk.com/bajk-maps/017.php",
"https://bankajk.com/bajk-maps/018.php",
"https://bankajk.com/bajk-maps/019.php",
"https://bankajk.com/bajk-maps/020.php",
"https://bankajk.com/bajk-maps/021.php",
"https://bankajk.com/bajk-maps/022.php",
"https://bankajk.com/bajk-maps/023.php",
"https://bankajk.com/bajk-maps/024.php",
"https://bankajk.com/bajk-maps/025.php",
"https://bankajk.com/bajk-maps/026.php",
"https://bankajk.com/bajk-maps/027.php",
"https://bankajk.com/bajk-maps/028.php",
"https://bankajk.com/bajk-maps/029.php",
"https://bankajk.com/bajk-maps/030.php",
"https://bankajk.com/bajk-maps/031.php",
"https://bankajk.com/bajk-maps/032.php",
"https://bankajk.com/bajk-maps/033.php",
"https://bankajk.com/bajk-maps/034.php",
"https://bankajk.com/bajk-maps/035.php",
"https://bankajk.com/bajk-maps/036.php",
"https://bankajk.com/bajk-maps/037.php",
"https://bankajk.com/bajk-maps/038.php",
"https://bankajk.com/bajk-maps/039.php",
"https://bankajk.com/bajk-maps/040.php",
"https://bankajk.com/bajk-maps/041.php",
"https://bankajk.com/bajk-maps/042.php",
"https://bankajk.com/bajk-maps/043.php",
"https://bankajk.com/bajk-maps/044.php",
"https://bankajk.com/bajk-maps/045.php",
"https://bankajk.com/bajk-maps/046.php",
"https://bankajk.com/bajk-maps/047.php",
"https://bankajk.com/bajk-maps/048.php",
"https://bankajk.com/bajk-maps/049.php",
"https://bankajk.com/bajk-maps/050.php",
"https://bankajk.com/bajk-maps/051.php",
"https://bankajk.com/bajk-maps/052.php",
"https://bankajk.com/bajk-maps/053.php",
"https://bankajk.com/bajk-maps/054.php",
"https://bankajk.com/bajk-maps/055.php",
"https://bankajk.com/bajk-maps/056.php",
"https://bankajk.com/bajk-maps/057.php",
"https://bankajk.com/bajk-maps/058.php",
"https://bankajk.com/bajk-maps/059.php",
"https://bankajk.com/bajk-maps/060.php",
"https://bankajk.com/bajk-maps/061.php",
"https://bankajk.com/bajk-maps/062.php",
"https://bankajk.com/bajk-maps/063.php",
"https://bankajk.com/bajk-maps/064.php",
"https://bankajk.com/bajk-maps/065.php",
"https://bankajk.com/bajk-maps/066.php"]
driver = webdriver.Firefox(executable_path="geckodriver.exe")

for url in urls:
	driver.get(url)
	print(url)
	sleep(2)

	main=driver.find_element_by_id("main")
	# Find the iframe element
	iframe = driver.find_element_by_tag_name('iframe')
	print()

	# Switch to the iframe
	driver.switch_to.frame(iframe)

	# Execute JavaScript to get the text content of the document
	document_content = driver.find_element_by_css_selector('a[title="Report errors in the road map or imagery to Google"]').get_attribute('href')

	print(document_content)
	location = document_content.split("@")[1].split(",17z")[0]
	data = [url,location]
	print(data)
	with open ("coordinates.csv",   'a',encoding='utf-8', newline='') as files:
		writer = csv.writer(files)
		writer.writerow(data)
		data.clear()