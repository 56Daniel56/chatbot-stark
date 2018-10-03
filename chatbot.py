
# Daniel Herbert 2018

# Selecting rows using a search string from keyboard

import sqlite3
#make the interface tidier by adding a line under each statement
line = "_______________________________"

sqlite_file = 'chatbot_db.sqlite'    # name of the sqlite database file

# Connecting to the database file, conn = connect, this is required if you want a connection with the database
conn = sqlite3.connect(sqlite_file)
#lets the program preform sql comands, very common varible name in sql programing
cur = conn.cursor()

#start of conversation

#meet and greet message made into function. I have done this because this message needs to be called multible times.                                                                                                                                                                                         
def welcome_message():
   print(line +"\n"   print("""Hello, my name is Stark and I am here to
help you learn about single use plastic bags.\n""" + line)
   print('')
   print("Just ask me anything about plastic bags and I will inform you.\n"+ line)

welcome_message()

#while loop to continue asking qustions, I have done this because I want the chat bot to continue asking questions.
while True:
   print("")
   searchstring = input("What's the question?: ")
   print(line)
   if not searchstring:
      print ("\nPlease try again\n"+ line +"\n")
      continue
   if(len(searchstring)==0):
      print ("\nPlease try again\n"+ line +"\n")
      continue
   if searchstring == "quit":
      print("Thanks, bye.")
      break
   if searchstring == "help":
      welcome_message()
      continue
#comand forsearhing for keyword from input from user and checking it with database
   cur.execute("select answer from questions where question like ?", (searchstring,) )
   for row in cur.fetchall():
      print ("\n" + row[0])
      print(line)
      break
   else:
      print("\nSorry, I dont understand. Please rephrase or change you question\n" + line)
      print('')

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()

