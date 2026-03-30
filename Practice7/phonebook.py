import psycopg2, csv
from config import load_config

def by_name(cur):
    name = input("Enter name to search: ")

    cur.execute(
        "SELECT * FROM numbers WHERE name = %s",
        (name,)
    )

    print(cur.fetchall())

def byphone(cur):
    prefix = input("Enter phone prefix: ")

    cur.execute(
        "SELECT * FROM numbers WHERE num LIKE %s",
        (prefix + "%",)
    )

    print(cur.fetchall())

def insert_csv(cur):
    f_name = input("csv file name: ").strip()

    with open(f"{f_name}", newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            cur.execute(
                "INSERT INTO numbers (name, num) VALUES (%s, %s)",
                (row[0], row[1])
            )

def insert_con(cur):
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    cur.execute(
        "INSERT INTO numbers (name, num) VALUES (%s, %s)",
        (name, phone)
    )

def delete(cur):
    phone = input("Enter phone to delete: ")

    cur.execute(
        "DELETE FROM numbers WHERE num = %s",
        (phone,)
    )

def upphone(cur): 
    name = input("Enter name to update phone: ")
    new_phone = input("Enter new phone: ")

    cur.execute(
        "UPDATE numbers SET num = %s WHERE name = %s",
        (new_phone, name)
    )


def upname(cur):
    old_name = input("Enter current name: ")
    new_name = input("Enter new name: ")

    cur.execute(
        "UPDATE numbers SET name = %s WHERE name = %s",
        (new_name, old_name)
    )

def showall(cur):
    cur = conn.cursor()

    cur.execute("SELECT * FROM numbers")
    print(cur.fetchall())
# ===============================================================
if __name__ == '__main__':
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                x = input('Type: \n'
                '"1" to search: \n'
                '"2" to insert:\n'
                '"3" to delete:\n'
                '"4" to update:\n'
                '"5" to see all:\n').strip()
                if x=='1':
                    x = input('Type "1" to search by name\n"2" to search by phone number:\n').strip()
                    if x=='1': by_name(cur)
                    elif x=='2': byphone(cur)
                elif x=='2':
                    x = input('Type "1" to insert by csv file\n"2" to insert mannually:\n').strip()
                    if x=='1': insert_csv(cur)
                    elif x=='2': insert_con(cur)
                elif x == '3': delete(cur)
                elif x=='4':
                    x = input('Type "1" to update name\n"2" to update phone number:\n').strip()
                    if x=='1': upname(cur)
                    elif x=='2': upphone(cur)
                elif x=='5': showall(cur)
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)