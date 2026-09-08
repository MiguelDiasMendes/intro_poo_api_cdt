import sqlite3

conn = sqlite3.connect("alls-tools.db")
cursor = conn.cursor()


cursor.execute(
    '''
    CREATE TABLE  IF NOT EXISTS tasks (
        id  INTEGRAL PRIMARY KEY AUTOINCREMENT,
        task_name TEXT NOT NULL,
        data_fish NUMBER NOT NULL,
        data_star NUMBER NOT NULL,
        tarefa_about  STRING NOT NULL)
'''
)

conn.commit
