import json
from database import Database
from flask import Flask

app = Flask(__name__)
app.config.from_object('config.Config')
db = Database(app.config['DATABASE_URI'])

@app.route('/api/v1/')
def index():
  results = []
  for row in db.query('select * from pokemon.pokedex limit 50'):
    results.append({'dex_id': row[0], 'dexno': row[1], 'name': row[2]})
  return {'resp': results}
  # return 'Pokemon-Teams API v1'

if __name__ == '__main__': app.run(debug=True)