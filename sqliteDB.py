import sqlite3

class SQLiteDB(object):
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
    
    def create_table(self, create_table_sql):
        try:
            self.c.execute(create_table_sql)
        except sqlite3.Error as e:
            print(e)
    
    def insert_data(self, insert_sql, data):
        try:
            self.c.executemany(insert_sql, data)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
    
    def fetch_all(self, select_sql):
        try:
            self.c.execute(select_sql)
            return self.c.fetchall()
        except sqlite3.Error as e:
            print(e)
            return []
    
    def close(self):
        if self.conn:
            self.conn.close()
