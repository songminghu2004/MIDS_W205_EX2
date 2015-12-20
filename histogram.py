import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Print outputs according to differnt command line arguments 
# Print error for other usage
if len(sys.argv) != 3:
    print('usage: python finalresults.py num1 num2')    

num1 = sys.argv[1]
num2 = sys.argv[2]

# Use psycopg to connect to Postgres
# Database name: Tcount;  Fields :  db_word and count 
# Table name: Tweetwordcount 
conn = psycopg2.connect(database="tcount", user="postgres", password="postgres", host="127.0.0.1", port="5432")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Create a cursor 
cur = conn.cursor()   

# Pull out seleced data from Tweetwordcount   
cur.execute("SELECT db_word, count FROM Tweetwordcount WHERE count>= %s and count <=%s;" %  (num1, num2) )

records = cur.fetchall()
for rec in records:
    print(rec[0], rec[1] )


#Closing cursor and connection
cur.close()
conn.close()
