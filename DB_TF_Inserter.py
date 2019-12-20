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
    cur.execute('SELECT id, displayable FROM zgundam;')
    data = cur.fetchall()
    print(data)

    if len(data) != 0:
        for row in data:
            print(row[0])
            t = 'true'
            if row[1] == None:
                id = row[0]
                cur.execute("UPDATE zgundam SET displayable = %s WHERE id = %s;", (t, id))
                conn.commit()
                print('Insert complete.')

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
