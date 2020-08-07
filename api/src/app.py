from database import Database
from flask import Flask, request, jsonify

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
  return {'data': None, 'error': f"error in request: {err}"}, 500


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


@app.route('/api/v1/sprites/<dexno>', methods=['GET'])
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


@app.route('/api/v1/teams', methods=['GET'])
def get_teams():
  try:
    teams = db.query('select * from pokemon.team')
    return query_resp([{'id': x[0], 'name': x[1]} for x in teams])
  except Exception as e:
    return error_resp(e)


@app.route('/api/v1/teams/<team_id>', methods=['GET'])
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


@app.route('/api/v1/teams', methods=['POST'])
def create_team():
  try:
    data = dict(request.json)
    team_id = db.bound_stmt(' '.join((
      'insert into pokemon.team (label)',
      'values (?)',
      'returning team_id'
    )), [data['label']] )[0]
    data['team_id'] = team_id

    for idx,mbr in enumerate(data['members']):
      mbr_id = db.bound_stmt(' '.join((
        'insert into pokemon.member (team_id, dex_id, sprite_id, gender, level, nickname, slot, shiny)',
        'values (?,?,?,?,?,?,?,?)',
        'returning member_id'
      )), [
        team_id, mbr['dex_id'], mbr['sprite_id'], mbr['gender'], 
        mbr['level'], mbr['nickname'], mbr['slot'], '1' if mbr['shiny'] else '0'
      ])[0]
      data['members'][idx]['member_id'] = mbr_id
    return data, 201
  except Exception as e:
    return error_resp(e)


@app.route('/api/v1/teams/<team_id>', methods=['PUT'])
def update_team(team_id):
  # TODO:
  try:
    data = request.json
    print(data)
    return 'epic', 201

  except Exception as e:
    return error_resp(e)


@app.route('/api/v1/teams/<team_id>', methods=['DELETE'])
def delete_team(team_id):
  try:
    db.bound_stmt('delete from pokemon.member where team_id = ?', [team_id])
    db.bound_stmt('delete from pokemon.team where team_id = ?', [team_id])
    return '', 204
  except Exception as e:
    return error_resp(e)


if __name__ == '__main__': app.run(debug=True)