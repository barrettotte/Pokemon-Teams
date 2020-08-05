import json
from database import Database
from flask import Flask, request

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object('config.Config')
db = Database(app.config['DATABASE_URI'])


def query_resp(data):
  if isinstance(data, list) and len(data) == 0:
    return {'data': [], 'error': 'no records found'}, 400
  return {'data': data, 'error': None}, 200


def error_resp(err):
  # yeah yeah yeah, I know. Its terrible to return raw error messages from an API.
  return {'data': None, 'error': f"error in request: {e}"}, 500


@app.route('/api/v1/')
def api_index():
  return 'Pokemon-Teams API v1'


@app.route('/api/v1/pokedex', methods=['GET'])
def get_pokedex():
  try:
    entries = db.query('select dexno,name from pokemon.pokedex')
    return query_resp([{'dexno': x[0], 'name': x[1]} for x in entries])
  except Exception as e:
    return error_resp(e)


@app.route('/api/v1/sprite/<dexno>', methods=['GET'])
def get_sprites(dexno):
  try:
    sprites = db.bound_query(' '.join((
      'select a.dexno, b.slug, b.has_female',
      'from pokemon.pokedex a', 
      'join pokemon.sprite b on a.dex_id=b.dex_id',
      'where a.dexno = ?' 
    )), [dexno])
    return query_resp([{'dexno': x[0], 'slug': x[1], 'has_female': x[2] == '1'} for x in sprites])
  except Exception as e:
    return error_resp(e)


@app.route('/api/v1/team', methods=['GET'])
def get_teams():
  try:
    teams = db.query('select * from pokemon.team')
    return query_resp([{'id': x[0], 'name': x[1]} for x in teams])
  except Exception as e:
    return error_resp(e)


@app.route('/api/v1/team/<team_id>', methods=['GET'])
def get_team(team_id):
  try:
    teams = db.bound_query('select * from pokemon.team where team_id = ? limit 1', [team_id])
    if len(teams) == 0:
      return {'data': [], 'error': 'no records found'}, 400

    team = {'team_id': teams[0][0], 'label': teams[0][1], 'members': []}
    members = db.bound_query('select * from pokemon.member where team_id = ? limit 6', [team['team_id']])
    for mbr in members:
      team['members'].append({
        'member_id': mbr[0], 'dex_id': mbr[1], 'sprite_id': mbr[2], 
        'gender': mbr[3], 'level': mbr[4], 'nickname': mbr[5], 'shiny': mbr[6] == "1"
      })
    return {'data': team, 'error': None}, 200
  except Exception as e:
    return error_resp(e)


@app.route('/api/v1/team/<team_id>', methods=['POST'])
def create_team(team_id):
  return 'TODO:'


@app.route('/api/v1/team/<team_id>', methods=['PUT'])
def update_team(team_id):
  return 'TODO:'


@app.route('/api/v1/team/<team_id>', methods=['DELETE'])
def delete_team(team_id):
  try:
    db.bound_stmt('delete from pokemon.member where team_id = ?', [team_id])
    db.bound_stmt('delete from pokemon.team where team_id = ?', [team_id])
  except Exception as e:
    return error_resp(e)


if __name__ == '__main__': app.run(debug=True)