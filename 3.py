
import os

# os.remove('text.txt')

if os.path.exists('text.txt'):
    os.remove('text.txt')
    print('successfully deleted')
else:
    print('file not exist')
