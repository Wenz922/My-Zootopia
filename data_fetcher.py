import requests

# API Ninja
HEADERS = {'X-Api-Key': 'HY98B+WTrLJwUlITv0hsBw==3Bh3GFG3n8jxIE9f'}
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
        raise Exception(f'Error fetching animals data, {res.status_code}, {res.text}')
    return res.json()