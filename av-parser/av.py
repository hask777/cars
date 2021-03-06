import requests
from bs4 import BeautifulSoup
import json
# import brands


base_url = 'https://cars.av.by/'

carslinks = {} 

finalcars = []

for x in range(1,5):

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

    r = requests.get(f'https://cars.av.by/filter?brands[0][brand]=1444&price_currency=2&page={x}')

    soup = BeautifulSoup(r.content, 'html.parser')
    carslist = soup.find_all('div', class_='listing-item')

    

    for item in carslist:

        ''' Find car image '''
        photo = item.find('div', class_='listing-item__photo')
        image = photo.find('img')['data-src']

        ''' Find car title '''
        title = item.find('span', class_='link-text').text

        ''' Find car link '''
        params = item.find('div', class_='listing-item__params').text

        ''' Find car link '''
        link = item.find('a', href=True)['href']

        ''' Find car price '''
        price_ru = item.find('div', class_='listing-item__price').text

        ''' Find car price by usd '''
        price_usd = item.find('div', class_='listing-item__priceusd').text
        price_usd = price_usd.replace('≈', ' ')
        price_usd = price_usd.replace('$', ' ').strip()
        price_usd = price_usd.split()
        for x in price_usd:
            x = int(x)

        price_usd = price_usd[0]+price_usd[1]
        
    
        carslinks = {
            'image': image,
            'title': title,
            'params': params,
            'link': link,
            'price_ru': price_ru,
            'price_usd': price_usd
        }

        finalcars.append(carslinks)

# print(len(finalcars))


cars = "cars.json"
with open(cars, 'w', encoding='utf-8') as json_file:
    json.dump(finalcars, json_file, ensure_ascii = False, indent =4)


print('file dumped')
    

# def convert(string: str) -> int:
#     for base in range(0, 36):
#         try:
#             if str(int(string, base)) == string:
#                 return int(string, base)
#                 break
#         except ValueError:
#             pass
#         finally:
#             pass

# print(convert(price_usd))   