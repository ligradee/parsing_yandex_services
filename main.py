import requests
import json
import csv
import time
import parsing_yandex


if __name__ == '__main__':
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
