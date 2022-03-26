# parse JSON into a Python dictionary

import json

#  Sample JSON
userJSON = '{"first_name": "Mahady", "last_name": "Hasan", "age": 35}'
print(userJSON)

# Parse to dict
user = json.loads(userJSON)
# print(user)
# print(user['first_name'])

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(car)
print(carJSON)