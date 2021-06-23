import yaml

f = open('emp.yml', 'r')

data = yaml.load(f)

for i in data:
    for j in range(len(data[i])):
        print(data[i][j])
