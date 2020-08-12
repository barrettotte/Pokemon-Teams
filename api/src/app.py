# This API is junk, but it'll work for this project.

from database import Database
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object('config.Config')
db = Database(app.config['DATABASE_URI'])
cors = CORS(app)


def query_resp(data):
  if isinstance(data, list) and len(data) == 0:
    return {'data': [], 'error': 'no records found'}, 404
  return {'data': data, 'error': None}, 200


def error_resp(err):
  # yeah yeah yeah, I know. Its terrible to return raw error messages from an API.
  return {'data': None, 'error': f"error in request: {err}"}, 500


def validate_request(data, required):
  missing = []
  for k in required:
    if not k in data:
      missing.append(f"'{k}'")
  return None if len(missing) > 0 else 'Bad request: Missing key(s) [' + ','.join(missing) + ']'


def team_exists(team_id):
  return len(db.bound_query('select team_id from pokemon.team where team_id=? limit 1', [team_id])) == 1

def team_not_found(team_id):
  return f"Could not find team with team_id='{team_id}'", 404

def member_exists(member_id):
  return len(db.bound_query('select member_id from pokemon.member where member_id=? limit 1', [member_id])) == 1

def member_not_found(member_id):
  return f"Could not find member with member_id='{member_id}'", 404


@app.route('/api/v1/')
def api_index():
  return 'Pokemon-Teams API v1'


@app.route('/api/v1/pokedex', methods=['GET'])
def get_pokedex():
  try:
    entries = db.query(' '.join((
      'select a.dexno, a.name, b.slug',
      'from pokemon.pokedex a',
      'join pokemon.sprite b on a.dex_id=b.dex_id',
      "  and b.form='$'"
    )));
    return query_resp([{'dexno': x[0], 'name': x[1], 'slug': x[2]} for x in entries])
  except Exception as e:
    return error_resp(e)


@app.route('/api/v1/pokedex/<dex_id>/sprites/', methods=['GET'])
def get_dex_sprites(dex_id):
  try:
    sprites = db.bound_query(' '.join((
      'select b.dexno, a.slug, a.has_female',
      'from pokemon.sprite a',
      'join pokemon.pokedex b on a.dex_id=b.dex_id',
      'where a.dex_id = ?'
    )), [dex_id])
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


@app.route('/api/v1/teams/random', methods=['GET'])
def get_random_team():
  try:
    team = db.query(' '.join([
      'select team_id',
      'from pokemon.team',
      'offset floor(random() * (select count(*) from pokemon.team))'
      'limit 1'
    ]))[0]
    return query_resp({'id': team[0]})
  except Exception as e:
    return error_resp(e)


@app.route('/api/v1/teams/<team_id>', methods=['GET'])
def get_team(team_id):
  try:
    teams = db.bound_query('select * from pokemon.team where team_id = ? limit 1', [team_id])
    if len(team) == 0:
      return team_not_found(team_id)

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
    return data, 201
  except Exception as e:
    return error_resp(e)


@app.route('/api/v1/teams/<team_id>', methods=['PUT'])
def update_team(team_id):
  try:
    if not team_exists(team_id):
      return team_not_found(team_id)

    data = dict(request.json)
    db.bound_stmt(' '.join((
      'update pokemon.team set label=?',
      'where team_id=?',
    )), [data['label'], team_id])

    return data, 200
  except Exception as e:
    return error_resp(e)


@app.route('/api/v1/teams/<team_id>', methods=['DELETE'])
def delete_team(team_id):
  try:
    db.bound_stmt('delete from pokemon.member where team_id = ?', [team_id])
    db.bound_stmt('delete from pokemon.team where team_id = ?', [team_id])
    return '', 200
  except Exception as e:
    return error_resp(e)


@app.route('/api/v1/teams/<team_id>/members/<member_id>', methods=['GET'])
def get_member(team_id, member_id):
  try:
    if not team_exists(team_id):
      return team_not_found(team_id)

    q = db.bound_query('select * from pokemon.member where member_id = ? limit 1', [member_id])
    if len(q) == 0:
      return member_not_found(member_id)

    mbr = q[0]
    data = {
      'member_id': mbr[0], 'dex_id': mbr[1], 'sprite_id': mbr[2], 
      'gender': mbr[3], 'level': mbr[4], 'nickname': mbr[5], 'shiny': mbr[6] == "1"
    }
    return data, 200
  except Exception as e:
    return error_resp(e)


@app.route('/api/v1/teams/<team_id>/members/', methods=['POST'])
def create_member(team_id):
  try:
    if not team_exists(team_id):
      return team_not_found(team_id)

    data = dict(request.json)
    mbr_id = db.bound_stmt(' '.join((
      'insert into pokemon.member (team_id, dex_id, sprite_id, gender, level, nickname, slot, shiny)',
      'values (?,?,?,?,?,?,?,?)',
      'returning member_id'
    )), [
      team_id, data['dex_id'], data['sprite_id'], data['gender'], 
      data['level'], data['nickname'], data['slot'], '1' if data['shiny'] else '0'
    ])[0]
    data['member_id'] = mbr_id
    return data, 201
  except Exception as e:
    return error_resp(e)


@app.route('/api/v1/teams/<team_id>/members/<member_id>', methods=['PUT'])
def update_member(team_id, member_id):
  try:
    if not team_exists(team_id):
      return team_not_found(team_id)
    if not member_exists(member_id):
      return member_not_found(member_id)

    data = dict(request.json)
    db.bound_stmt(' '.join((
      'update pokemon.member set dex_id=?, sprite_id=?, slot=?, gender=?, level=?, nickname=?, shiny=?',
      'where team_id=? and member_id=?',
    )), [
      data['dex_id'], data['sprite_id'], data['slot'], data['gender'], 
      data['level'], data['nickname'], '1' if data['shiny'] else '0', 
      team_id, member_id
    ])
    return data, 200
  except Exception as e:
    return error_resp(e)


@app.route('/api/v1/teams/<team_id>/members/<member_id>', methods=['DELETE'])
def delete_member(team_id, member_id):
  try:
    db.bound_stmt('delete from pokemon.member where member_id = ?', [member_id])
    return '', 200
  except Exception as e:
    return error_resp(e)


if __name__ == '__main__': app.run(debug=True, host='0.0.0.0', port=5000)