import traceback, argparse, requests, shutil
import pandas as pd
import random
import json

from bs4 import BeautifulSoup


class Scraper(object):

    def collect(self):

        try:
            _response = self.send_request('https://www.dafiti.com.br/calcados/')

            _soup = self.to_soup(_response.text)
            _page_count = 1
            _infos = []

            for i in range(5):

                print('page: {}'.format(i))
                _infos_products = self.collect_products(_soup)
                _infos = _infos + _infos_products
                _next_link = _soup.find('li', {'class': 'page next'}).a

                if _next_link:
                    _response = self.send_request('https://www.dafiti.com.br/{}'.format(_next_link.attrs.get('href')))
                    _soup = self.to_soup(_response.text)
                else:
                    break;

            pd.DataFrame(_infos).to_csv('calcados.csv', sep=';', index=False)

        except Exception as ex:
            traceback.print_exc()
    
    def collect_products(self, soup):
        try:

            _links = soup.find_all('a', {'class': 'product-box-link'})
            _infos = []
            for link in _links:
                if link.attrs.get('href'):
                    _info = self.collect_product(link.attrs.get('href'))
                    _infos.append(_info)

            return _infos
        except Exception as ex:
            traceback.print_exc()
            raise ex

    def collect_product(self, link):
        try:

            _response = self.send_request(link)
            _soup = self.to_soup(_response.text)
            sku = None
            name = _soup.find('h1', {'class': 'product-name'}).text 
            price = _soup.find('span', {'class': 'catalog-detail-price-value'}).text
            price = price.strip().split('R$')[1].strip().replace(',', '.')
            details = _soup.find('p', {'class': 'product-information-description'}).text.replace('\r', '').replace('\n', '')
            tags  = list(map(lambda item: item.a.text if item.a else None, _soup.find_all('div', {'class': 'box-see-more-content'})))
            information_table = _soup.find('table', {'class': 'product-informations'})
            information = {}
            # sizes = list(map(lambda item: 
            #     {'size': item.text, 'available_quantity':random.randint(0, 10)},
            #          _soup.find_all('span', {'class': 'selectbox-option-name'})))

            sizes = [{
                'size': random.randint(34, 42),
                'available_quantity': random.randint(1, 15)
            } for i in range(3)]

            for item in information_table.tbody.select('tr'):
                tds = item.select('td')
                if tds[0].text == 'SKU':
                    sku = tds[1].text
                else:
                    information[tds[0].text] = tds[1].text.replace('\r', '').replace('\n', '')

            return {
                'sku': sku,
                'name': name,
                'price': price,
                'price': price,
                'details': details,
                'tags': tags,
                'informations': json.dumps(information),
                'promotion': random.randint(0, 60),
                'sizes': json.dumps(sizes)
            }

        except Exception as ex:
            traceback.print_exc()
            return {}
    
    def to_soup(self, text):
        try:
            return BeautifulSoup(text, 'html.parser')
        except Exception as ex:
            traceback.print_exc()
            raise ex

    def send_request(self, url, stream=False): 

        try:

            _session = requests.Session()

            _headers = {
                'User-Agent': 'My User Agent 1.0',
                'From': 'youremail@domain.com'
            }

            _response = _session.get(url, headers=_headers, stream=stream)

            if _response.status_code > 400:
                raise

            return _response

        except Exception as ex:
            print('Erro na request da url {}'.format(url))
            return None

if __name__ == '__main__':
    _crawler = Scraper()
    _crawler.collect()