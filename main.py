import requests
import json

def  get_html(url):
	r = requests.get(url)
	return r.text

def get_page_data(html):
	page = json.loads(html)

def main():
	url = "https://yandex.ru/uslugi/api/1--/category/repetitoryi-i-obuchenie--2255??msp=no&p=0"
	html = get_html(url)
	print(get_page_data(html))

if __name__ == '__main__':
	main()