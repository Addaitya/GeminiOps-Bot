import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv('./.env')

def search_wikipedia(search_query: str):
    print('-'*20 + "Action search wikipedia called" + '-'*20)
    url = os.getenv('WIKI_API')

    response = requests.get(
        url,
        params={
            "action": "query",
            "list": "search",
            "srsearch": search_query,
            "format": "json"
        }
    )

    return response.json()['query']['search'][0]['snippet']

def calculate(math_expression: str):
    print('-'*25 + "Action calculate called" + '-'*25)
    print("calculate called")
    return eval(math_expression)

def currency(currency_from:str, currency_to:str, currency_date=None):
    print('-'*25 + "Action currency called" + '-'*25)
    url = os.getenv('CURRENCY_API')
    url = f"{url}/{currency_date}" if currency_date else f'{url}/latest'
    response = requests.get(
        url,
        params={'from':currency_from, 'to': currency_to}
    )

    return response.json()

if __name__=='__main__':
    '''
    If this file executed directly it will run tests to check above fucntions.
    '''
    
    print(f'Search wikipedia: \n{search_wikipedia('What does England share borders with?')}\n')
    print(f"Calculation operation: \n4+5 = {calculate('4+5')}")
    print(f"Currency: {currency('USD', 'INR', '2020-01-01')}")
