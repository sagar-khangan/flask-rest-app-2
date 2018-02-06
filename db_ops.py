import psycopg2

def connect(config):
    try:
        conn = psycopg2.connect(database=config.get('db', 'database'), user=config.get('db', 'user'),
                                password=config.get('db', 'password'), host=config.get('db', 'host'),
                                port=config.get('db', 'port'))
        create_db(conn)
        return conn
    except Exception as e:
        print "unable to connect to the database", e
        return "error"

def create_db(conn):
    cur = conn.cursor()
    cur.execute("create table if not exists contacts(id serial primary key , name  VARCHAR (50) not null, email VARCHAR (50) not null , phone VARCHAR (10))  ")
    conn.commit()

def fetch_data(conn):
    cur = conn.cursor()
    cur.execute("select * from contacts")
    return cur.fetchall()

def insert_data(conn,request):
    cur = conn.cursor()
    try:
        cur.execute("""insert into contacts(name,email,phone) values(%s,%s,%s)""",(request.form['name'],request.form['email'],request.form['phone']))
        conn.commit()
        return {'message':cur.statusmessage}
    except Exception as e:
        print e
        return {'message':'error in insertion'}


def delete_data(conn,request):

    cur = conn.cursor()
    try:
        cur.execute("""delete from contacts where name = '{0}' """.format(request.form['name']))
        conn.commit()
        return {'message':cur.statusmessage}
    except Exception as e:
        print e
        return {'message':'error in deletion'}


def update_data(conn,request):
    cur = conn.cursor()
    try:
        cur.execute("""update contacts set email =   '{0}', phone  = '{1}' where name = '{2}'  """.format(
            request.form['email'],request.form['phone'],request.form['name']))
        conn.commit()
        return {'message':cur.statusmessage}
    except Exception as e:
        print e
        return {'message':'error in updation'},