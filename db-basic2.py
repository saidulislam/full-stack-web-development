import psycopg2

connection = psycopg2.connect('dbname=todoapp_development user=sislam password=******')



# Open a cursor to perform database operations
cursor = connection.cursor()

# drop any existing table2 table
cursor.execute('DROP TABLE IF EXISTS table2;')

# (re)create the todos table
# (note: triple quotes allow multiline text in python)
cursor.execute('''
  CREATE TABLE table2 (
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
  );
''')

# this is one way to execute SQL
# cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))

# this is a way to prepare the SQL statement
SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'

# create a dictionary of data to send
data = {
  'id': 1,
  'completed': True
}

# execute the SQL statement
cursor.execute(SQL, data)

# commit, so it does the executions on the db and persists in the db
connection.commit()

connection.close()
cursor.close()