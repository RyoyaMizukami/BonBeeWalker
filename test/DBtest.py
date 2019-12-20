import psycopg2
connection = psycopg2.connect(host = "localhost", database = "bonbee_db", user = "ryoya", password = "zzzxxx0822")

cur = connection.cursor()
cur.execute('SELECT * FROM gundam')
data = cur.fetchone()
cur.close()
connection.close()

print(data)
