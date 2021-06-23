# loads json file in to the dictionary
import json

with open('data.json') as f:
    data = json.load(f)

for i in data.keys():
    for j in range(len(data[i])):
        print(data[i][j])

for i in data['emp_details']:
    print(i)
