import requests
from bs4 import BeautifulSoup
import json

base_url = 'https://av.by/'

headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

r = requests.get(base_url)

soup = BeautifulSoup(r.content, 'html.parser')
brandlist = soup.find('ul', class_='brandslist')

brands = {}

for brand in brandlist:
    
    try:
        name = brand.find('span').text
    except:
        name = brand.find('span')

    try:
        cars_count = brand.find('small').text
    except:
        cars_count = brand.find('small')

    print(cars_count)

    barnds = {
        'name': name,
        'cars_count': cars_count
    }

    print(barnds)
