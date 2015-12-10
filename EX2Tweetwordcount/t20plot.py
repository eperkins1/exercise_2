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

wordnums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#wordlens = []
#for word in words:
#	wordlens.append(len(word))
#interval = max(wordlens)
#curlen = 0
#for word in words:
#	curlen += interval
#	wordnums.append(curlen)
plt.bar(wordnums, counts, align='center')
plt.xticks(np.arange(20), words)

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

plt.savefig('foo.png')

conn.commit()
conn.close()
