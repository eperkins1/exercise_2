#!/usr/bin/env python                                                                                                                                                                                       
from __future__ import absolute_import, print_function, unicode_literals
import numpy as np
import matplotlib.pyplot as plt
import sys
import psycopg2

multiple_bars = plt.figure()
words = []
counts = []

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("SELECT word, count from Tweetwordcount ORDER BY count DESC LIMIT 20")
records = cur.fetchall()
for rec in records:
	words.append(rec[0])
	counts.append(int(rec[1]))

plt.bar([1:20], counts, align='center')
plt.xticks(words, LABELS)

# x = [datetime.datetime(2011, 1, 4, 0, 0),
#      datetime.datetime(2011, 1, 5, 0, 0),
#      datetime.datetime(2011, 1, 6, 0, 0)]
# x = date2num(x)

# y = [4, 9, 2]
# z=[1,2,3]
# k=[11,12,13]

# ax = plt.subplot(111)
# ax.bar(x-0.2, y,width=0.2)
# ax.bar(x, z,width=0.2)
# ax.bar(x+0.2, k,width=0.2)
# ax.xaxis_date()

plt.show()

conn.commit()
conn.close()