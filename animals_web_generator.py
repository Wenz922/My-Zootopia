import json

JSON_FILE = 'animals_data.json'
HTML_FILE = 'animals_template.html'
NEW_HTML_FILE = 'animals.html'


def load_json_data(json_file_path):
    '''Loads a JSON file'''
    with open(json_file_path, 'r') as handle:
        return json.load(handle)


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
    output += '<p class="card__text">'
    output += f'<strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'
    output += f'<strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'
    if animal_obj['characteristics'].get('type'):
        output += f'<strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n'
    output += '</p>'
    output += '</li>'
    return output


def main():
    '''Main function'''
    animals_data = load_json_data(JSON_FILE)
    #print(animals_data)
    html_data = load_html_data(HTML_FILE)
    #print(html_data)

    output = ''     # define an empty string
    for animal in animals_data:
        output += serialize_animal(animal)
    #print(output)

    new_html_data = html_data.replace("__REPLACE_ANIMALS_INFO__", output)
    #print(new_html_data)

    write_html_data(NEW_HTML_FILE, new_html_data)


if __name__ == '__main__':
    main()

