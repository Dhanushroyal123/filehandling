

file = open('text.txt', 'r')


print(id(file))

print(file.read(10))

print(file.readline())
print(file.readline())
print(file.readline())

for i in file.readlines():
    print(i)

file.close()
