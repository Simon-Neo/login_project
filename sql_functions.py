import sqlite3

class sql_info():
    def __init__(self, address_db, str_create_table):
        self.conn = sqlite3.connect(address_db)
        self.cur = self.conn.cursor()

        try:
            self.cur.execute(str_create_table)
        except Exception as ex:
            print(f'occur error = {ex}')

    def add_to_sql_table(self, list_data, sql_shape):
        for dic_info in list_data:
            list_values = list(dic_info.values())
            print(list_values)
            self.cur.execute(sql_shape, list_values)

    def exit_sql(self):
        self.conn.commit()
        self.conn.close()