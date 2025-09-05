import json

JSON_FILE = 'animals_data.json'
HTML_FILE = 'animals_template.html'


def load_data(file_path):
    '''Loads a JSON file'''
    with open(file_path, 'r') as handle:
        return json.load(handle)


animals_data = load_data(JSON_FILE)
with open(HTML_FILE, 'r') as file:
    html_data = file.read()
#print(html_data)

output = ''     # define an empty string
for animal in animals_data:
    # append information to each string
    output += '<li class="cards__item">'
    output += f"Name: {animal['name']}<br/>\n"
    output += f"Diet: {animal['characteristics']['diet']}<br/>\n"
    output += f"Location: {animal['locations'][0]}<br/>\n"
    if animal['characteristics'].get('type'):
        output += f"Type: {animal['characteristics']['type']}<br/>\n"
    output += '</li>'
#print(output)

new_html_data = html_data.replace("__REPLACE_ANIMALS_INFO__", output)
#print(new_html_data)

with open('animals.html', 'w') as file:
    file.write(new_html_data)
