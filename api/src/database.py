import pyodbc

class Database():

  def __init__(self, conn_str):
    self.conn_str = conn_str
    self.conn = pyodbc.connect(conn_str)
  
  def query(self, sql):
    rows = []
    try:
      rows = self.conn.execute(sql).fetchall()
    except e as Exception:
      print(f'Error occurred executing query:\n  {sql}')
    return rows
