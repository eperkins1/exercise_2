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


# plt.bar(wordnums, counts, align='center')
# plt.xticks(np.arange(20), words)

# Set up the axes and figure
fig, ax = plt.subplots()

# Make a bar plot, ignoring the date values
ax.bar(np.arange(20), counts, align='center', width=1.0)
ax.xticks(np.arange(20), words)

# Force matplotlib to place a tick at every bar and label them with the date
ax.tick_params(axis='x', pad=8) #Same as plt.xticks

plt.savefig('foo.png')

conn.commit()
conn.close()
