# seed postgres database with pokedex to make searching super easy

import requests, json, time
import pyodbc  

# seed with pokeapi - Not going to use this I don't think -> missing gen 8 and alt forms.
def get_from_pokeapi():
  limit = 100
  offset = 0
  url = 'https://pokeapi.co/api/v2/pokemon?limit={}&offset={}'
  headers = {'Content-Type': 'application/json'}
  
  count = 807 # max API dexno
  resp = requests.get(url.format(100, 0)).json()
  entries = resp['results']

  for i in range(2, (count // 100) + 1):
    if ((i+1) * 100) > count:
      limit = count % i
    time.sleep(0.5)
    resp = requests.get(url.format(limit, offset + (i * 100))).json()
    entries.extend(resp['results'])
  return entries


# Using pokemon.json from https://raw.githubusercontent.com/msikma/pokesprite/master/data/pokemon.json
def get_from_pokesprite():
  entries = []

  with open('./pokemon.json', 'r') as f:
    for k,v in json.loads(f.read()).items():
      entry = {'dexno': k, 'name': v['name']['eng'], 'slug': v['slug']['eng'], 'forms': []}
  
      # get gender specific forms
      for fk,fv in v['gen-8']['forms'].items():
        entry['forms'].append({'form': fk, 'has_female': 'has_female' in fv})

      entries.append(entry)
  return entries


def get_conn_str(f_path):
  # simple Postgres config file
  with open(f_path, 'r') as f:
    config = json.load(f)
  return ''.join([
    'DRIVER={PostgreSQL Unicode};',
    'DATABASE={};'.format(config['db']),
    'UID={};'.format(config['user']),
    'PWD={};'.format(config['pwd']),
    'SERVER={};'.format(config['server']),
    'PORT={}'.format(config['port'])
  ])
  

def main():
  entries = get_from_pokesprite()
  with open('./seed.json', 'w+') as f:
    f.write(json.dumps(entries, indent=2))

  cs = get_conn_str('./seed-config.json')

  conn = pyodbc.connect(cs)
  conn.setencoding(encoding='utf-8') # Postgres uses UTF-8

  cursor = conn.execute("select * from wakatime_stats limit 25")
  for row in cursor.fetchall():
    print(row)
  
  cursor.close()
  conn.close()


if __name__ == "__main__": main()