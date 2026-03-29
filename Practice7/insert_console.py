import psycopg2

conn = psycopg2.connect(
    dbname="phnbk2026",
    user="postgres",
    password="4376269",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

name = input("Enter name: ")
phone = input("Enter phone: ")

cur.execute(
    "INSERT INTO numbers (name, num) VALUES (%s, %s)",
    (name, phone)
)
conn.commit()

cur.close()
conn.close()