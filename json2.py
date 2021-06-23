# coverts string json to dict

import json

a = '{"name":"Bob","langauges":"English"}'

y = json.loads(a)

print(y)

print(type(y))
