
# Daniel Herbert 2018
# This program simulates a basic chatbot program

# sqlite3 is a very easy to use database engine that is embedded with Python
import sqlite3

#make the UI a little prettier, by adding a line under each statement
line = "_______________________________"

# name of the sqlite database file
sqlite_file = 'chatbot_db.sqlite'    

# Connecting to the database file, conn = connect, this is required if you want a connection with the database
conn = sqlite3.connect(sqlite_file)

#lets the program perform sql comand
sql_cursor = conn.cursor()



#meet and greet message made into function. I have done this because this message needs to be called multible times.                                                                                                                                                                                         
def welcome_message():
   print(line +"\n"   print("""Hello, my name is Stark and I am here to
help you learn about single use plastic bags.\n""" + line)
   print('')
   print("Just ask me anything about plastic bags and I will inform you.\n"+ line)

#start of conversation
welcome_message()

#while loop, continue asking qustions, I have done this because I want the chat bot to continue asking questions.
# keywords recognised are 'help' and 'quit'
# help = just reprints the welcome message
# quit = will allow the program to terminate cleanly
# otherwise program will continue waiting for an input and comparing the user input with known questions
# if a match is found, the respective answer is returned otherwise it will ask the user to re-enter the question
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
#command for searching based on text entry from input from user and checking it with database
   sql_cursor.execute("select answer from questions where question like ?", (searchstring,) )
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

