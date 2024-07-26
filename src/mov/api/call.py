import requests
import os
import pandas as pd
def list2df():
	l = req2list()
	df = pd.DataFrame(l)
	print(df)
	return df
def req2list():
	_, data = req()
#	data.get('').get('')
	l = data['boxOfficeResult']['dailyBoxOfficeList']
	return l
		
def gen_url(dt="20120101"):
	base_url="http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
	key="e1ac8e397edce73a571ba078b2d4db58"
	url=f"{base_url}?key={key}&targetDt={dt}"
	key = get_key()
	return url

def req(dt="20120101"):
	url = gen_url()
	r = requests.get(url)
	data = r.json()
	stat_code = r.status_code	
	print(stat_code, data)
	return stat_code,data

def get_key():
	key = os.getenv("MOVIE_API_KEY")
	return key
