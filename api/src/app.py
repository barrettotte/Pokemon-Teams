import json
from database import Database
from flask import Flask

app = Flask(__name__)
db = Database()

@app.route('/')
def hello():
  results = []
  # https://stackabuse.com/using-sqlalchemy-with-flask-and-postgresql/
  for row in db.query('select * from pokemon.pokedex limit 50'):
    results.append({
      'dex_id': row[0],
      'dexno': row[1],
      'name': row[2]
    })
  return {'resp': results}

if __name__ == '__main__': app.run()