def req(dt="20120101"):
	base_url="http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
	key="e1ac8e397edce73a571ba078b2d4db58"

	url=f"{base_url}?key={key}&targetDt={dt}"
	print(url)
	
req()
	
