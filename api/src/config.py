import os

def get_conn_str():
  return ''.join([
    'DRIVER={PostgreSQL Unicode};',
    'DATABASE={};'.format(os.getenv('DB_NAME')),
    'UID={};'.format(os.getenv('DB_USER')),
    'PWD={};'.format(os.getenv('DB_PWD')),
    'SERVER={};'.format(os.getenv('DB_SERVER')),
    'PORT={}'.format(os.getenv('DB_PORT'))
  ])

class Config(object):
  DATABASE_URI = get_conn_str()
  API_PORT = os.getenv('API_PORT')