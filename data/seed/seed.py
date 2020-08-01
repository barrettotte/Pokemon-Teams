# seed postgres database with pokedex to make searching super easy

import requests, json, time


def get_entries():
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


def main():
  entries = get_entries()
  with open('./data.json', 'w+') as f:
    f.write(json.dumps(entries, indent=2))


if __name__ == "__main__": main()