import requests


def  get_html(url):
	r = requests.get(url)
	return r.text

def main():
	url = "https://yandex.ru/uslugi/api/1--/category/repetitoryi-i-obuchenie--2255??msp=no&p=0"

if __name__ == '__main__':
	main()