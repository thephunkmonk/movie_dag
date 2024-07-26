from src.mov.api.call import gen_url, req, get_key, req2dataframe

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

def test_req2df():
	l = req2dataframe()
	assert len(l) > 0
	assert 'rnum' in l[0].keys()
