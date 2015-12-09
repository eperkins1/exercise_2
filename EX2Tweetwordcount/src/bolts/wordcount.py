from __future__ import absolute_import, print_function, unicode_literals
import psycopg2
from collections import Counter
from streamparse.bolt import Bolt
#Figure out password



class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        self.conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
       

    def process(self, tup):
        word = tup.values[0]

        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount 
        # Table name: Tweetwordcount 
        # you need to create both the database and the table in advance.
        #set cursor
        cur = self.conn.cursor()
        #Create new entry if word is first of its kind
        if self.counts[word] == 1:
            cur.execute("INSERT INTO Tweetwordcount (word,count) \
                VALUES (%s, 1)", (word));
        #Update count if word has already occurred
        else:
            cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s", (self.counts[word], word))
        self.conn.commit()

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
