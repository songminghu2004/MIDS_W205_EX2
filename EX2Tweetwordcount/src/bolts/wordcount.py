from __future__ import absolute_import, print_function, unicode_literals
from collections import Counter
from streamparse.bolt import Bolt
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class WordCounter(Bolt):
    
    def initialize(self, conf, ctx):
        self.counts = Counter()
    
    def process(self, tup):
        word = tup.values[0]
            
        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount 
        # Table name: Tweetwordcount 
        # you need to create both the database and the table in advance.
        conn = psycopg2.connect(database="tcount", user="postgres", password="postgres", host="127.0.0.1", port="5432")
        
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        #conn.autocommit = True
        #conn.set_isolation_level(0)
        
        #create a cursor 
        cur = conn.cursor()
        
        #Create a table  Tweetwordcount
        try:
           cur.execute('''CREATE TABLE Tweetwordcount (db_word TEXT PRIMARY KEY, count INT);''')
        except Exception, e:
           print("Table Tweetwordcount exists")
            
        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])
        
        #Insert word and count into the database
        #cur.execute("INSERT INTO Tweetwordcount (db_word,count) VALUES (%s, %s)", (word, self.counts[word]))
        
        cur.execute("SELECT db_word FROM Tweetwordcount WHERE db_word = %s", (word,))
        if cur.fetchone() is not None:
            cur.execute("UPDATE Tweetwordcount SET count = %s WHERE db_word = %s;", (self.counts[word],word)  )
        else:
            cur.execute("INSERT INTO Tweetwordcount (db_word,count) VALUES (%s, %s);", (word, self.counts[word]))
        
        
        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
        
        cur.close()
        conn.close()

