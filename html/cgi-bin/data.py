#!/usr/bin/python
#Import libraries needed
import sqlite3
import sys
import json

#Connect to the database
con = sqlite3.connect('../../log/room.db')
cur = con.cursor()

print("Content-type:text/json;charset=utf-8\n")
con.row_factory = sqlite3.Row
cur.execute("SELECT * FROM (SELECT * FROM room ORDER BY time DESC LIMIT 10) ORDER BY time ASC;")
dataset = cur.fetchall()
chartJSON = []
for row in dataset:
	chartJSON.append({"time": row[0], "state": row[1],"people": float(row[2])})
print(json.dumps(chartJSON))
con.close()
exit(0)
