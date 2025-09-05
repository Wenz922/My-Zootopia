import json

JSON_FILE = 'animals_data.json'


def load_data(JSON_FILE):
    '''Loads a JSON file'''
    with open(JSON_FILE, 'r') as handle:
        return json.load(handle)


animals_data = load_data(JSON_FILE)
"""print(type(animals_data))
print(type(animals_data[0]))
print(animals_data[0].keys())
print(type(animals_data[0]['name']))
print(animals_data[0]['taxonomy'].keys())
print(type(animals_data[0]['locations']))
print(animals_data[0]['characteristics'].keys())"""

for animal in animals_data:
    print(f"Name: {animal['name']}")
    print(f"Diet: {animal['characteristics']['diet']}")
    print(f"Location: {animal['locations'][0]}")
    if animal['characteristics'].get('type'):
        print(f"Type: {animal['characteristics']['type']}")
    print()
