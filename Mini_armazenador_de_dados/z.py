import sqlite3 as sq

banco= sq.connect('primeiro_banco.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text,idade integer,email text)")

""" pessoa= input('qual seu nome')
idade = int(input('qual sua idade'))
gmail = input('qual seu gmail')

cursor.execute("INSERT INTO pessoas VALUES(?,?,?)",(pessoa,idade,gmail))
 """
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())
banco.commit()