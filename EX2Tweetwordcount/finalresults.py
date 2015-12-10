#!/usr/bin/env python                                                                                                                                                                                       
from __future__ import absolute_import, print_function, unicode_literals
import sys
import psycopg2

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

if sys.argv[1] is None:
	#Case where we print out all the words in the stream and their total count of occurrences, sorted alphabetically in an ascending order, one word per line                                           
    cur.execute("SELECT word, count from Tweetwordcount ORDER BY word ASC")
    records = cur.fetchall()
    for rec in records:
	   print ("word = ", rec[0])
	   print ("count = ", rec[1], "\n")
else:
    #Case where we print number of occurrences of sys.argv[1]
    cur.execute("SELECT word, count from Tweetwordcount WHERE word == \'%s\'", sys.argv[1])
    records = cur.fetchall()
    for rec in records:
       print ("Total number of occurrences of \"%s\": %s", (rec[0], rec[1]), "\n")
conn.commit()
conn.close()
