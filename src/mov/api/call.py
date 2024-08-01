import requests
import os
import pandas as pd



def apply_type2df(load_dt='20120101', path="~/tmp/test_parquet"):
	df = pd.read_parquet(f'{path}/load_dt={load_dt}')
	
	num_cols = ['rnum', 'rank', 'rankInten', 'salesAmt', 'audiCnt', 'audiAcc', 'scrnCnt', 'showCnt', 'salesShare','salesInten','salesChange','audiInten','audiChange']
	
	for col in num_cols:
		df[col] = pd.to_numeric(df[col])

#	df['rnum']=pd.to_numeric(df['rnum'])
#	df['scrnCnt']=pd.to_numeric(df['scrnCnt'])
#	df['showCnt']=pd.to_numeric(df['showCnt'])
#	df['rank']=pd.to_numeric(df['rank'])
	return df

def save2df(load_dt='20120101', url_param={}):
	df = list2df(load_dt, url_param)
	# add load_dt column with format YYYYMMDD
	# and partition by load_dt when saving to parquet
	df['load_dt'] = load_dt
	print(df.head(5))
#	df.to_parquet(f'~/data/parquet/load_dt={dt}/parquet.parquet', partition_cols=['load_dt'])
	
	df.to_parquet(f'~/tmp/test_parquet', partition_cols=['load_dt'])
	return df


def list2df(load_dt='20120101', url_param = {}):
	l = req2list(load_dt, url_param)
	df = pd.DataFrame(l)
	print(df)
	return df
def req2list(load_dt='20120101', url_param = {}):
	_, data = req()
#	data.get('').get('')
	l = data['boxOfficeResult']['dailyBoxOfficeList']
	return l
		
def gen_url(dt="20120101", url_param={'multiMovieYn':'N'}):
	base_url="http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
	key="e1ac8e397edce73a571ba078b2d4db58"
	url=f"{base_url}?key={key}&targetDt={dt}" 
	
	for k, v in url_param.items():
		url = url + f"&{k}={v}"
	key = get_key()
	return url

def req(load_dt="20120101", url_param={}):
	url = gen_url(load_dt, url_param)
	r = requests.get(url)
	data = r.json()
	stat_code = r.status_code	
	print(stat_code, data)
	return stat_code,data

def get_key():
	key = os.getenv("MOVIE_API_KEY")
	return key
