import json
import sqlalchemy as db


class Database():

  def __init__(self):
    self.engine = db.create_engine(self.get_conn_str('../../config.json'))
    self.conn = self.engine.connect()


  def get_conn_str(self, f_path):
    with open(f_path, 'r') as f:
      cfg = json.load(f)
    return 'postgresql://{}:{}@{}/{}'.format(
      cfg['user'], cfg['pwd'], cfg['server'], cfg['db'])

  
  def query(self, sql):
    rows = []
    try:
      rows = self.conn.execute(sql).fetchall()
    except e as Exception:
      print(f'Error occurred executing query:\n  {sql}')
    return rows
