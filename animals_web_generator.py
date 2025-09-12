
from data_fetcher import fetch_data


HTML_FILE = 'animals_template.html'
NEW_HTML_FILE = 'animals.html'


def load_html_data(html_file_path):
    """Loads a HTML file"""
    with open(html_file_path, 'r') as handle:
        return handle.read()


def write_html_data(new_file_path, data):
    """Writes a HTML file"""
    with open(new_file_path, 'w') as new_file:
        new_file.write(data)


def serialize_animal(animal_obj):
    """Serializes an animal html object"""
    output = ''
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{animal_obj.get("name")}</div>\n'
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


def main():
    """Main function"""
    # Open html template file
    html_data = load_html_data(HTML_FILE)

    # Get animal data from API
    animal_name = input('Please enter an animal: ')
    try:
        animals_data = fetch_data(animal_name)
    except Exception as e:
        print('Error fetching animals data from API.', e)
        return

    if animals_data:
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

