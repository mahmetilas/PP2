import psycopg2

conn = psycopg2.connect(
    dbname="phnbk2026",
    user="postgres",
    password="4376269",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

phone = input("Enter phone to delete: ")

cur.execute(
    "DELETE FROM phonebook WHERE phone = %s",
    (phone,)
)

conn.commit()

cur.close()
conn.close()