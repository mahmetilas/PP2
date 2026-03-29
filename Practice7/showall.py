import psycopg2

conn = psycopg2.connect(
    dbname="phnbk2026",
    user="postgres",
    password="4376269",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("SELECT * FROM numbers")
print(cur.fetchall())

cur.close()
conn.close()