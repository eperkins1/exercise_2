#!/usr/bin/env python                                                                                                                                                                                       
from __future__ import absolute_import, print_function, unicode_literals
import sys
import psycopg2

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

if len(sys.argv) != 2:
	#Case where we print out all the words in the stream and their total count of occurrences, sorted alphabetically in an ascending order, one word per line                                           
    print ("Please enter two numbers separated by only a comma as single argument, where the first is less than or equal to the second")
else:
    ks = sys.argv[1].split(',')
    if len(ks) != 2 or not (ks[0].isdigit() and ks[1].isdigit) or int(ks[0]) > int(ks[1]):
        print("Please enter two numbers separated by only a comma as a single argument, where the first is less than or equal to the second")
    else:
        cur.execute("SELECT word, count from Tweetwordcount WHERE count >= %s AND count <= %s" % (ks[0], ks[1]))
        records = cur.fetchall()
        for rec in records:
            print (rec[0] + ": " + str(rec[1]) + "\n")

    # w = str(sys.argv[1])
    # #Case where we print number of occurrences of sys.argv[1]
    # cur.execute("SELECT word, count from Tweetwordcount WHERE word = \'%s\'" % (w))
    # records = cur.fetchall()
    # for rec in records:
    #    print ("Total number of occurrences of \"" + rec[0] + "\": " + str(rec[1]) + "\n")
conn.commit()
conn.close()
