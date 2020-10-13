import pymysql
import json
import os

# print("Environment = ", os.environ)

pw = os.environ['dbpw']

print("Environment = ", os.environ['dbpw'])

c_info = {
        "host": "ec2simpledb.c5juyujlj64h.us-east-1.rds.amazonaws.com",
        "user": "dbuser",
        "password": pw,
        "cursorclass": pymysql.cursors.DictCursor,
    }

conn = pymysql.connect(**c_info)
cur = conn.cursor()
res = cur.execute("show databases;")
res = cur.fetchall()

print("databases = ", json.dumps(res, indent=4, default=str))
