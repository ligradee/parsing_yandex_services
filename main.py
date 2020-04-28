import requests
import json

def  getHtml(url):
	r = requests.get(url)
	return r.text

def getPageData(html):
	page = json.loads(html)
	profile = page['workers']
	profile = profile['items']
	cookies = dict(cookies_are='_ym_uid=1562097438760144276; mda=0; fuid01=5d75497528442b76.WJLTwvcBzZPTVSJ81bIDjeXCWAJixGiDH_d_6tyuGIBUM9S_jkvg-nqQDYcNbJH5jB9D9wbAsdajBshn6vcnh8J4Cd2kPUCm4-_neodGg1BTna5iQA2bVBlozVs8uWtG; yandexuid=1186228981561890726; yuidss=1186228981561890726; i=22ZIqAQDyOvlZtJR8D2WIaQCTWi4f4oND2SwA6wwo0McrgNhsMT01PtLfLLhyXHRaeAcdWNpybPd5YX3daNCm9GiiOk=; gdpr=0; ymex=1576788978.oyu.7287139971574196678#1877250726.yrts.1561890726#1889556979.yrtsi.1574196979; bltsr=1; ys=svt.1#ymrefl.16F8A028192B2E42#wprid.1582836800884344-973866089991090189700067-vla1-1314; yp=1877250726.yrts.1561890726#1889556979.yrtsi.1574196979#1587766494.ygu.1; yandex_gid=2; _ym_d=1585174495; sMLIIeQQeFnYt=1; font_loaded=YSv1; zm=m-white_bender.gen.webp.css-https%3As3home-static_JXvDB1rLJQhLQ7sfFw1WzdqarbM%3Al; yabs-frequency=/4/0000000000000000/wrImS6Gw8DhqSd1aEYS0/; yc=1585433696.zen.cach%3A1585178094; skid=7538336611585253025; ar=1586204800329223-744546; _ym_isad=1; _ym_visorc_49540177=b')
	for key in profile:
		ip = key
	params = '{"data":{"params":{"id":"'+ ip + '"}}}'
	try:
		number = requests.post('https://yandex.ru/uslugi/api/get_worker_phone?ajax=1', params, cookies=cookies)
		number = number.text.split('{')[2].split('"')[3]
	except IndexError:
		continue

def main():
	url = "https://yandex.ru/uslugi/api/1--/category/repetitoryi-i-obuchenie--2255??msp=no&p=0"
	html = get_html(url)
	print(get_page_data(html))
	

if __name__ == '__main__':
	main()