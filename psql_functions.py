import psycopg2
import sys
import os

# conf = {
#       "host" : os.environ['DB_HOST'],
#       "database" : os.environ['DB_NAME'],
#       "user" : os.environ['DB_USER'],
#       "password" : os.environ['DB_PASS'],
#       "port" : os.environ['DB_PORT']
# }

conf = {
    "database" : "mailer",
    "user" : "postgres",
    "password" : "Pass2020!",
    "host" : "172.16.38.15", 
    "port" : "5432"
}


# Conversation Table
def Insert(data):
    conn = psycopg2.connect(database=conf["database"], user = conf["user"], password = conf["password"], host = conf["host"], port = conf["port"])
    cur = conn.cursor()

    fullname = data['fullname']
    companyid = data['companyid']
    
    cur.execute("INSERT INTO main_users (full_name, companyid) VALUES (%s, %s);", (fullname, companyid))

    conn.commit()
    print("Records created successfully")
    conn.close()


def Select_All():
    conn = psycopg2.connect(database=conf["database"], user = conf["user"], password = conf["password"], host = conf["host"], port = conf["port"])
    cur = conn.cursor()

    cur.execute("SELECT ID, full_name, companyid from main_users")
    rows = cur.fetchall()
    # for row in rows:
    #     print(row[0], row[1], row[2])
    print("Operation done successfully")
    conn.close()

    return rows


def Select_One(_id):
    conn = psycopg2.connect(database=conf["database"], user = conf["user"], password = conf["password"], host = conf["host"], port = conf["port"])
    cur = conn.cursor()

    cur.execute("SELECT ID, full_name, companyid from main_users WHERE ID = %s;", [_id])
    row = cur.fetchone()
    # print(row)
    print("Operation done successfully")
    conn.close()

    return row


def Select_One_By_Statement(statement):
    conn = psycopg2.connect(database=conf["database"], user = conf["user"], password = conf["password"], host = conf["host"], port = conf["port"])
    cur = conn.cursor()

    cur.execute("SELECT * from conversation WHERE statement = %s;", [statement])
    row = cur.fetchone()
    # print(row)
    print("Operation done successfully")
    conn.close()

    return row


def Update(_id, response):
    conn = psycopg2.connect(database=conf["database"], user = conf["user"], password = conf["password"], host = conf["host"], port = conf["port"])
    cur = conn.cursor()

    cur.execute("UPDATE conversation set response = %s where ID = %s;", (response, _id))
    conn.commit()
    print("Total number of rows updated: ", cur.rowcount)
    conn.close()


def Delete_One(_id):
    conn = psycopg2.connect(database=conf["database"], user = conf["user"], password = conf["password"], host = conf["host"], port = conf["port"])
    cur = conn.cursor()

    cur.execute("DELETE from main_users where ID = %s;", [_id])
    conn.commit()
    print("User  deleted :", cur.rowcount)
    conn.close()


def Delete_All():
    conn = psycopg2.connect(database=conf["database"], user = conf["user"], password = conf["password"], host = conf["host"], port = conf["port"])
    cur = conn.cursor()

    cur.execute("DELETE from conversation where ID > 0;")
    conn.commit()
    print("Total number of rows deleted :", cur.rowcount)
    conn.close()






# Users Table
def Select_All_Users():
    conn = psycopg2.connect(database=conf["database"], user = conf["user"], password = conf["password"], host = conf["host"], port = conf["port"])
    cur = conn.cursor()

    cur.execute("SELECT * from fb_users")
    rows = cur.fetchall()
    # for row in rows:
    #     print(row[0], row[1], row[2])
    print("Operation done successfully")
    conn.close()

    return rows


def Select_One_User(fb_id):
    conn = psycopg2.connect(database=conf["database"], user = conf["user"], password = conf["password"], host = conf["host"], port = conf["port"])
    cur = conn.cursor()

    cur.execute("SELECT * from fb_users WHERE fb_id = %s;", [fb_id])
    row = cur.fetchone()
    # print(row)
    print("Operation done successfully")
    conn.close()

    return row


def Insert_User(data):
    conn = psycopg2.connect(database=conf["database"], user = conf["user"], password = conf["password"], host = conf["host"], port = conf["port"])
    cur = conn.cursor()

    first_name = data['first_name']
    last_name = data['last_name']
    profile_pic = data['profile_pic']
    fb_id = data['id']

    cur.execute("INSERT INTO fb_users (first_name, last_name, profile_pic, fb_id) VALUES (%s, %s, %s, %s);", (first_name, last_name, profile_pic, fb_id))

    conn.commit()
    print("Records created successfully")
    conn.close()






