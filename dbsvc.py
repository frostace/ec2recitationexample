import pymysql
import json

c_info = {
        "host": "ec2simplerdb.ckkqqktwkcji.us-east-1.rds.amazonaws.com",
        "user": "dbuser",
        "password": "dbuserdbuser",
        "cursorclass": pymysql.cursors.DictCursor,
    }

conn = pymysql.connect(**c_info)
cur = conn.cursor()
res = cur.execute("show databases;")
res = cur.fetchall()

print("databases = ", json.dumps(res, indent=4, default=str))
