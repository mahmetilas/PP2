import psycopg2

conn = psycopg2.connect(
    dbname="phnbk2026",
    user="postgres",
    password="4376269",
    host="localhost",
    port="5432"
)
cur = conn.cursor()
def upphone(): 
    name = input("Enter name to update phone: ")
    new_phone = input("Enter new phone: ")

    cur.execute(
        "UPDATE numbers SET num = %s WHERE name = %s",
        (new_phone, name)
    )

    conn.commit()

def upname():
    old_name = input("Enter current name: ")
    new_name = input("Enter new name: ")

    cur.execute(
        "UPDATE numbers SET name = %s WHERE name = %s",
        (new_name, old_name)
    )

    conn.commit()
    
x = input("print '1' for updating name '2' for updating phone number: ")

if  x== '1': upname()
elif x=='2': upphone()

cur.close()
conn.close()