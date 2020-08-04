import json
from pathlib import Path

def get_conn_str(file_name):
  with open(Path.joinpath(Path(__file__).resolve().parents[2], file_name), 'r') as f:
    cfg = json.load(f)
  return ''.join([
    'DRIVER={PostgreSQL Unicode};',
    'DATABASE={};'.format(cfg['db']),
    'UID={};'.format(cfg['user']),
    'PWD={};'.format(cfg['pwd']),
    'SERVER={};'.format(cfg['server']),
    'PORT={}'.format(cfg['port'])
  ])

class Config(object):
  DATABASE_URI = get_conn_str('config.json')
  SPRITE_BASE = 'https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8'
