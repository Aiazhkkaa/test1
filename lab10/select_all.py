import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="lab10",
    user="aiazhanshormano"

)
cur = conn.cursor()

cur.execute("SELECT * FROM phonebook")
rows = cur.fetchall()

print("Контакты:")
for row in rows:
    print(f"ID: {row[0]}, Имя: {row[1]}, Номер: {row[2]}")

cur.close()
conn.close()
