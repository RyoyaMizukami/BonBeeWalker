#using: utf-8
# 色々引っ張ってきたり、定義したり
from flask import Flask, render_template, session, redirect, url_for, escape, request
import psycopg2
import psycopg2.extras
import os
import random, string

app = Flask(__name__)
# ↓はGoogle Maps APIのAPIキーを定義してます。APIキーというのは鍵です。
API_key = os.environ.get('gmap_API')

# データベースに接続する関数です。
def get_connection():
    dsn = os.environ.get('DATABASE_URL')
    return psycopg2.connect(dsn)



# 最初にアクセスされるページ
@app.route('/')
def index():
    IsIDPassValue = False
    return render_template('index2.html', IsIDPassValue = IsIDPassValue)

# 登録ページの表示
@app.route('/register', methods=['POST'])
def register():
    identity = request.form['identity']
    return render_template('commons/register.html', identity = identity, API_key = API_key)

# 検索の過程
@app.route('/result', methods=['POST'])
def post():
    IsIDPassValue = False

    budget = request.form['budget']
    type = request.form['type']
    print(budget)
    print(type)
    if not type and not budget:
        IsIDPassValue = True
        return render_template('index2.html', IsIDPassValue = IsIDPassValue)

    cur = get_connection().cursor()

    if type and not budget:
        cur.execute("SELECT type,money,place,random_address FROM zgundam WHERE type LIKE %s AND displayable = 't' ORDER BY money ASC", (type,))
        data = cur.fetchall()
        cur.close()
        get_connection().close()
    elif budget and not type:
        cur.execute("SELECT type,money,place,random_address FROM zgundam WHERE money <= %s AND displayable = 't' ORDER BY money DESC", (budget,))
        data = cur.fetchall()
        cur.close()
        get_connection().close()
    else:
        cur.execute("SELECT type,money,place,random_address FROM zgundam WHERE money <= %s AND type LIKE %s AND displayable = 't' ORDER BY money DESC", (budget,type))
        data = cur.fetchall()
        cur.close()
        get_connection().close()

    return render_template('commons/result2.html', budget = budget, type = type, data = data, len = len(data))

def random_address_generator(n):
    rand_list = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
    return ''.join(rand_list)

# 投稿の過程
@app.route('/register_post', methods=['POST'])
def registing():
    type = request.form['type']
    money = request.form['money']
    #placeID = request.form['placeID']
    place = request.form['place']
    cando = request.form['cando']
    identity = request.form['identity']

    if type and money and place and cando:
        print(type, money, place, cando)
        IsValue = False

        random_address = random_address_generator(16)
        displayable = True

        conn = get_connection()
        cur = conn.cursor()
        cur.execute('SELECT max(id) from zgundam;')
        id = cur.fetchone()[0]
        print(id)
        id += 1
        print(id)
        cur.execute('INSERT INTO zgundam(id, type, money, place, cando,random_address, identity, displayable) VALUES(%s, %s, %s, %s, %s, %s, %s, %s);', (id, type, money, place, cando, random_address, identity, displayable))
        cur.close()
        conn.commit()
        conn.close()

        IsRegistration = True

        return render_template('index2.html', IsValue = IsValue, IsRegistration = IsRegistration)
    else:
        IsValue = True
        return render_template('commons/register.html', IsValue = IsValue, API_key = API_key, identity = identity)

# 各URL用の概要ページ
@app.route('/result/<name>')
def detail(name):
    cur = get_connection().cursor()
    cur.execute('SELECT place,cando FROM zgundam WHERE random_address LIKE %s;', (name,))
    value = cur.fetchone()
    cur.close()
    get_connection().close()
    return render_template('commons/detail_template.html',value = value,random_address = name)

# ログインの過程
@app.route('/login', methods=['POST'])
def login():
    identity = request.form['identity']
    password = request.form['password']

    print(identity)
    print(password)

    # そもそもフォームに文字を入れたかどうか
    if not identity or not password:
        IsIDPassValue = True
        return render_template('index2.html', IsIDPassValue = IsIDPassValue)

    else:
        # ucgundamから一致するか検索する
        cur = get_connection().cursor()
        cur.execute('SELECT identity FROM ucgundam WHERE identity LIKE %s', (identity,))
        auth_id = cur.fetchone()
        cur.execute('SELECT password FROM ucgundam WHERE identity LIKE %s AND password LIKE %s', (identity,password))
        auth_pw = cur.fetchone()
        cur.close()
        get_connection().close()

        if not auth_id and not auth_pw:
            conn = get_connection()
            cur = conn.cursor()
            data = []
            NiceToMeetYou = True
            cur.execute('INSERT INTO ucgundam(identity, password) VALUES(%s, %s);', (identity, password))
            print(identity,password)
            cur.close()
            conn.commit()
            conn.close()

            return render_template('commons/mypage2.html', data = data, identity = identity, NiceToMeetYou = NiceToMeetYou)

        elif auth_id and auth_pw:
            NiceToMeetYou = False
            cur = get_connection().cursor(cursor_factory=psycopg2.extras.DictCursor)
            cur.execute("SELECT id,type,money,place,cando,displayable FROM zgundam WHERE identity LIKE %s AND displayable = 't' ORDER BY id DESC;", (identity,))
            data = cur.fetchall()
            cur.close()
            get_connection().close()
            print(data, auth_id, auth_pw)
            return render_template('commons/mypage2.html', data = data, identity = identity, NiceToMeetYou = NiceToMeetYou)

        else:
            IsIDPassInvalid = True
            IsIDPassValue = False
            return render_template('index2.html', IsIDPassValue = IsIDPassValue, IsIDPassInvalid = IsIDPassInvalid)

@app.route('/delete', methods=['POST'])
def delete():
    id = request.form['delete_id']
    conn = get_connection()
    cur = conn.cursor()
    f = 'false'
    cur.execute("UPDATE zgundam SET displayable = %s WHERE id = %s;", (f, id))
    cur.close()
    conn.commit()
    conn.close()

    return render_template('index2.html')

# おまじない。これがないとHerokuで動かない。
if __name__ == "__main__":
    app.run()
