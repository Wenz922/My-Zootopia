import requests
import os
from dotenv import load_dotenv

load_dotenv()

# API Ninja
API_KEY = os.getenv('API_KEY')
#print(API_KEY)
HEADERS = {'X-Api-Key': API_KEY}
REQUEST_URL = 'https://api.api-ninjas.com/v1/animals'


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
        ...
        },
    '   locations': [
        ...
        ],
        'characteristics': {
         ...
        }
     },
    """
    params = {'name': animal_name}
    res = requests.get(REQUEST_URL, headers=HEADERS, params=params)
    if res.status_code != 200:
        raise Exception(f'{res.status_code}: {res.text}')
    return res.json()