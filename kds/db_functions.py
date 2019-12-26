import psycopg2


def insert_value(name, form):
    conn = psycopg2.connect(
        host="localhost", database="postgres", user="ml", password="docker"
    )
    cur = conn.cursor()
    print("Inserting values")
    into = ""
    values = ""
    for index, field in enumerate(form):
        if field.name not in ["csrf_token", "submit"] and field.data not in ["", None]:
            separator = ", " if index is not 0 else ""
            into += separator
            into += field.name
            values += separator
            values += "'" + str(field.data) + "'"

    sql = "INSERT INTO {} ({}) VALUES ({});".format(name, into, values)
    print(sql)
    cur.execute(sql)
    conn.commit()
    conn.close()


def select_from(name):
    conn = psycopg2.connect(
        host="localhost", database="postgres", user="ml", password="docker"
    )
    cur = conn.cursor()
    print("Selecting values")
    sql = "SELECT * FROM {};".format(name)
    print(sql)
    cur.execute(sql)
    records = cur.fetchall()
    conn.close()
    return records
