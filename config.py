import string
import random


rand = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(rand) for i in range(12))
SECRET_KEY = key
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql://root:Rentcars@2019@localhost:3306/testeb'
SQLALCHEMY_TRACK_MODIFICATIONS = True
BOTICARIO_ACUMULADO_URI = 'https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback'