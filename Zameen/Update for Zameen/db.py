from selenium import webdriver
import urllib.request, json 
from time import sleep
import requests
import json
import urllib.request
from pandas.io.json import json_normalize
import csv
import os
import pandas as pd
import requests
from pandas.io.json import json_normalize
from datetime import date
from datetime import datetime

import pandas as pd
import csv
import os
import psycopg2
from datetime import datetime
import re
import pandas as pd
import csv
import os
import psycopg2
from datetime import datetime
import re
import requests
from time import sleep
from dbConfiguration import DbConfig


db = DbConfig('172.16.44.80','TPLMaps',5432,'qgis.plugin','assigncity')

conn = db.ConnectDb()


#query = "select * from google_pois_v1 where qa_status in('new_true_phase_9','new_phase_2_true','true_phase_10_3_july')"
query = "select * from google_pois_v1 where qa_status = 'true_11_12_2023'"
# print('db ', query)

data = db.DbResultsQuery(query)
# print('db ', query)
result = data
print(result)
print(len(result))
sleep(5)
for res in result:
	print("res", res)
	name = res[3]
	num =  res[0]
	print(num)
	print(name)
	r = requests.get('http://172.16.103.221:8066/subcatpredictor?name={0}'.format(name))

	res = r.text
	res1 = json.loads(res)
	# print(type(res1))
	# print(res1)
	sub = res1['Subcategory']
	cat = res1['Category']
	print(sub, cat)

	resp = db.DbModifyQuery("""update google_pois_v1 set tpl_cat = '{0}' , tpl_subcat = '{1}' where id = {2}""".format(cat, sub, num))
	


