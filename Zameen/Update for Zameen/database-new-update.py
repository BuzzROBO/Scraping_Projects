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
from datetime import date
from datetime import datetime
from dbConfiguration import DbConfig
import ast
from time import strftime, localtime
db = DbConfig('172.16.130.23','TPLMaps',5432,'qgis.plugin','assigncity')
conn = db.ConnectDb()
# query = "select id from web_portal.zameen_price where area is not null and title is null"
# data = db.DbResultsQuery(query)
# print('db ', query)
# result = data
# print(len(result))
# sleep(10)
count = 0
df = pd.read_csv('All_new1.csv', usecols=['id'])
for uu in zip(df['id']):
	print(uu[0])
	idd = uu[0]
	count = count+1
	print(count)
	print('*'*200,count)
	print(idd)
	url = f'https://www.zameen.com/api/listing/?external_id={idd}'
	print(url)
	try:
		sleep(2)
		r = requests.get(url, timeout=20)
		print(r.status_code)
		if r.status_code==200:
			res = r.text
			res2 = json.loads(res)
			try:
				cat = res2['category']
				purr = []
				for ca in cat:
					purr.append(ca['name'])
				print(purr)
				pp = ' '.join(purr)
			except:
				pp = 'None'		
			poo = res2['purpose']
			price = res2['price']
			title = res2['title']
			loc_lat = res2['geography']['lat']
			loc_lng = res2['geography']['lng']
			area = res2['area']
			approv = res2['approvedAt']
			apppp = strftime('%Y-%m-%d %H:%M:%S', localtime(approv))
			title = title.replace("'","")
			title = title.replace('"','')
			pp = pp.replace("'","")
			pp = pp.replace('"','')
			
			print(pp,poo,price,title,loc_lat,loc_lng,area,apppp)

			
			try:
				db.DbModifyQuery("""insert into zameen_price (id,lat,long,property_type,purpose,avg_price,area,title,approved_date) values ({0},'{1}','{2}','{3}','{4}',{5},{6},'{7}','{8}')""".format(idd,loc_lat,loc_lng,pp,poo,price,area,title,apppp))
			except Exception as e:
				exc_type, exc_obj, exc_tb = sys.exc_info()
				fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
				print(exc_type, fname, exc_tb.tb_lineno)
				with open('last1.csv', 'a', encoding="utf-8", newline='') as csv_file:
					csv_writer = csv.writer(csv_file)
					csv_writer.writerow([idd])
	except Exception as e:
		print("eeeeeeeeeee",e)
		with open('last1.csv', 'a', encoding="utf-8", newline='') as csv_file:
			csv_writer = csv.writer(csv_file)
			csv_writer.writerow([idd])
		pass			


