import psycopg2
import os
import random, string

def get_connection():
    dsn = os.environ.get('DATABASE_URL')
    return psycopg2.connect(dsn)

def random_address_generator(n):
    rand_list = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
    return ''.join(rand_list)

def inserter():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, random_address FROM zgundam;')
    data = cur.fetchall()
    print(data)

    if len(data) != 0:
        for row in data:
            print(row[0])
            if row[1] == None:
                id = row[0]
                random_strings = random_address_generator(16)
                print(random_strings)
                cur.execute("UPDATE zgundam SET random_address = %s WHERE id = %s;", (random_strings, id))
                conn.commit()
                print('Insert complete. Strings is ' + random_strings + '!')

            else:
                print('Error! DB_Inserter could not detect enpty row!')

        cur.close()
        conn.close()
        return print('FINISHED!')

    else:
        cur.close()
        get_connection().close()
        return print('Error! This table does not have a row!')

if __name__ == "__main__":
    inserter()
