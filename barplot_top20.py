import sys
import matplotlib.pyplot as plt
import numpy as np
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Use psycopg to connect to Postgres
# Database name: Tcount;  Fields :  db_word and count 
# Table name: Tweetwordcount 
conn = psycopg2.connect(database="tcount", user="postgres", password="postgres", host="127.0.0.1", port="5432")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Create a cursor 
cur = conn.cursor()   

# Pull out seleced data from Tweetwordcount   
cur.execute("SELECT db_word, count FROM Tweetwordcount ORDER by COUNT DESC LIMIT 20;") 
y_val = []
x_label = []

records = cur.fetchall()
type(records) 
for rec in records:
    x_label.append(rec[0])
    y_val.append(rec[1])

x_val = np.arange(len(x_label))

plt.barh(x_val, y_val, align='center', alpha=0.5)
plt.yticks(x_val, x_label)
plt.ylabel('Count')
plt.title('Top 20 Word Count')
plt.show()

#Closing cursor and connection
cur.close()
conn.close()
