import sqlite3 as sq

banco= sq.connect('primeiro_banco.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE pessoas (nome text,idade integer,email text)")

banco.commit()


