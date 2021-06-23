import json

# covert dict to json string
person_dict = {
    'name': 'Bob',
    'age': 12,
    'children': None
}

print(person_dict, type(person_dict))
person_json = json.dumps(person_dict)

print(person_json, type(person_json))
