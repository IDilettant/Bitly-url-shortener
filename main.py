import argparse
import os
from urllib.parse import urlparse, urlunparse

import requests
from dotenv import load_dotenv


def get_bitlink(long_url, headers):
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    payload = {'long_url': '{}'.format(long_url)}
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()['id']


def get_count_clics(bitlink, headers):
    bitlink = urlparse(bitlink)._replace(scheme='')
    bitlink = urlunparse(bitlink)
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{0}/clicks/summary'.format(bitlink)
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(url, headers):
    url = urlparse(url)._replace(scheme='')
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{0}'.format(urlunparse(url))
    response = requests.get(url, headers=headers)
    return response.ok


def create_url_parser():
    description = 'Accepts a link as input and converts it into a bitlink.\n' \
                  'If a bitlink is entered, it returns the total number of clicks on it.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('urls', nargs='+', help='link address')
    return parser    
    

def main():
    load_dotenv()
    token = os.getenv('BITLINK_TOKEN')
    headers = {'Authorization': 'Bearer {0}'.format(token)}
    parser = create_url_parser()
    args = parser.parse_args()
    for url in args.urls:
        if is_bitlink(url, headers):
            try:
                print(get_count_clics(url, headers))
            except requests.exceptions.HTTPError:
                print('Wrong bitlink. Please, try another!')
        else:
            try:
                print(get_bitlink(url, headers))
            except requests.exceptions.HTTPError:
                print('Wrong link. Please, try another!')


if __name__ == '__main__':
    main()
