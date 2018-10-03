import sqlite3


#making the database file a variable
sqlite_file = 'chatbot_db.sqlite'  



# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


#creating tables and text for the questions and answers
c.execute('''create table questions

(id integer primary key,

question text,

 answer text)''')


#Inserting values for questions in answers, so the database knows the keyword from the query
c.execute('''insert into questions (question,answer) values('what type of bags are bad', 'single use plastic bags are the ones in question')  ''')

c.execute('''insert into questions (question,answer) values('are plastic bags that bad', 'In short no, but how we dispose of them is bad')  ''')

c.execute('''insert into questions (question,answer) values('are plastic bags recyclable', 'Almost everything is recyclable and plastic bags are not an exception')  ''')

c.execute('''insert into questions (question,answer) values('how are you', 'I am good, but why don’t you try asking a question that I was designed for') ''')

#closing conetion with the database and committing changes
conn.commit()
conn.close()





