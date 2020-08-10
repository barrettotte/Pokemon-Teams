# one-off script to seed database with pokedex entries and sprite references

import json, pyodbc


# Using pokemon.json from https://raw.githubusercontent.com/msikma/pokesprite/master/data/pokemon.json
def get_from_pokesprite():
  entries = []

  with open('./pokemon.json', 'r') as f:
    for k,v in json.loads(f.read()).items():
      entry = {'dexno': k, 'name': v['name']['eng'], 'sprites': []}

      for fk,fv in v['gen-8']['forms'].items():
        entry['sprites'].append({
          'form': fk,
          'has_female': '1' if 'has_female' in fv else '0',
          'slug': v['slug']['eng']
        })
      entries.append(entry)
  return entries


def get_conn_str(f_path):
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


# there's no way this is efficient at all...
  # I'm sure there is a genius way to do this, but I'm not worried about it.
def seed_db(conn, entries):
  for entry in entries:
    print('seeding #{}'.format(entry['dexno']))

    # insert dex record
    cursor = conn.execute(
      'insert into pokemon.pokedex(dexno,name) values(?,?)', 
      entry['dexno'], entry['name'])

    # get FK for sprite table
    cursor = conn.execute('select dex_id from pokemon.pokedex where dexno=? limit 1', entry['dexno'])
    dex_fk = cursor.fetchone()[0]

    # insert sprite records
    for sp in entry['sprites']:

      # adjust sprite slug for alt. form
      slug = sp['slug'] if sp['form'] == '$' else sp['slug'] + '-' + sp['form']

      cursor = conn.execute(
        'insert into pokemon.sprite(dex_id, form, has_female, slug) values(?,?,?,?)',
        dex_fk, sp['form'], sp['has_female'], slug)

    cursor.close()
    conn.commit()
  

def main():
  entries = get_from_pokesprite()
  
  with open('./seed.json', 'w+') as f:
    f.write(json.dumps(entries, indent=2))

  conn = pyodbc.connect(get_conn_str('dbconfig.json'))
  cursor = conn.execute('select count(*) from pokemon.pokedex')
  do_seed = cursor.fetchone()[0] == 0
  cursor.close()

  if do_seed:
    print('seeding {} entries!'.format(len(entries)))
    seed_db(conn, entries) # seeded 1398 sprites, 893 pokemon
  else:
    print('already seeded.')

  print('done!')
  conn.close()

if __name__ == "__main__": main()