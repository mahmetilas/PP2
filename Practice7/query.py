import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="phnbk2026",
    user="postgres",
    password="4376269",
    port=5432,
)
cur = conn.cursor()

def by_name():
    name = input("Enter name to search: ")

    cur.execute(
        "SELECT * FROM numbers WHERE name = %s",
        (name,)
    )

    print(cur.fetchall())

def byphone():
    prefix = input("Enter phone prefix: ")

    cur.execute(
        "SELECT * FROM numbers WHERE num LIKE %s",
        (prefix + "%",)
    )

    print(cur.fetchall())
x = input("print '1' for searching by name '2' for searching by phone number: ")

if  x== '1': by_name()
elif x=='2': byphone()

conn.commit()

cur.close()
conn.close()