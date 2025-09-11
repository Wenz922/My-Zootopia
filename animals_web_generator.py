import json
import requests

JSON_FILE = 'animals_data.json'
HTML_FILE = 'animals_template.html'
NEW_HTML_FILE = 'animals.html'

# API Ninja
HEADERS = {'X-Api-Key': 'HY98B+WTrLJwUlITv0hsBw==3Bh3GFG3n8jxIE9f'}
REQUEST_URL = 'https://api.api-ninjas.com/v1/animals'


def load_json_data(json_file_path):
    '''Loads a JSON file'''
    with open(json_file_path, 'r') as handle:
        return json.load(handle)


def get_animals_data(animal_name):
    '''Fetch the animal data from a API'''
    params = {'name': animal_name}
    res = requests.get(REQUEST_URL, headers=HEADERS, params=params)
    if res.status_code != 200:
        raise Exception(f'Error fetching animals data, {res.status_code}, {res.text}')
    return res.json()


def load_html_data(html_file_path):
    '''Loads a HTML file'''
    with open(html_file_path, 'r') as handle:
        return handle.read()


def write_html_data(new_file_path, data):
    '''Writes a HTML file'''
    with open(new_file_path, 'w') as new_file:
        new_file.write(data)


def serialize_animal(animal_obj):
    '''Serializes an animal html object'''
    output = ''
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    output += '<div class="card__text">'
    output += '<ul>'
    output += f'<li><strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}</li>\n'
    output += f'<li><strong>Location:</strong> {animal_obj["locations"][0]}</li>\n'
    if animal_obj['characteristics'].get('type'):
        output += f'<li><strong>Type:</strong> {animal_obj["characteristics"]["type"]}</li>\n'
    output += '</ul>'
    output += '</div>'
    output += '</li>'
    return output


def skin_type(animal_obj):
    '''Prints animal skin types'''
    skin_types = set()
    for animal in animal_obj:
        skin_type = animal["characteristics"].get("skin_type")
        if skin_type:
            skin_types.add(skin_type)
    print("Available animal skin types: ")
    for ani_skin in skin_types:
        print('-', ani_skin)


def main():
    '''Main function'''
    # animals_data = load_json_data(JSON_FILE)  # Get animal data from given file
    # print(animals_data)

    # Open html template file
    html_data = load_html_data(HTML_FILE)

    # Get animal data from API
    animal_name = input('Enter a name of an animal: ')
    animals_data = get_animals_data(animal_name)
    if animals_data:

        """# Display animal skin types
        skin_type(animals_data)
        # User choose a animal skin type
        user_selected = input(f"Enter an animal's skin type from the above list: ").strip()
        filtered_animals = [animal for animal in animals_data
                            if animal["characteristics"].get("skin_type") == user_selected]"""

        output = ''     # define an empty string
        for animal in animals_data:
            output += serialize_animal(animal)
    else:
        output = f'<h2>The animal "{animal_name}" does not exist.</h2>'

    new_html_data = html_data.replace("__REPLACE_ANIMALS_INFO__", output)
    #print(new_html_data)

    write_html_data(NEW_HTML_FILE, new_html_data)
    print("Website was successfully generated to the file animals.html.")


if __name__ == '__main__':
    main()

