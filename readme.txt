tep-by-step instructions: 

1. make sure that the Postgres database "Tcount" has been created

2. start the storm application and deposite the data into the postgres database
   enter the EX2Tweetwordcount folder, type the command, "sparse run", to start the storm application for the EX2Tweetwordcount project. 

   the emitted words and word counts will be save into the table "Tweetwordcount" under the Database "Tcount"

3. submit queries encoded in Python to pull out the data and generate the bar plot

3.1. finalresults.py with a word argument
     for a given word, submit the command "python finalresults.py <word>".  It will print out the total number of word occurrences in the stream. 
     for example "python finalresults.py hello" will print out "$ Total number of occurences of “hello”: 10"

3.2. finalresults.py without any argument
     submit the command "python finalresults.py" without any argument.  It will print out the total number of word occurrences in the stream. 
     for example "python finalresults.py" will print out all the words in the stream and their total count of occurrences,
     Those  words are sorted alphabetically in an ascending order and each line will be associated with one word and its count.

3.3  histogram.py
     submit the command, e.g. "python histogram.py k1 k2", to obtain all the words that their total number of occurrences in the stream 
     that is more or equal than k1 and less or equal than k2.   

