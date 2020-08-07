import pyodbc

class Database():

  def __init__(self, conn_str):
    self.conn_str = conn_str
    self.conn = pyodbc.connect(conn_str)
  
  def query(self, sql):
    return self.conn.execute(sql).fetchall()

  def bound_query(self, sql, params):
    return self.conn.execute(sql, params).fetchall()

  def bound_stmt(self, sql, params):
    cursor = self.conn.cursor()
    try:
      cursor.execute(sql, params)
      data = cursor.fetchone()
    except Exception:
      data = None
    cursor.commit()
    return data
