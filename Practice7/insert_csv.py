import psycopg2, csv

conn = psycopg2.connect(
    dbname="phnbk2026",
    user="postgres",
    password="4376269",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

f_name = input("csv file name: ").strip()

with open(f"{f_name}", newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        cur.execute(
            "INSERT INTO numbers (name, num) VALUES (%s, %s)",
            (row[0], row[1])
        )

conn.commit()

cur.close()
conn.close()