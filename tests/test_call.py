from mov.api.call import gen_url, req, get_key, req2list, list2df, save2df
import pandas as pd

def test_save2df():
	df = save2df()
	assert isinstance(df, pd.DataFrame)
	assert 'rnum' in df.columns
	assert 'openDt' in df.columns
	assert 'movieNm' in df.columns
	assert 'audiAcc' in df.columns
	assert 'load_dt' in df.columns

def test_gen_url():
	url = gen_url()
	assert True
	assert "http" in url

def test_req():
	stat_code, data = req("19700101")
	assert stat_code == 200

def test_key():
	key = get_key()
	assert key

def test_req2list():
	l = req2list()
	assert len(l) > 0
	assert 'rnum' in l[0].keys()

def test_list2df():
	df = list2df()
	print(df)
	assert isinstance(df, pd.DataFrame)
	assert 'rnum' in df.columns
	assert 'openDt' in df.columns
	assert 'movieNm' in df.columns
	assert 'audiAcc' in df.columns
