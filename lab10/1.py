import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="PhoneBook",
    user="aiazhkkaa"  ,
    password="12345"
)

cur = conn.cursor()
cur.execute("SELECT * FROM contacts")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()