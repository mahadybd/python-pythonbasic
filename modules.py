#Core modules
# import datetime
# from datetime import date
# import time
# from time import time

# # today = datetime.date.today()
# today = date.today()
# timestamp = time()

# print(timestamp)

#pip module
from camelcase import CamelCase

#import custom module
import validator
from validator import validate_email

c = CamelCase()
print(c.hump('Hello from camelcase module'))


email = 'test@test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is bad')