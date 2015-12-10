#!/usr/bin/env python                                                                                                                                                                                       
from __future__ import absolute_import, print_function, unicode_literals
import sys
import psycopg2

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("SELECT word, count from Tweetwordcount ORDER BY count DESC LIMIT 20")
records = cur.fetchall()
for rec in records:
	print (rec[0] + ": " + str(rec[1]))

conn.commit()
conn.close()