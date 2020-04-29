import requests
import json
import csv
import time

def  getHtml(url):
	r = requests.get(url, timeout=3.05)
	return r.text

def nameCol():
	with open('Yandex.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow(('Ф.И.О. или название образовательного учреждения.',
						'Описание профиля.',
						'Номер телефона.',
						'Услуга.',
						'Цена за час (в рублях).',
						'Описание услуги.',
						'Город.',
						'Адрес.',
						'Ссылка на профиль.',
						'Ссылка на Вконтакте',
						'Cсылка на Instagram',
						'Ссылка на Facebook',
						'Ссылка на Profi.ru'))

def writeCsv(data):
	with open('Yandex.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow( (data['name'],
						  data['description'],
						  data['number'],
						  data['service'],
						  data['price'], 
						  data['serviceDescription'],
						  data['city'],
						  data['address'],
						  data['url'],
						  data['linkVk'],
						  data['linkInst'],
						  data['linkFacebook'],
						  data['linkProfi']) )

def formattedText(str):
	str = str.split(".")
	lenStr = len(str)
	i = 1
	l = str[0].strip(" ")
	while(i < lenStr):
		if(str[i][0] != " "):
			l = l + str[i]
			continue
		l = l + ".\n"
		l = l + str[i].strip(" ")
		i = i + 1
	return l

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

		card = profile[key]
		cardInformation = card['personalInfo']

		try:
			description = cardInformation['description']
			#description = formattedText(description)

		except KeyError:
			description = ' '

		site = cardInformation['socialLinks']

		try:
			linkVk = site['vk']
			linkInst = site['instagram']
			linkFacebook = site['facebook']
			linkProfi = site['profi']

		except KeyError:
			linkVk = ' '
			linkInst = ' '
			linkFacebook = ' '
			linkProfi = ' '

		name = cardInformation['displayName']
		adr = cardInformation['addressesList']

		try:
			city = adr[0]['cityName']

		except IndexError:
			continue
		except KeyError:
			continue

		try:
			address = adr[0]['address']
			
		except IndexError:
			address = ' '
		except KeyError:
			address = ' '

		urlId = card['seoname']
		url = 'https://yandex.ru/uslugi/profile/' + urlId + '?occupationId=%2Frepetitory-i-obucenie&specId=%2Frepetitory-i-obucenie%2Fanglijskij-azyk&text='
		serviceInformation = card['occupations']
		serviceInformation = serviceInformation[0]['specializations']
		services = serviceInformation[0]['services']
		numberOfServices = len(services)
		i = 0
		while(i != numberOfServices):
			serviceCard = services[i]['attrs']
			if i == 0:
				service = serviceCard['name']
				try:
					price = str(serviceCard['price'])
					serviceDescription = serviceCard['description']
				except KeyError:
					price = ' '
					serviceDescription = ' '
			if i > 0:
				try:
					service = service + '.\n'  + serviceCard['name']
				except KeyError:
					continue	

				try:
					price = price + '\n' + str(serviceCard['price'])
					serviceDescription = serviceDescription + '\n' + serviceCard['description']
				except KeyError:
					price = price + ' '
					serviceDescription = serviceDescription + ' '
			i = i + 1

		data = {'name':name,
				'description':description,
				'number':number,
				'service':service,
				'serviceDescription':serviceDescription,
				'price':price,
				'city':city,
				'address':address,
				'url':url,
				'linkVk':linkVk,
				'linkInst':linkInst,
				'linkFacebook':linkFacebook,
				'linkProfi':linkProfi}
		writeCsv(data)


def main():
	baseUrl = 'https://yandex.ru/uslugi/api/'
	cityPart = '--/'
	queryPart = 'category/repetitoryi-i-obuchenie'
	categoryPart ='--2255??'
	pagePart = 'msp=no&p='
	cityArray = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 
				22, 23, 24, 25, 28, 30, 33, 35, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47,
				48, 49, 50, 51, 53, 54, 55, 56, 57, 58, 62, 63, 64, 65, 66, 67, 68, 74, 75, 
				76, 77, 78, 79, 80]
	nameCol()
	for j in cityArray:
		urlGenBase = baseUrl + str(j) + cityPart + queryPart + categoryPart + pagePart
		i = 0;
		while i < 70:
			url = urlGenBase + str(i)
			print(url)
			html = getHtml(url)
			print(getPageData(html))
			time.sleep(5)
			i = i + 1;
	

if __name__ == '__main__':
	main()